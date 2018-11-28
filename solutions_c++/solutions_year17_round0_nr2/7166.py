#include<bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// #include <ext/pb_ds/detail/standard_policies.hpp>
// using namespace __gnu_pbds;
using namespace std;
#define ll long long
#define mset(m,v) memset(m,v,sizeof(m))
#define pr(a,s) printf("Case #%lld: %lld\n",a,s)
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define scan(a) scanf("%d",&a)
#define scanl(a) scanf("%lld",&a)
#define all(x) x.begin(),x.end()
#define se second
#define fi first
#define pi 3.14159265358979323
#define print(ans) printf("Case #%d: ",ans)
 
// template <typename T>
// using ordered_set = tree<T, null_type, less<T>, rb_tree_tag,
//     tree_order_statistics_node_update>;

const ll inf = 1e17;
const int MAXM = 1e3+5;
const int MAXN = 1e6+4;

vector<int> v;

int main()
{
	ll t,n,i,j,k;
	scanl(t);
	for(int x=1;x<=t;x++)
	{
		v.clear();
		scanl(n);
		while(n){
			v.pb(n%10);
			n/=10;
		}
		reverse(all(v));
		while(1){
			int f=0;
			for(i=1;i<(int)v.size();i++){
				if(v[i]<v[i-1])	f=1;
			}
			if(f==0){
				break;
			}
			f=0;
			int sz = (int)v.size();
			for(i=sz-1;i>=1;i--){
				if(v[i]<v[i-1]){
					f=1;
					v[i-1]--;
					break;
				}
			}
			if(f)	
			for(j=i;j<sz;j++){
				v[j]=9;
			}
		}
		int f=0;
		printf("Case #%d: ",x);
		for(i=0;i<(int)v.size();i++){
			if(v[i]==0 and f==0)	continue;
			printf("%d",v[i]);
			f=1;
		}
		printf("\n");
	}
	return 0;
}