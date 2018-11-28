#include<bits/stdc++.h>
using namespace std;

#define fre freopen("in.txt","r",stdin)
#define ll long long
#define abs(x) ((x)>0?(x):-(x))
#define mod 1000000007
#define scand(x) scanf("%d",&x);
#define scanlld(x) scanf("%I64d",&x);
#define scans(x) scanf("%s",x);
#define printd(x) printf("%d",x);
#define printlld(x) printf("%I64d",x);
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define inf (1<<30)
#define forup(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int,int>
#define boost ios_base::sync_with_stdio(0)
#define MAXN 1000003
ll a[MAXN];
int main()
{
  boost;
  freopen("in.txt","r",stdin);  freopen("out.txt","w",stdout);
  int t;
  cin>>t;
  forup(tt,1,t+1)
  {
    cout<<"Case #"<<tt<<": ";
    string s;
    int n,k,ans=0,f=0;
    cin>>s>>k;
    n=s.size();
    s=' '+s;
    // forup(i,2,k+1)
    //   if(s[i]!=s[1]){f=1;break;}
    // if(s[1]=='-')ans++;
    forup(i,1,n-k+1)
    {
      if(s[i]=='-')
      {
        for(int j=0,p=i;j<k;j++,p++)
          if(s[p]=='-')s[p]='+';
          else s[p]='-';
        ans++;
      }
    }
    forup(i,n-k+1,n+1)
      if(s[i]!=s[n-k+1]){f=1;break;}
    if(s[n-k+1]=='-')ans++;
    if(f)cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
  }
  return 0;
}

