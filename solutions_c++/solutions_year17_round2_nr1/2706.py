#include <bits/stdc++.h>
#define inf 1000000000000000018LL
#define mod 1000000007
#define scano(x) scanf("%d",&x)
#define scanll(x) scanf("%lld",&x)
#define scant(x,y) scanf("%d%d",&x,&y)
#define pb push_back
#define mp make_pair
#define ll long long int
#define vi vector<int>
#define pii pair<int,int>
#define vpii vector< pii >
#define rep(i,a,b) for(int i=a;i<b;i++)
#define fre freopen("input.in","r",stdin);freopen("output.in","w",stdout);
#define fe first
#define se second
#define MAX 100005
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    fre
    int t;
    cin>>t;
    rep(tc,1,t+1)
    {
        double d;
        int n;
        cin>>d>>n;
        double ans = inf;
        rep(i,1,n+1)
        {
            double k,s;
            cin>>s>>k;
            double temp = d*k;
            temp = temp/(d-s);
            ans = min(ans,temp);
        }
        printf("Case #%d: %.6f\n",tc,ans);
    }
    return 0;

}
