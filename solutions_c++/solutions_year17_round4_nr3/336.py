#include <bits/stdc++.h>

#define DEBUG

#ifdef DEBUG
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif

using namespace std;

int r, c;

void erase(int x, int y, vector<string>& v, set<pair<int, int>>& s){
	if (v[x][y] == '-'){
		for (int w = y; w--; ){
			if (v[x][w] == '.')
				s.erase({x, w});
			if (v[x][w] == '#')
				break;
		}
		for (int w = y + 1; w < c; ++w){
			if (v[x][w] == '.')
				s.erase({x, w});
			if (v[x][w] == '#')
				break;
		}
	} else if (v[x][y] == '|'){
		for (int w = x; w--; ){
			if (v[w][y] == '.')
				s.erase({w, y});
			if (v[w][y] == '#')
				break;
		}
		for (int w = x + 1; w < r; ++w){
			if (v[w][y] == '.')
				s.erase({w, y});
			if (v[w][y] == '#')
				break;
		}
	} else {
		assert(0);
	}
}

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		cin >> r >> c;
		vector<string> v(r);
		vector<pair<int, int>> shooter;
		set<pair<int, int>> s;
		for (int i = 0; i < r; ++i){
			cin >> v[i];
			for (int j = 0; j < c; ++j){
				if (v[i][j] == '-' || v[i][j] == '|'){
					shooter.push_back({i, j});
					v[i][j] = '-';
				}
				else if (v[i][j] == '.')
					s.insert({i, j});
			}
		}
		vector<pair<int, int>> a;
		bool next = false;
		for (int i = 0; i < shooter.size(); ++i){
			int x = shooter[i].first, y = shooter[i].second;
			bool flag1 = false, flag2 = false;
			for (int w = x; w--; ){
				if (v[w][y] == '-' || v[w][y] == '|'){
					flag1 = true;
				}
				if (v[w][y] == '#')
					break;
			}
			for (int w = x + 1; w < r; ++w){
				if (v[w][y] == '-' || v[w][y] == '|'){
					flag1 = true;
				}
				if (v[w][y] == '#')
					break;
			}
			for (int w = y; w--; ){
				if (v[x][w] == '-' || v[x][w] == '|'){
					flag2 = true;
				}
				if (v[x][w] == '#')
					break;
			}
			for (int w = y + 1; w < c; ++w){
				if (v[x][w] == '-' || v[x][w] == '|'){
					flag2 = true;
				}
				if (v[x][w] == '#')
					break;
			}
			if (flag1 && flag2){
				cout << "IMPOSSIBLE\n";
				next = true;
				break;
			} else if (flag1){
				v[x][y] = '-';
				erase(x, y, v, s);
			} else if (flag2){
				v[x][y] = '|';
				erase(x, y, v, s);
			} else {
				a.push_back({x, y});
			}
		}
		if (next)
			continue;
		if (a.empty() && s.empty()){
			cout << "POSSIBLE\n";
			for (int i = 0; i < r; ++i){
				cout << v[i] << "\n";
			}
			continue;
		}
		int sz = a.size();
		set<pair<int, int>> now = s;
		for (int i = 0; i < (1 << sz); ++i){
			for (int j = 0; j < sz; ++j){
				int x = a[j].first, y = a[j].second;
				if ((i >> j) & 1){
					v[x][y] = '|';
				} else {
					v[x][y] = '-';
				}
				erase(x, y, v, now);
			}
			if (test == 9 && i == 0){
			for (int i = 0; i < r; ++i){
				cerr << v[i] << "\n";
			}
			for (auto& x : now){
				cerr << x.first << " " << x.second << "\n";
			}
			}
			if (now.empty()){
				cout << "POSSIBLE\n";
				for (int i = 0; i < r; ++i){
					cout << v[i] << "\n";
				}
				goto NEXT;
			}
			now = s;
		}
		cout << "IMPOSSIBLE\n";
NEXT:;
	}
}