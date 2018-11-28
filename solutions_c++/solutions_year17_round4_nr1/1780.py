#ifdef LOCAL111
	#define _GLIBCXX_DEBUG
#else
	#define NDEBUG
#endif
#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
const int INF = 1e9;
using namespace std;
template<typename T, typename U> ostream& operator<< (ostream& os, const pair<T,U>& p) { cout << '(' << p.first << ' ' << p.second << ')'; return os; }

#define endl '\n'
#define ALL(a)  (a).begin(),(a).end()
#define SZ(a) int((a).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n)  FOR(i,0,n)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#ifdef LOCAL111
	#define DEBUG(x) cout<<#x<<": "<<(x)<<endl
	template<typename T> void dpite(T a, T b){ for(T ite = a; ite != b; ite++) cout << (ite == a ? "" : " ") << *ite; cout << endl;}
#else
	#define DEBUG(x) true
	template<typename T> void dpite(T a, T b){ return; }
#endif
#define F first
#define S second
#define SNP string::npos
#define WRC(hoge) cout << "Case #" << (hoge)+1 << ": "
template<typename T> void pite(T a, T b){ for(T ite = a; ite != b; ite++) cout << (ite == a ? "" : " ") << *ite; cout << endl;}
template<typename T> bool chmax(T& a, T b){if(a < b){a = b; return true;} return false;}
template<typename T> bool chmin(T& a, T b){if(a > b){a = b; return true;} return false;}

typedef long long int LL;
typedef unsigned long long ULL;
typedef pair<int,int> P;

void ios_init(){
	//cout.setf(ios::fixed);
	//cout.precision(12);
#ifdef LOCAL111
	return;
#endif
	ios::sync_with_stdio(false); cin.tie(0);	
}

int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		int n,p;
		cin >> n >> p;
		vector<int> g(n);
		REP(i,n) cin >> g[i];
		vector<int> cnt(p);
		REP(i,n){
			cnt[g[i]%p]++;
		}
		int ans = 0;
		if(p == 2){
			DEBUG(ans);
			ans += cnt[0];
			DEBUG(cnt[0]);
			DEBUG(ans);
			DEBUG(cnt[1]);
			ans += (cnt[1]+1)/2;
			DEBUG(ans);
		}else if(p == 3){
			ans += cnt[0];
			DEBUG(ans);
			int mi = min(cnt[1],cnt[2]);
			ans += mi;
			DEBUG(ans);
			DEBUG(mi);
			cnt[1] -= mi;
			cnt[2] -= mi;
			DEBUG(cnt[1]); DEBUG(cnt[2]);
			if(cnt[1] != 0){
				ans += (cnt[1]+2)/3;
			}
			if(cnt[2] != 0){
				ans += (cnt[2]+2)/3;
			}
		}else if(p == 4){

		}
		WRC(hoge);
		cout << ans << endl;
	}
	return 0;
}
