#include <bits/stdc++.h>
#define fre freopen("input.in","r",stdin);freopen("output.in","w",stdout);
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
    fre
    int t;
    cin>>t;
    rep(test,1,t+1)
    {
        string s;
        cin>>s;
        int in=-1;
        rep(i,0,s.size()-1)
        {
            if(s[i]>s[i+1])
            {
                in = i;
                break;
            }
        }
        cout<<"Case #"<<test<<": ";
        if(in==-1)
        {
            cout<<s<<endl;
            continue;
        }
        while(in>=1 && s[in]==s[in-1])in--;
        if(s[in]=='1')
        {
            if(in>0)
            {
                s[in] = (char)(s[in]-1);
            }
            else
            {
                s.resize(s.size()-1);
                rep(i,0,s.size())s[i]='9';
            }
        }
        else
        {
            s[in] = (char)(s[in]-1);
            for(int i=in+1;i<s.size();i++)s[i]='9';
        }
        cout<<s<<endl;
    }
    return 0;

}
