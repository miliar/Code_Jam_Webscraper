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

int main()
{
	string s;
	int t,i,j,k;
	scan(t);
	for(int x=1;x<=t;x++){
		int cn=0;
		cin>>s>>k;
		for(i=0;i<s.length()+1-k;i++){
			if(s[i]=='-'){
				cn++;
				for(j=i;j<i+k;j++){
					if(s[j]=='-')	s[j]='+';
					else	s[j]='-';
				}
			}
		}
		int f=0;
		for(i=0;i<s.length();i++){
			if(s[i]=='-'){
				f=1;
				printf("Case #%d: IMPOSSIBLE\n",x);
				break;
			}
		}
		if(f)	continue;
		printf("Case #%d: %d",x,cn);
		printf("\n");
	}
	return 0;
}