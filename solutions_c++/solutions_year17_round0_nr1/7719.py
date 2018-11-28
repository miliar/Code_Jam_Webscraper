#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair < int , int > pii ;

void solve()
{
    string S;
    int K , i ;
    int ans=0;
    cin>>S>>K;
    for(i=0;i+K-1<S.length();++i)
    {
        if(S[i]=='-')
        {
            for(int j=i;j<=i+K-1;++j)
            {
              if(S[j]=='-')S[j]='+';
              else S[j]='-';
            }
            ++ans;
        }
    }
    int f=1;
    for(int i=0;i<S.length();++i)if(S[i]=='-')f=0;
    if(!f)cout<<"IMPOSSIBLE";
    else cout<<ans;
}
int main()
{
//////    ini();
    freopen("in.in","r+",stdin);
    freopen("1.txt","w+",stdout);
    int T , i ;
    cin>>T;
    cin.ignore();
    for(i=1;i<=T;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
    return 0;
}
