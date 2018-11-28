#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
#include <ctime>
#include <cassert>
using namespace std;
#define DB(a) << #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < int(n); ++i)
#define FOR(i,n) for (int i = 0; i < int(n); ++i)
#define SEG(i,a,b) for (int i = (a); i <= (b); ++i)
#define escRS "\u001B[0m"
#define escBK "\u001B[30m"
#define escR "\u001B[31m"
#define escG "\u001B[32m"
#define escY "\u001B[33m"
#define escBL "\u001B[34m"
#define escP "\u001B[35m"
#define escC "\u001B[36m"
#define escW "\u001B[37m"
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

const int NMAX = (int)1e3;

char id2colBIN(int id){
	switch (id) {
		case 1: return 'B';
		case 2: return 'Y';
		case 3: return 'G';
		case 4: return 'R';
		case 5: return 'V';
		case 6: return 'O';
		default: return '?';
	}
}

char id2colRYB(int id){
	switch (id) {
		case 0: return 'R';
		case 1: return 'Y';
		case 2: return 'B';
		default: return '?';
	}
}

int gmax(vector <int> & ryb, int nid) {
	int Mi = -1, Mx = 0;
	REP(ryb.size()) if (i != nid && Mx < ryb[i]) Mx = ryb[i], Mi = i;
	return Mi;
}

int ans[NMAX];

bool tryslv(int fst, vector <int> ryb, int N){
	// CR(DB(fst) DB(N))
	if (!ryb[fst]) return false;
	ans[0] = fst; --ryb[fst];
	REP(N-1) {
		// WR(cerr << "\tRYB:"; REP(3) cerr << ryb[i] << " "; cerr << endl;)
		ans[i+1] = gmax(ryb, ans[i]);
		if (ans[i+1] == -1 || ryb[ans[i+1]] <= 0) return false;
		// CR("\t" DB(ans[i+1]))
		--ryb[ans[i+1]];
	}

	// string s; s.resize(N);
	// REP(N) s[i] = id2colRYB(ans[i]);
	// CR(DB(s))

	return ans[0] != ans[N-1];
}

void solve(){
	// WR(cerr << endl;)
	//int R,O,Y,G,B,V;
	// cin >> N >> R >> O >> Y >> G >> B >> V;
	int N;
	vector <int> a(7);
	cin >> N >> a[4] >> a[6] >> a[2] >> a[3] >> a[1] >> a[5];

	vector <int> ryb = {a[4], a[2], a[1]};
	int n = 0; REP(ryb.size()) n += ryb[i];

	if (!tryslv(0, ryb, n)) if (!tryslv(1, ryb, n)) if (!tryslv(2, ryb, n)) {
		cout << "IMPOSSIBLE\n";
		WR(assert(ryb[0] > ryb[1] + ryb[2] || ryb[1] > ryb[0] + ryb[2] || ryb[2] > ryb[1] + ryb[0]);)
		CR("==============")
		return;
	}
	string s; s.resize(N);
	REP(n) s[i] = id2colRYB(ans[i]);

	cout << s << endl;

	assert(N == n);
	REP(N) assert(s[i] != s[(i+1)%N]);
	CR("==============")
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
