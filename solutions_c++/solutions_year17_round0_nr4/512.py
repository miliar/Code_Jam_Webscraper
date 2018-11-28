#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <random>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FOR(k,a,b) for(typeof(a) k=(a); k <= (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define REPD(k,a) for(int k=(a)-1; k >= 0; --k)
#define PB push_back 
#define MP make_pair
int N, M;
char m[105][105];

int count() {
	int points = 0;
	for (int i = 0; i < N; ++i){
		for (int j = 0; j < N; ++j) {
			if (m[i][j] == 'o') points++;
			if (m[i][j] != '.') points++;
		}
	}
	return points;
}
bool canPlacePlus(int i, int j){
	for (int a = 0; a < N; ++a){
		for (int b = 0; b < N; b++) {
			if (i == a && j == b) continue;
			if (abs(i - a) == abs(j - b) && m[a][b] != 'x' && m[a][b] != '.'){
				return false;
			}

		}
	}
	return true;
}
bool canPlaceCross(int i, int j){
	for (int a = 0; a < N; ++a){
		for (int b = 0; b < N; b++) {
			if (i == a && j == b) continue;
			if ((i==a||j==b) && m[a][b] != '+' && m[a][b] != '.'){
				return false;
			}

		}
	}
	return true;
}

void solve(){
	vector<string> ss;
	bool hasCross = false;
	bool hasO = false;
	int co;
	for (int i = 0; i < N; ++i){
		if (m[0][i] == 'x') hasCross = true;
		if (m[0][i] == 'o') {
			hasO = true; co = i;
		}
	}
	if (hasCross) {
		for (int i = 0; i < N; ++i){
			if (m[0][i] == 'x'){
				co = i;
				m[0][i] = 'o';
				std::stringstream sbuf;
				sbuf << "o " << 1 << " " << (i+1);
				ss.push_back(sbuf.str());
			}
		}
	}
	else if (! hasO){
		int i = 0;
		co = i;
		m[0][i] = 'o';
		std::stringstream sbuf;
		sbuf << "o " << 1 << " " << (i + 1);
		ss.push_back(sbuf.str());
	}
	for (int j = 0; j < N; ++j) {
		if (m[0][j] == '.'){
			m[0][j] = '+';
			std::stringstream sbuf;
			sbuf << "+ " << 1 << " " << (j + 1);
			ss.push_back(sbuf.str());
		}
	}
	for (int j = 1; j < N; ++j) {
		int i = (co + j);
		if (co >= N / 2) i = co - j;
		if (i < 0) i = j;
		if (i >= N) i = N - j - 1;
		if (m[j][i] == '.'){
			m[j][i] = 'x';
			std::stringstream sbuf;
			sbuf << "x " << (j+1) << " " << (i + 1);
			ss.push_back(sbuf.str());
		}
	}
	int i = N - 1;
	for (int j = 0; j<N; ++j) {
		if (m[i][j] != '.') continue;
		bool canPlus = canPlacePlus(i, j);
		if (canPlus) {
			m[i][j] = '+';
			std::stringstream sbuf;
			sbuf << "+ " << (i + 1) << " " << (j + 1);
			ss.push_back(sbuf.str());
		}
	}

	auto points = count();
	if (points != 3 * N - 2 && N > 1) {
		cout << "Error!" << " " << points << " " << N << endl;
		
	}

	cout << count() << " " << ss.size() << endl;
	for (auto s : ss) {
		cout << s << endl;
	}
}
int main()
{
	int T;
	
	cin >> T;
	for (int tt = 1; tt <= T; ++tt){
		cin >> N >> M;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) m[i][j] = '.';
		}
		for (int i = 0; i < M; ++i) {
			char x;
			int r,c;
			cin >> x >> r >> c;
			m[r - 1][c - 1] = x;
		}
		cout << "Case #" << tt << ": ";
		solve();
		//cout << endl;
	}
	return 0;
}
