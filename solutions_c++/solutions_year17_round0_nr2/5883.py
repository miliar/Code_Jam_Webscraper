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

unsigned long long digit(unsigned long long N, unsigned long long A){
	return (N / A) % 10;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	REP(c, T){
		unsigned long long N;
		cin >> N;

		unsigned long long A = 1;
		while(A < 1e19){
			if(digit(N, A * 10) > digit(N, A)){
				N -= (digit(N, A) + 1) * A;
//				cout << N << endl;
				N += A - (N % A) - 1;
			}
			A *= 10;
		}

		cout << "Case #" << c + 1 << ": " << N << endl;

	}

	return 0;
}
