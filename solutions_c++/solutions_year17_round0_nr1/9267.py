#include<bits/stdc++.h>
#define MX 100005
#define M 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long
#define SF(x) scanf("%d",&x)
#define DBG cout<<"Chk("<<++TM<<")\n"
#define FOR(_i,_n) for(int _i=0;_i<_n;_i++)
#define ALL(typ) typ.begin(),typ.end()
#define SZ(ar,T) sizeof(ar)/sizeof(T)
#define PII pair<int,int>
#define READ(tag) freopen(tag,"r",stdin)
#define RITE(tag) freopen(tag,"w",stdout)
#define INF 9223372036854775807
using namespace std; int TM;

void sol()
{
  string str; cin>>str;
  int lim,ans=0; cin>>lim;

  FOR(i,str.length())
  {
    if(str[i]=='-')
    {
      for(int k=i;k<i+lim;k++)
      {
        if(k>=str.length())
        {
          cout<<"IMPOSSIBLE";
          return;
        }
        if(str[k]=='-') str[k]='+';
        else str[k]='-';
      }
      ans++;
    }
  }
  cout<<ans;
}
int main()
{
  //READ("inA.txt");
  //RITE("outA.txt");

  int tc; cin>>tc;
  FOR(i,tc)
  {
    cout<<"Case #"<<i+1<<": ";
    sol(); cout<<"\n";
  }
}
