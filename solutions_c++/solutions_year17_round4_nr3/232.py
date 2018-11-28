#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdlib>

using namespace std;
using pii = pair<int, int>;
static const int dx[] = { 1, 0, -1, 0 };
static const int dy[] = { 0, -1, 0, 1 };

inline bool between(int a, int b, int c){
	return a <= b && b < c;
}

bool is_safe(const vector<string>& field, int i, int j, int d){
	const int r = field.size(), c = field[0].size();
	while(true){
		i += dy[d]; j += dx[d];
		if(!between(0, i, r) || !between(0, j, c)){ return true; }
		if(field[i][j] == '#'){ return true; }
		if(field[i][j] == '-' || field[i][j] == '|'){ return false; }
		if(field[i][j] == '/'){
			d ^= 1;
		}else if(field[i][j] == '\\'){
			d ^= 3;
		}
	}
	return true;
}

void simulate(
	vector<vector<vector<int>>>& v,
	const vector<string>& field,
	int i, int j, int d, int x)
{
	const int r = field.size(), c = field[0].size();
	while(true){
		i += dy[d]; j += dx[d];
		if(!between(0, i, r) || !between(0, j, c)){ return; }
		if(field[i][j] == '#'){ return; }
		if(field[i][j] == '-' || field[i][j] == '|'){ return; }
		if(field[i][j] == '/'){
			d ^= 1;
		}else if(field[i][j] == '\\'){
			d ^= 3;
		}else if(field[i][j] == '.'){
			v[i][j].push_back(x);
		}
	}
}

pair<bool, vector<int>> solve(const vector<vector<int>>& cnf){
	int n = 0, m = cnf.size();
	for(const auto& row : cnf){
		for(const auto x : row){ n = max(n, abs(x)); }
	}
	ofstream ofs("cnf.dimacs");
	ofs << "p cnf " << n << " " << m << endl;
	for(const auto& row : cnf){
		for(const auto x : row){ ofs << x << " "; }
		ofs << 0 << endl;
	}
	ofs.close();
	system("minisat cnf.dimacs minisat.txt 2>&1 > /dev/null");
	ifstream ifs("minisat.txt");
	string sat;
	ifs >> sat;
	if(sat == "SAT"){
		vector<int> result;
		int x;
		while(ifs >> x){
			result.push_back(x);
			if(x == 0){ break; }
		}
		ifs.close();
		return make_pair(true, result);
	}else{
		ifs.close();
		return make_pair(false, vector<int>());
	}
}
	

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int case_num = 1; case_num <= T; ++case_num){
		int r, c;
		cin >> r >> c;
		vector<string> field(r);
		for(int i = 0; i < r; ++i){ cin >> field[i]; }
		int n_empty = 0, n_source = 0;
		vector<vector<int>> empty_index(r, vector<int>(c, -1));
		vector<vector<int>> source_index(r, vector<int>(c, -1));
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				if(field[i][j] == '-' || field[i][j] == '|'){
					source_index[i][j] = n_source++;
				}else if(field[i][j] == '.'){
					empty_index[i][j] = n_empty++;
				}
			}
		}
		vector<vector<int>> cnf;
		vector<vector<vector<int>>> v(r, vector<vector<int>>(c));
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				if(field[i][j] != '-' && field[i][j] != '|'){ continue; }
				const int k = source_index[i][j] + 1;
				if(is_safe(field, i, j, 0) && is_safe(field, i, j, 2)){
					simulate(v, field, i, j, 0, k);
					simulate(v, field, i, j, 2, k);
				}else{
					cnf.push_back(vector<int>(1, -k));
				}
				if(is_safe(field, i, j, 1) && is_safe(field, i, j, 3)){
					simulate(v, field, i, j, 1, -k);
					simulate(v, field, i, j, 3, -k);
				}else{
					cnf.push_back(vector<int>(1, k));
				}
			}
		}
		bool answer = true;
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				if(empty_index[i][j] < 0){ continue; }
				if(v[i][j].empty()){
					answer = false;
				}else{
					cnf.push_back(v[i][j]);
				}
			}
		}
		if(answer){
			const auto sat = solve(cnf);
			if(sat.first){
				vector<int> d(n_source, '-');
				for(const auto i : sat.second){
					if(i > 0){
						d[i - 1] = '-';
					}else if(i < 0){
						d[-i - 1] = '|';
					}
				}
				for(int i = 0; i < r; ++i){
					for(int j = 0; j < c; ++j){
						if(source_index[i][j] >= 0){
							field[i][j] = d[source_index[i][j]];
						}
					}
				}
			}else{
				answer = false;
			}
		}
		cout << "Case #" << case_num << ": " << (answer ? "POSSIBLE" : "IMPOSSIBLE") << endl;
		if(answer){
			for(const auto& line : field){ cout << line << endl; }
		}
	}
	return 0;
}

