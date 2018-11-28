#include <bits/stdc++.h>
#define inf 1000000009LL
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
#define fe first
#define se second
#define MAX 100005
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    //ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    rep(test,1,t+1)
    {
        string s;
        int k;
        cin>>s>>k;
        int flag=1;
        int ans=0;
        rep(i,0,s.size())
        {
            if(s[i]=='-')
            {
                if(i+k-1>=s.size())
                {
                    flag=0;
                    break;
                }
                for(int j=i;j<=i+k-1;j++)
                {
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                }
                //cout<<s<<endl;
                ans++;
            }
        }
        //cout<<s<<endl;
        printf("Case #%d: ",test);
        if(flag==0)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;

}
