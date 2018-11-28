#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(;c<'0'||c>'9';c=getchar())if(c=='-')sign=-1;
    for(num=0;c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests;
    cin>>tests;

    for(int cases=1;cases<=tests;cases++)
    {
        string S;
        int n,ans=0;
        cin>>S>>n;

        for(int i=0;i<=S.length()-n;i++)
        {
            if(S[i]=='-')
            {
                ans++;
                for(int j=0;j<n;j++)S[i+j]=('-'+'+'-S[i+j]);
            }
        }
        for(int i=0;i<S.length();i++)if(S[i]=='-')ans=-1;

        if(ans==-1)cout<<"Case #"<<cases<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<cases<<": "<<ans<<"\n";
    }
}
