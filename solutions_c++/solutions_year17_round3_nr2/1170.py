#include<bits/stdc++.h>

using namespace std;

#define ll 							long long
#define mp make_pair
#define fi first
#define se second
#define PI 		3.1415926535897932384626
#define pb push_back
ll t,i,j,ans,r,c,R,C,m,n,k,u,v;

ll w[1500],dp[1500][730][2],s[10010],start;
ll p,a,b,x,y;

 ll ff(ll i,ll secondd,ll p)
 {
     if(dp[i][secondd][p]!=-1)
     return dp[i][secondd][p];
     if(i==1440)
     {
         if(secondd!=720)
         {
             return 5000;
         }
         if(p!=start)
         {
             return 1;
         }
         else
         {
             return 0;
         }
     }
     if(secondd>720)
     {
         return 50000;
     }
     if(i-secondd>720)
     {
         return 50000;
     }
    if(s[i]==0)
    {
        if(p==0)
            dp[i][secondd][p]= ff(i+1,secondd+1,p);
        else
            dp[i][secondd][p]= 1+ff(i+1,secondd+1,1-p);
        return dp[i][secondd][p];
    }
    if(s[i]==1)
    {
        if(p==0)
            dp[i][secondd][p]= 1+ff(i+1,secondd,1-p);
        else
            dp[i][secondd][p]= ff(i+1,secondd,p);
        return dp[i][secondd][p];
    }
    if(p==0)
    {
        dp[i][secondd][p]= min(ff(i+1,secondd+1,p),1+ff(i+1,secondd,1-p));
        return dp[i][secondd][p];
    }
    else
    {
        dp[i][secondd][p]= min(ff(i+1,secondd,p),1+ff(i+1,secondd+1,1-p));
        return dp[i][secondd][p];
    }

 }


int main(){
    freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);	cin>>t;
	for(u=1;u<=t;u++){

		cin>>n>>m;
        memset(s,-1,sizeof(s));
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            for(j=x;j<y;j++)
            {
                s[j]=1;
                w[j]=y;
            }
        }
        for(i=0;i<m;i++)
        {
            cin>>x>>y;
            for(j=x;j<y;j++)
            {
                s[j]=0;
                w[j]=y;

            }
        }
        start=0;
        memset(dp,-1,sizeof(dp));
        ll res=ff(0,0,0);
        start=1;
        memset(dp,-1,sizeof(dp));
         res=min(ff(0,0,1),res);
		cout<<"Case #"<<u<<": "<<res<<endl;
	}
	return 0;
}
