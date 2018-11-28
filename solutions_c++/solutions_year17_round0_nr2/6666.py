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
int check(int x)
{
  string ss=to_string(x);
  int f=0;
  forup(i,1,ss.size())
    if(ss[i]<ss[i-1]){f=1;break;}
  return f^1;
}
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
    int loc=0;
    cin>>s;
    forup(i,1,s.size())
      if(s[i]<s[i-1]){loc=i;break;}
    if(!loc)cout<<s<<endl;
    else
    {
      int pp=loc-1;
      if(s[pp]=='1')
      {
        while(pp-1>=0 && s[pp]==s[pp-1])pp--;
        //cout<<pp<<"@#$%^&*";
        if(pp)
        {
          forup(i,pp,loc)
            s[i]='0';
          forup(i,loc,s.size())s[i]='9';
        }
        else
        {
          string temp="";
          forup(i,1,s.size())temp+='9';
          s=temp;
        }
      }
      else
      {
        while(pp-1>=0 && s[pp]==s[pp-1])pp--;
        //cout<<pp<<"@#$%^&*";
        
        int p=(int)(s[pp]);
        s[pp]=(char)(p-1);
        forup(i,pp+1,s.size())s[i]='9';
    }
      
      cout<<stol(s)<<endl;
    }
    // int n;
    // cin>>n;
    // while(1)
    // {
    //   if(check(n)){cout<<n<<endl;break;}
    //   n--;
    // }
  }  
  return 0;
}

