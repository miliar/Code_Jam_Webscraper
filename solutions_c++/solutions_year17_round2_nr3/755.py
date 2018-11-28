#include <bits/stdc++.h>

#define f(_i, _n) for (auto _i = 0; _i < _n; _i++)
#define F(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define fr(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define r(_t, _n)     _t _n;     cin >> _n;
#define ra(_type, _name, _len)_type _name[_len]; f(_i, _len)    cin >> _name[_len];
#define mp make_pair
#define re return
#define takedown re 0;
#define fi first
#define se second
#define in(_name) freopen(_name, "r", stdin);
#define out(_name) freopen(_name, "w", stdout);
#define pb push_back
#define fill(_a, _n) memset(_a, _n, sizeof(_a))
#define all(_v) _v.begin(), _v.end()
#define deb cout << "  DEBUG "
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;


ll d[150][150];
double ans[150];
ll e[150], s[150];
void solve(int i){
    int n, q;
	cin >> n >> q;
	cout << "Case #" << i << ": ";
	f(i, n){
		cin >> e[i] >> s[i];
	}
    f(i, n) f(j, n){
		cin >> d[i][j];
		if(d[i][j] == -1) d[i][j] = 1e18;
    }
    for (int k=0; k<n; ++k)
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				d[i][j] = min (d[i][j], d[i][k] + d[k][j]);

    f(i, q){
    	int st, en;
        cin >> st >> en;
        --st; --en;
        f(i, n) ans[i] = 1e18;
        ans[st] = 0;
        set<pair<double, int> > dj;
        dj.insert({0, st});
        while(!dj.empty()){
            int cur = dj.begin()->se;
            double cans = dj.begin()->fi;
            ll mxd = e[cur];
//			deb << cur << ' ' << ans[cur] << ' ' << mxd << endl;
            dj.erase(dj.begin());
            f(i, n){
				if(i != cur){
					if(d[cur][i] <= mxd && ans[i] > cans + 1. * d[cur][i] / s[cur]){
						dj.erase({ans[i], i});
						ans[i] = cans + 1. * d[cur][i] / s[cur];
						dj.insert({ans[i], i});
					}
				}
            }
        }
//        deb << endl;
        printf("%.10f ", ans[en]);
    }
    cout << '\n';
}

int main(){
	in("C-large.in");
	out("out.txt");
	int t;
	cin >> t;
	f(i, t) solve(i+1);
}
