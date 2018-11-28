#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
#include <ctime>
#include <climits>
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

const int NMAX = (int)2e5;

void solve(){
	int D, N;
	cin >> D >> N;
	double U = 1./0;
	REP(N) {
		int Si, Vi;
		cin >> Si >> Vi;
		U = min(U, 1.*D/(D - Si)*Vi);
	}
	printf("%0.7f\n", U);
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
