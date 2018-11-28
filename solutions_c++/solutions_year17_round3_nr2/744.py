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
	int t;
	cin >> t;
	REP(hoge,t) {
		int ac, aj;
		cin >> ac >> aj;
		if(ac+aj == 0){
			cout << 1 << endl;
			continue;
		}
		using T = tuple<int,int,int>;
		vector<T> rag;
		int cg[2] = {0,0};
		REP(i,ac){
			int l, r;
			cin >> l >> r;
			rag.emplace_back(l,r,0);
			cg[0] += r-l;
		}
		
		REP(i,aj){
			int l, r;
			cin >> l >> r;
			rag.emplace_back(l,r,1);
			cg[1] += r-l;
		}
		sort(ALL(rag));

		int anst = INF;
		REP(lo1,2) REP(lo2,2){
			auto ra = rag;
			int lll, rrr;
			int llll1 , llll2;
			tie(lll,ignore,llll1) = rag[0];
			tie(ignore,rrr,llll2) = rag.back();
			vector<int> s[3];
			int c[] = {cg[0],cg[1]};
			if(lll != 0){
				c[lo1] += 1;
				ra.emplace_back(0,1,lo1);
			}else{
				if(llll1 != lo1) continue;
			}
			if(rrr != 1440){
				c[lo2] += 1;
				ra.emplace_back(1439,1440,lo2);
			}else{
				if(llll2 != lo2) continue;
			}
			sort(ALL(ra));
			
			int tcn = 0;
			REP(i,SZ(ra)-1){
				int l,r,t;
				tie(l,r,t) = ra[i];
				int ln,tn;
				tie(ln,ignore,tn) = ra[i+1];
				if(tn == t){
					s[t].push_back(ln-r);
					c[t] += ln-r;
				}else{
					s[2].push_back(ln-r);
					tcn++;
				}
			}
			DEBUG(lo1); DEBUG(lo2); DEBUG(c[0]); DEBUG(c[1]);
			tcn += (lo1 != lo2);
			DEBUG(tcn);
			int ans = tcn;
			if(c[0] <= 1440/2 and c[1] <= 1440/2){
				ans = tcn;
			}else{
				int p = 1;
				if(c[0] > 1440/2){
					p = 0;
				}
				REP(i,SZ(s[2])){
					c[!p] += s[2][i];
				}
				sort(ALL(s[p]),greater<int>());
				DEBUG(p); dpite(ALL(s[p]));
				REP(i,SZ(s[p])){
					c[p] -= s[p][i];
					ans += 2;
					if(c[p] <= 1440/2){
						break;
					}
				}
				DEBUG(ans);
				if(c[p] > 1440/2){
					bool f = true;
					if(f) ans = INF;
				}
			}
			DEBUG(ans);
			chmin(anst,ans);
			DEBUG(endl);
		}
		WRC(hoge); cout << anst << endl;
		DEBUG(endl);
	}
	return 0;
}
