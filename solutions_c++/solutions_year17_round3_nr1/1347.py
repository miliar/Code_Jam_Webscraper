#include <bits/stdc++.h>
using namespace std;
const int MAXN=1005;
const long double PI=3.141592653589793238;
const long long INF=1e18;
int T,N,K,t;
long long ans,dp[MAXN][MAXN];
pair<long long,long long> vals[MAXN];
long long query(int curr,int left)
{
    if (left==0)return 0;
    if (curr==N)return -INF;
    long long &ans=dp[curr][left];
    if (ans!=-1)return ans;
    ans=max(query(curr+1,left),query(curr+1,left-1)+2*vals[curr].first*vals[curr].second);
    return ans;
}
int main()
{
    freopen("ample2.in","r",stdin);
    freopen("ample2.out","w",stdout);
    scanf("%i",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%i%i",&N,&K);
        for (int i=0;i<N;i++)scanf("%lli%lli",&vals[i].first,&vals[i].second);
        sort(vals,vals+N);
        reverse(vals,vals+N);
        ans=-INF;
        memset(dp,-1,sizeof(dp));
        for (int i=0;i<N;i++)
        {
            ans=max(ans,query(i+1,K-1)+vals[i].first*vals[i].first+2*vals[i].first*vals[i].second);
         }
        long double out = (long double)ans * PI;
        cout.setf(ios::fixed);
        cout.precision(10);
        cout<<"Case #"<<t<<": "<<out<<endl;
    }
}
