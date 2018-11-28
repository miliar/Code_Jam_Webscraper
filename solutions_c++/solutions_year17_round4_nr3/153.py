// 2SAT code from my contest lib https://github.com/ttalvitie/libcontest/blob/master/src/logic/2sat.hpp
#include <iostream>
#include <climits>
#include <vector>
#include <array>
#include <map>

using namespace std;
typedef long long int Z;

typedef pair<int, bool> PIB;

/// Solve 2SAT-problem, i.e. find assignments of x_0...x_(n-1) to true or false
/// such that all clauses in 'clauses' hold. The clauses are given as
/// ((i1, v1), (i2, v2)), and a clause holds if x_i1 == v1 or x_i2 == v2.
/// The function returns true if there is such an assignment and replaces the
/// content of 'solution' to one solution, otherwise returns false.
bool solve2SAT(int n, const vector<pair<PIB, PIB>>& clauses, vector<char>& solution) {
	vector<vector<PIB>> imp[2];
	imp[0].resize(n);
	imp[1].resize(n);
	
	for(pair<PIB, PIB> clause : clauses) {
		PIB a = clause.first;
		PIB b = clause.second;
		imp[!a.second][a.first].push_back(b);
		imp[!b.second][b.first].push_back(a);
	}
	
	vector<char> isset[2];
	vector<char> val[2];
	vector<int> log[2];
	vector<int> stack[2];
	vector<int> pos[2];
	
	for(int b = 0; b < 2; ++b) {
		isset[b].resize(n, false);
		val[b].resize(n);
		pos[b].resize(n);
	}
	
	int win = 0;
	for(int i = 0; i < n; ++i) {
		if(isset[0][i]) continue;
		
		bool failed[2] = {false, false};
		
		for(int b = 0; b < 2; ++b) {
			isset[b][i] = true;
			val[b][i] = b;
			pos[b][i] = 0;
			
			log[b].clear();
			stack[b].clear();
			
			log[b].push_back(i);
			stack[b].push_back(i);
		}
		
		win = -1;
		while(win == -1 && !(failed[0] && failed[1])) {
			for(int b = 0; b < 2; ++b) {
				if(failed[b]) continue;
				if(stack[b].empty()) {
					win = b;
					break;
				}
				
				int x = stack[b].back();
				bool v = val[b][x];
				
				if(pos[b][x] == imp[v][x].size()) {
					stack[b].pop_back();
				} else {
					PIB p = imp[v][x][pos[b][x]++];
					
					int y = p.first;
					if(isset[b][y]) {
						if(val[b][y] != p.second) {
							failed[b] = true;
							continue;
						}
					} else {
						isset[b][y] = true;
						val[b][y] = p.second;
						log[b].push_back(y);
						
						pos[b][y] = 0;
						stack[b].push_back(y);
					}
				}
			}
		}
		if(win == -1) break;
		
		int lose = 1 - win;
		for(int v : log[lose]) {
			isset[lose][v] = false;
		}
		for(int v : log[win]) {
			isset[lose][v] = true;
			val[lose][v] = val[win][v];
		}
	}
	if(win == -1) return false;
	
	solution = move(val[0]);
	return true;
}

int R, C;
char X[55][55];
vector<pair<int, int>> P;
bool allowH[128];
bool allowV[128];
vector<pair<int, bool>> seenBy[55][55];

bool tr(int i, int j, int di, int dj, int m, bool d) {
	while(true) {
		i += di;
		j += dj;
		if(X[i][j] == '#') return true;
		if(X[i][j] == '+') return false;
		if(X[i][j] == '/') {
			swap(di, dj);
			di = -di;
			dj = -dj;
		}
		if(X[i][j] == '\\') {
			swap(di, dj);
		}
		if(X[i][j] == '.') {
			seenBy[i][j].emplace_back(m, d);
		}
	}
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int Tc;
	cin >> Tc;
	
	for(int Ti = 1; Ti <= Tc; ++Ti) {
		cin >> R >> C;
		for(int j = 0; j <= C + 1; ++j) {
			X[0][j] = '#';
			X[R + 1][j] = '#';
		}
		for(int i = 0; i < R; ++i) {
			string S;
			cin >> S;
			X[i][0] = '#';
			for(int j = 0; j < C; ++j) {
				X[i + 1][j + 1] = S[j];
			}
			X[i][C + 1] = '#';
		}
		P.clear();
		for(int i = 1; i <= R; ++i) {
			for(int j = 1; j <= C; ++j) {
				if(X[i][j] == '|' || X[i][j] == '-') {
					P.emplace_back(i, j);
					X[i][j] = '+';
				}
			}
		}
		fill(allowH, allowH + 128, false);
		fill(allowV, allowV + 128, false);
		
		for(int i = 0; i < 55; ++i) {
			for(int j = 0; j < 55; ++j) {
				seenBy[i][j].clear();
			}
		}
		
		for(int i = 0; i < (int)P.size(); ++i) {
			auto p = P[i];
			if(tr(p.first, p.second, 0, -1, i, false) && tr(p.first, p.second, 0, 1, i, false)) {
				allowH[i] = true;
			}
			if(tr(p.first, p.second, -1, 0, i, true) && tr(p.first, p.second, 1, 0, i, true)) {
				allowV[i] = true;
			}
		}
		
		vector<pair<PIB, PIB>> clauses;
		bool ok = true;
		for(int i = 1; i <= R; ++i) {
			for(int j = 1; j <= C; ++j) {
				if(X[i][j] == '.') {
					if(seenBy[i][j].empty()) {
						ok = false;
					} else if(seenBy[i][j].size() == 1) {
						clauses.emplace_back(seenBy[i][j][0], seenBy[i][j][0]);
					} else {
						if(seenBy[i][j].size() != 2) throw 0;
						clauses.emplace_back(seenBy[i][j][0], seenBy[i][j][1]);
					}
				}
			}
		}
		
		for(int i = 0; i < (int)P.size(); ++i) {
			if(!allowH[i]) {
				clauses.emplace_back(PIB(i, true), PIB(i, true));
			}
			if(!allowV[i]) {
				clauses.emplace_back(PIB(i, false), PIB(i, false));
			}
		}
		
		vector<char> solution;
		if(ok) {
			ok = solve2SAT(P.size(), clauses, solution);
		}
		
		cout << "Case #" << Ti << ": ";
		if(ok) {
			cout << "POSSIBLE\n";
			for(int i = 0; i < (int)P.size(); ++i) {
				auto p = P[i];
				if(solution[i]) {
					X[p.first][p.second] = '|';
				} else {
					X[p.first][p.second] = '-';
				}
			}
			for(int i = 1; i <= R; ++i) {
				for(int j = 1; j <= C; ++j) {
					cout << X[i][j];
				}
				cout << '\n';
			}
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
	
	return 0;
}
