#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define sz size()
#define pii pair<int,int>
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(),(v).end()

ll A[55][55];
ll R[55];
std::vector< pair<ll,ll> > v[55];

bool chk(ll a,ll b)
{
	ll lo = 90LL*b,hi = 110LL*b;
	a *= 100LL;

	return ( (a <= hi) && (a >= lo) );
}

bool ok(pii a,pii b)
{
	return max(a.ff,b.ff) <= min(a.ss,b.ss);
}

int taken[55];

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);
	
	int t;
	int N,P;

	cin >> t;

	for(int cases =1;cases <= t;cases++){

		cin >> N >> P;

		memset(taken,0,sizeof taken);

		for(int i = 0;i < N;i++)cin >> R[i];

		for(int i = 0;i < N;i++){

			for(int j = 0;j < P;j++)cin >> A[i][j];
		}

		cout << "Case " << "#" << cases << ": ";

		for(int i = 0;i < N;i++){

			for(int j = 0;j < P;j++){

				int mn = 1000001LL,mx = 0;

				for(int k = 1;k <= 1000000LL;k++){

					if( chk(A[i][j],R[i]*k) ){

						mn = min(mn,k);
						mx = k;
					}
					else if(mx)break;
				}
				//cout << i <<' '<< j << ' '<<mn << ' ' << mx << endl;
				v[i].pb(mp(mn,mx));
			}
			sort(all(v[i]));
		}
		int ans = 0;

		if(N == 1){

			for(int i = 0;i< P;i++){

				if(v[0][i].ff <= v[0][i].ss){

					ans++;
				}
			}
			cout << ans << endl;
		}
		else if(N == 2){

			for(int i = 0;i < P;i++){

				for(int j = 0;j < P;j++){

					if(taken[j])continue;

					if(ok(v[0][i],v[1][j])){

						taken[j] = 1;
						ans++;
					}
				}
			}
			cout << ans << endl;
		}
		for(int i = 0;i<N;i++)v[i].clear();

		/*for(int i = 0;i < P;i++){

			int mn = v[0][i].ff,mx = v[0][i].ss;

			for(int j = 1;j < N;j++){

				for(int k = 0;k < P;k++){

					if(taken[j][k])continue;

					mn = max(mn,v[j][k].ff);
					mx = min(mx,v[j][k].ss);

					if(mn <= mx){

						cur.pb(j);
					}
				}
			}
		}*/

	}

	return 0;
}