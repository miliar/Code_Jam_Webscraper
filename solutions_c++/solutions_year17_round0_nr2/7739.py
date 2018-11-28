#include <bits/stdc++.h>
using namespace std;
char num[20];
long long int dp[20][10][2],n;
long long int ans(int in,int last,int eq)
{
    //cout<<in<<" "<<n<<" "<<last<<" "<<eq<<" "<<endl;
    if(in>=n)return 0;
    long long int ret = -999999999999990000;
    if(dp[in][last][eq]!=-1)return dp[in][last][eq];
    int hi = 9;
    if(num[in]-'0'<last && eq)return -999999999999990000;
    if(eq)hi = num[in] - '0';
    //cout<<hi<<endl;
    long long int pw  = 1;
    for(int i = 0;i<n-in-1;i++)pw *= 10;
    for(int i = last;i<=hi;i++)
    {
        ret = max(ret,(ans(in+1,i,(i==num[in]-'0' && eq))+ pw*i));
        //if(in==1)cout<<in<<" "<<i<<".."<<"    "<<eq<<"  "<<last<<"--"<<pw*i<<" "<<ret<<endl;
    }
    return dp[in][last][eq] = ret;

}
int main()
{
    //freopen("outbl.txt","w",stdout);
    int t,tc,l;

    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        memset(dp,-1,sizeof(dp));
        scanf("%s",num);
        n = strlen(num);
        //cout<<num<<" "<<n<<endl;
        printf("Case #%d: ",t);
        printf("%lld\n",ans(0,0,1));

    }
    return 0;
}
