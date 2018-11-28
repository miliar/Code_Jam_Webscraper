#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define MP make_pair
#define MT make_tuple
#define EACH(i,c) for(auto i: c)
#define SORT(c) sort((c).begin(),(c).end())

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()


bool dfs(vector<string>& s, int x1, int x2, int y1, int y2){
//	cout << x1 << " " << x2 << " " << y1 << " " << y2 << endl;
//	REP(i, s.size()) cout << s[i] << endl;
	set<char> a;
	FOR(x, x1, x2){
		FOR(y, y1, y2){
			if(s[x][y] != '?') a.insert(s[x][y]);
		}
	}

	if(a.size() == 0) return false;
	if(a.size() == 1){
		char b = *a.begin();
		FOR(x, x1, x2){
			FOR(y, y1, y2){
				s[x][y] = b;
			}
		}
		return true;
	}

	if((x1 + 1 < x2 && rand() % 2) || (y2 <= y1 + 1)){
		int d = rand() % (x2 - x1 - 1) + 1;
		if(!dfs(s, x1, x1 + d, y1, y2)) return false;
		if(!dfs(s, x1 + d, x2, y1, y2)) return false;
	}
	else{
		int d = rand() % (y2 - y1 - 1) + 1;
		if(!dfs(s, x1, x2, y1, y1 + d)) return false;
		if(!dfs(s, x1, x2, y1 + d, y2)) return false;
	}
	return true;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	REP(c, T){
		int R, C;
		cin >> R >> C;
		vector<string> S(R);
		REP(i, R) cin >> S[i];

		while(1){
			auto s = S;
			if(dfs(s, 0, R, 0, C)){
				cout << "Case #" << c + 1 << ":" << endl;
				REP(i, R) cout << s[i] << endl;
				break;
			}
		}
	}

	return 0;
}
