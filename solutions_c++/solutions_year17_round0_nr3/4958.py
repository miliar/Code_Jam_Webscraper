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

template <typename T>
struct reversion_wrapper { T& iterable; };

template <typename T>
auto begin (reversion_wrapper<T> w) { return rbegin(w.iterable); }

template <typename T>
auto end (reversion_wrapper<T> w) { return rend(w.iterable); }

template <typename T>
reversion_wrapper<T> reverse (T&& iterable) { return { iterable }; }


int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		LL n,k;
		cin >> n >> k;
		map<LL,LL> mp;
		LL sum = 1;
		mp[n] = 1;
		while(k > sum){
			k -= sum;
			map<LL,LL> nex;
			LL nsum = 0;
			for(auto&& e : mp) {
				LL f,s;
				tie(f,s) = e;
				f--;
				if(f/2 > 0){
					nex[f/2] += s;
					nsum += s;
				}
				nex[f-f/2] += s;
				nsum += s;
			}
			sum = nsum;
			swap(nex,mp);
			DEBUG(SZ(mp));
		}
		LL ans1, ans2;
		for(auto&& e : reverse(mp)) {
			if(e.S < k){
				k -= e.S;
			}else{
				ans2 = (e.F-1)/2;
				ans1 = e.F-1-ans2;
				break;
			}
		}
		WRC(hoge);
		cout << ans1 << ' ' << ans2 << endl;
	}
	return 0;
}
