#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
#include <ctime>
#include <sstream>
#include <algorithm>
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

string int2str(lli v){
    stringstream ss;
    ss << v;
    string s;
    ss >> s;
    return s;
}

bool inline tidy_chk(int n){
    int last = 10;
    do {
        if (last < n%10) return false;
        last = n%10;
        n /= 10;
    } while (n > 0);
    return true;
}

void brute_chk(lli N, string ans){
    int thr = int(2e8);
    if (N > 1ll*thr) {
        WR(cerr << escY "[Skipped brute. " DB(N) << " greater then " DB(thr) << "] " escRS;)
        return;
    }
    int n = N;
    while (!tidy_chk(n)) --n;
    string bans = int2str(n);
    if (bans == ans) {
        WR(cerr << escG "[Passed brute] " escRS;)
        return;
    }
    WR(cerr << escR "[Failed brute, for " << N << " ans is " << bans << "] " escRS;)
}

void solve(){
    lli N;
    cin >> N;
    string ans = int2str(N);
    int mi = ans.size(), dir = 1;
    for (int i = 0; 0 <= i && i < ans.size()-1; i += dir) {
        if (ans[i] > ans[i+1]) {
            --ans[i];
            mi = i+1;
            dir = -1;
        }
    }
    if (mi == 0 || ans[0] == '0') ans.resize(ans.size()-1), mi = 0;
    SEG(i,mi,ans.size()-1) ans[i] = '9';
    // reverse(ans.begin(), ans.end());
    // char last = '9';
    // int Mi = -1;
    // REP(ans.size()) {
    //     if (last < ans[i]) ans[i] = last, Mi = max(i,Mi);
    //     last = ans[i];
    // }
    // REP(Mi) ans[i] = '9';
    // if (ans.back() == '0') ans.resize(ans.size()-1);
    // reverse(ans.begin(), ans.end());
    WR(brute_chk(N, ans);)
	cout << ans << endl;
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
