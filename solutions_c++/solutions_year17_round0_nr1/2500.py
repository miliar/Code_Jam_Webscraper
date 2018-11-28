#include<bits/stdc++.h>
using namespace std;
#define sl(n) scanf("%lld",&n)
#define debug(n) printf("%lld\n",n)
typedef long long int ll;
//#define INPUT

int main(){
	#ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w", stdout);
   	#endif
   	ll z;sl(z);
   	for(ll t=1;t<=z;t++){
   		ll ans,k;
   		string s;cin>>s;
   		sl(k);
   		ll l = s.length(),i;
   		ll dp[l];
   		for(i=0;i<l;i++){
   			if(s[i]=='+')
   			dp[i]=1;
   			else
   			dp[i]=0;
   		}
   		ans=0;
   		ll flag=0,j;
   		for(i=0;i<l;i++){
   			if(dp[i]==0){
   				if(i+k>l){
   					flag=1;
   					break;
   				}
   				ans++;
   				for(j=i;j<i+k;j++)
   				dp[j]=dp[j]^1;
   			}
   		}
   		if(flag)
   		printf("Case #%lld: IMPOSSIBLE\n",t);
   		else
   		printf("Case #%lld: %lld\n",t,ans);
   	}
}
