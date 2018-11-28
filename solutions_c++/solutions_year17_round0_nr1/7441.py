#include<bits/stdc++.h>
using namespace std;
#define INPUT
int main()
{
	#ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w", stdout);
   	#endif
   	long long z,t;
   	cin>>z;
   	for(t=1;t<=z;t++){
   		long long ans,k;
   		string s;
   		cin>>s;
   		cin>>k;
   		long long l = s.length(),i;
   		long long dp[l];
   		for(i=0;i<l;i++)
        {
   			if(s[i]=='+')
   			dp[i]=1;
   			else
   			dp[i]=0;
   		}
   		ans=0;
   		long long flag=0,j;
   		for(i=0;i<l;i++)
   		{
   			if(dp[i]==0)
   			{
   				if(i+k>l)
   				{
   					flag=1;
   					break;
   				}
   				ans++;
   				for(j=i;j<i+k;j++)
                    dp[j]=dp[j]^1;
   			}
   		}
   		if(flag)
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
   		else
            cout<<"Case #"<<t<<": "<<ans<<endl;
   	}
   	return 0;
}
