#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
#define MODN 1000000007

vi r, q[105], f(105);
int main() {
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);

    ll i, j, n, p, ii, t, inp, x;
	s(t);
	for( ii = 1 ; ii <= t ; ii++ )
	{
		s(n); s(p);
		r.clear();
		for( i = 0; i < n; i++ ){
			s(inp);
			r.pb(inp);
		}
		
		for( i = 0; i < n; i++ ){
			q[i].clear();
				for( j = 0; j < p; j++ ){
					s(x);
					q[i].pb(x);
				}
			sort(q[i].begin(), q[i].end());
            f[i] = 0;
		}
		ll ans = 0, mxf = 0, mult = 1, curVal, mxVal, mnVal, flag;

        while(mxf < p && mult < 1000005) {
            flag = 1;
            for(i = 0; i < n; i++) {
                curVal = r[i] * mult;
                mxVal = (curVal * 110)/100;
                mnVal = ceil(((double)(curVal*90))/100.0);

                while(q[i][f[i]] < mnVal && f[i] < p) f[i]++;
                if(!(f[i] < p && q[i][f[i]] >= mnVal && q[i][f[i]] <= mxVal)) flag = 0;
                mxf = max(mxf, f[i]);
            }
			if(!flag) mult++;
            else{
                for(i = 0; i < n; i++) {
                    f[i]++;
                    mxf = max(mxf, f[i]);
                }
                ans++;
            }
        }
		cout << "Case #" << ii << ": " << ans << endl;
	}
    return 0;
}
