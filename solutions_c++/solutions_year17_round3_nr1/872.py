#include<bits/stdc++.h>
using namespace std;
#define li long long int
#define ii pair<li,li>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define vi vector<li>
#define vii vector<ii>
#define INF 9999999999999
#define MAXN 100005
#define sz size()
#define ins insert


#define pi 3.14159265359
li n;
ii a[1005];
li dp[1005][1005][2];
li cal(li i,li k,bool f)
{
    if(i<0 || k==0) { return 0; }
    if(dp[i][k][f]!=-1) {  return dp[i][k][f]; }
    if(f)
    {
        return dp[i][k][f]=max(a[i].fi*a[i].fi+2*a[i].fi*a[i].se+cal(i-1,k-1,0),cal(i-1,k,1));
    }
    return dp[i][k][f]=max(2*a[i].fi*a[i].se+cal(i-1,k-1,0),cal(i-1,k,0));
}
int main()
{
    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    li testcases; //read(testcases);
    cin>>testcases;
    for(li testcase=1;testcase<=testcases;testcase++)
    {
        li k,i,j; cin>>(n); cin>>(k);
        for(i=0;i<n;i++) { cin>>(a[i].fi); cin>>(a[i].se); }
        for(i=0;i<=n;i++) for(j=0;j<=n;j++) dp[i][j][0]=dp[i][j][1]=-1;
        sort(a,a+n);
        double ans=(double)cal(n-1,k,1);
        cout<<"Case #"<<testcase<<": "<<setprecision(30)<<(double)pi*ans<<endl;
    }
    return 0;
}
