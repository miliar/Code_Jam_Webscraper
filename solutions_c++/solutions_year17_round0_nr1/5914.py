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

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	REP(c, T){
		string S;
		int K;
		cin >> S >> K;

		int N = S.length();
		VI A(N + 1, 0);
		int ret = 0;

		REP(i, N){
			if(i != 0) A[i] += A[i - 1];
			if(N - K < i) continue;
			if((S[i] == '-' && (A[i] % 2) == 0)
			|| (S[i] == '+' && (A[i] % 2) == 1)){
				A[i]++;
				A[i + K]--;
				ret++;
			}
		}

		bool ok = true;
		FOR(i, N - K, N){
			if((S[i] == '-' && (A[i] % 2) == 0)
			|| (S[i] == '+' && (A[i] % 2) == 1)){
				ok = false;
			}
		}

//		EACH(a, A) cout << a << " ";
//		cout << endl;

		cout << "Case #" << c + 1 << ": ";
		if(ok) cout << ret << endl;
		else cout << "IMPOSSIBLE" << endl;

	}

	return 0;
}
