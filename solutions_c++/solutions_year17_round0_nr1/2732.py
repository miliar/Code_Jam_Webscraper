#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000005
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define all(xx) xx.begin(),xx.end()
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,sizeof(x))
#define INF 1e18
#define PI acos(-1)
#define ll long long
#define endl "\n"


int main() {
    hg;
    //freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);
    int t,tt=1;
    int i,j,k;
    int f=0;
    string s,ss;
    int cnt,ans,tc;
    int l;
    cin>>t;
    while(t--){
    cin>>s;
    ss=s;
    cin>>k;
    cnt=0;ans=0;f=0;
    l=s.size();
    for(i=0;i<l;i++)
    {
      if(s[i]=='-' && i+k<=l)
      {
        tc=0;
        cnt++;
        for(j=i;j<l;j++)
        {
          if(s[j]=='+')
            s[j]='-';
          else
            s[j]='+';
          tc++;
          if(tc==k)
            break;
        }
        
      }
    }
    for(i=l-1;i>=0;i--)
    {
      if(ss[i]=='-' && i-k+1>=0)
      {
        ans++;
        tc=0;
        for(j=i;j>=0;j--)
        {
          if(ss[j]=='+')
            ss[j]='-';
          else
            ss[j]='+';
           tc++;
          if(tc==k)
            break;
        }
       
      }
    }
    ans=min(ans,cnt);
    for(i=0;i<l;i++){
      if(s[i]=='-'){
        f=1;
        break;
      }
    }
    cout<<"Case #"<<tt<<": ";
    if(f)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<ans<<"\n";
    tt++;
  }
    
    return 0;
}