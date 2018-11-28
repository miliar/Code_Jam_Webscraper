#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
#include <ctime>
using namespace std;
#define DB(a) << #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < int(n); ++i)
#define FOR(i,n) for (int i = 0; i < int(n); ++i)
#define SEG(i,a,b) for (int i = (a); i <= (b); ++i)
#ifdef DBG
#define WR(things_to_wrap) things_to_wrap
int __GOV = 0, __GOVTH = int(2e6);
#define OP {if (++__GOV > __GOVTH) cerr << "exit(1): __GOV exceeded " << __GOVTH << endl, exit(1);}
#else
#define WR(things_to_wrap)
#define OP
#endif
#define CR(text_to_cerr) WR(cerr << "" text_to_cerr << endl;)
#define mp make_pair
#define fst first
#define snd second
typedef pair <int, int> pint;
typedef long long int lli;

const int NMAX = (int)2e5;

inline char flip(char c, int times){
	if (times&1)
		return c == '+' ? '-' : '+';
	else
		return c;
}

void solve(){
	int K;
	string s;
	cin >> s >> K;
	int N = s.size();
	string dump = s;
	bool ans = true;
	int front = 0, times = 0;
	REP(N) {
		// CR(DB(s[i]) DB(i < N-K+1) DB(i))
		if (dump[i] == 'V') --front;
		if (flip(s[i], front) == '-') {
			if (i < N-K+1)
				++front, ++times, dump[i+K] = 'V';
			else
				ans = false;
		}
		s[i] = flip(s[i], front); //just to be sure later
	}
	CR(DB(ans) DB(s) DB(times))
	if (ans)
		cout << times << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main(){ // WR(srand(chrono::system_clock::now().time_since_epoch().count());)
	int T = 0;
	scanf("%d", &T);
	SEG(t,1,T){
		fprintf(stderr, "Started case #%d...\n", t);
		printf("Case #%d: ", t);
		solve();
	}
	cerr << "Finished " << T << " tests in " << 1.*clock()/CLOCKS_PER_SEC << " seconds." << endl;
	return 0;
}
