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
	cout.setf(ios::fixed);
	cout.precision(12);
#ifdef LOCAL111
	return;
#endif
	ios::sync_with_stdio(false); cin.tie(0);	
}

const double pi = M_PI;

int main()
{
	ios_init();
	int t;
	cin >> t;
	REP(hoge,t){
		using P = pair<double,double>;
		int k,n;
		cin >> n >> k;
		vector<P> rh(n);
		REP(i,n){
			cin >> rh[i].F >> rh[i].S;
			rh[i].S = -rh[i].S;
		}
		sort(ALL(rh));
		REP(i,n) rh[i].S = -rh[i].S;
		dpite(ALL(rh));
		double ans = 0;
		REP(i,n){
			double sum = rh[i].F*rh[i].F*pi + rh[i].S*rh[i].F*2*pi;
			vector<double> v;
			RREP(j,i){
				v.push_back(2*rh[j].S*rh[j].F*pi);
			}
			sort(ALL(v),greater<double>());
			DEBUG(SZ(v));
			if(!(SZ(v) >= k-1)) continue;
			dpite(ALL(v));
			REP(j,k-1){
				sum += v[j];
			}
			DEBUG(sum);
			chmax(ans,sum);
		}
		WRC(hoge);
		cout << ans << endl;
	}
	return 0;
}
