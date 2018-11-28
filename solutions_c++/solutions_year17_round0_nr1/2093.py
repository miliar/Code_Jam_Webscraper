#include<bits/stdc++.h>
# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
  rf;
  wf;
  int t;
  cin>>t;
  string s;
  int k;
  int ans=0;
  for(int i=1;i<=t;i++)
  {
    cin>>s;cin>>k;
    ans=0;
    for(int j=0;j<=(s.length()-k);j++)
    {
      if(s[j]=='-'){
        ans++;
      //  cout<<" "<<j<<endl;
      
      for(int d=j;d<(j+k);d++)
      {
        
        if(s[d]=='-'){
          s[d]='+';
        }
        else{
          s[d]='-';
        }
      }
      }
    }
   // cout<<" SDASD "<<s<<endl;
    for(int j=0;j<s.length();j++)
    {
      if(s[j]=='-'){
      //  cout<<" "<<j<<" "<<s[j]<<endl;
        ans=-1;break;
      }
    }
    if(ans==-1){
      cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }
    else{
      cout<<"Case #"<<i<<": "<<ans<<endl;
    }
  }
  
}
