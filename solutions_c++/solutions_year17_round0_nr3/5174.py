#include <bits/stdc++.h>
#define test int t; cin >> t;while(t--)
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%lld",&n)

typedef long long ll;

using namespace std;

map <ll,ll> M;


int main(){

	freopen("C-large(1).in","r",stdin);
	freopen("A3.out","w",stdout);
	int z=1;
	test{
		printf("Case #%d: ",z++);
		M.clear();

		ll n,k; sld(n);sld(k);


		M[n]=1;

		map <ll,ll> :: iterator it;



		ll loop=0,ans1=0,ans2=0;

		while(loop<k){
			it=M.end();
			it--;

			ll tot=(*it).second;
			ll y=(*it).first;
			if(y==1 || y==0){
				ans1=0; ans2=0;break;
			}
			else if(y==2){
				ans2=0;
			}


			if(y%2==0){
				ll k1=y/2;
				ll k2=y/2-1;

				if(k1>0){
					M[k1]+=tot;
					ans1=k1;
				}
				if(k2>0){
					M[k2]+=tot;
					ans2=k2;
				}
			}
			else{
				ll k1=y/2,k2=y/2;
				if(k1>0){
					M[k1]+=tot; M[k2]+=tot;

					ans1=k1; ans2=k2;
				}
			}
			M.erase(y);
			loop+=tot;
		}
	cout << ans1 << " " << ans2 << endl;
	}
}
