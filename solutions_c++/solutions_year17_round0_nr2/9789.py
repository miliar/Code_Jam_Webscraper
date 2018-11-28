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
  string str,ans="";
  cin>>str;

  bool zero=false;
  FOR(i,str.length())
  {
    if(str[i]=='0') zero=true;
  }
  if(false)
  {
    FOR(i,str.length()-1) ans+='9';
  }
  else
  {
    bool got=false;
    FOR(i,str.length())
    {
      if(got)
      {
        ans+='9';
        continue;
      }

      /*char lo='9';
      for(int k=i+1;k<str.length();k++)
      {
        if(str[k]<lo) lo=str[k];
      }

      if(str[i]>lo)
      {
        ans+=str[i]-1;
        got=true;
      }
      else ans+=str[i];
      */
      if(i==(str.length()-1))
      {
        ans+=str[i];
        continue;
      }
      if(str[i]<str[i+1]) ans+=str[i];
      else if(str[i]==str[i+1])
      {
        char lo='9';
        for(int k=i+1;k<str.length();k++)
        {
          if(str[k]<lo) lo=str[k];
        }
        if(lo<str[i])
        {
          if(str[i]!='1') ans+=str[i]-1;
          got=true;
        }
        else ans+=str[i];
      }
      else
      {
        if(str[i]!='1') ans+=str[i]-1;
        got=true;
      }
    }
  }
  //cout<<str<<" => ";
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
