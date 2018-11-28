
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 52;

int kaf(const int &x,const int &y){return x/y;}
int saghf(const int &x,const int &y){return (x+y-1)/y;}

int a[MN] , b[MN][MN] , val[2*MN*MN];
//pii vec[MN][MN];
multiset<pii>st[MN];
int sz , n , m;
set<pii> :: iterator it;

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T, cnt=0;
	cin >> T;
	while(T--){
		++cnt;
		cin >> n >> m;
		for(int i=0;i<n;++i) cin >> a[i];
		sz=0;
		for(int i=0;i<n;++i){
			st[i].clear();
			for(int j=0;j<m;++j){
				cin >> b[i][j];
				int l , r;
				l = saghf(10*b[i][j] , 11*a[i]) , r = kaf(10*b[i][j] , 9*a[i]);
				st[i].insert({r , l});
//				vec[i][j] = {r , l};
//				cout << "[" << l << ',' << r << "] ";
				//		cout << i << ' ' << j << ' ' << l << ' ' << r << '\n';
				val[sz++] = l , val[sz++] = r;
			}
//			cout << '\n';
//			sort(vec[i] , vec[i]+m);
		}

		int ans = 0;
		sort(val , val+sz);
		sz = unique(val , val+sz) - val;
		
/*		for(int i=0;i<n;++i){
			for(auto x:st[i]) cout << x.second << ' ' << x.first << '\n';
			cout << "***\n";
		}
*/
	//	cout << "HI" << ' ' << sz << ' ' << val[sz-1] << endl;
		for(int i=0;i<sz;++i){
	//		cout << i << ' ' << val[i] << endl;
			bool Check = true;
			vector<pii> Tmp;
			for(int r=0;r<n;++r){
				if(st[r].empty()){
					Check = false;
					continue;
				}
				it = st[r].lower_bound(make_pair(val[i] , -INF));
				if(it == st[r].end()){
					Check = false;
					continue;
				}
				Tmp.pb(*it);
				if(it->second > val[i])
					Check = false;
			}
//			cout << "Check"<< ' ' << Check << '\n';
//			cout << "-----\n";
			if(Check){
				ans++;
				for(int r=0;r<n;++r) st[r].erase(st[r].find(Tmp[r]));
				--i;
			}
		}
		cout << "Case #" << cnt << ": " << ans << '\n';
	}
	return 0;
}

