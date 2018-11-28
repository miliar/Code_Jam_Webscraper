#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;

const ll INF= ll (1e18);
const int MOD= 1e9+7;

int main()
{
  int t;
  cin>>t;
  int n=1;
  //freopen("input.in","r",stdin);
//freopen("output_file_name.out","w",stdout);
  while(t--)
  {
      ll num;
      vector<ll> v;
      cin>>num;
      int mainflag=0;
      if(num<10)
      {
          mainflag=1;
      }
      for(ll i=num;i>=0;i--)
      {
          int flag=0;
          int k=0;
          v.clear();
          ll t=i;
          //cout<<t<<endl;
          while(t>0)
          {

             v.pb(t%10);
             t=t/10;


          }
          for(int j=0;j<v.size()-1;j++)
          {
              //cout<<v[j]<<" ";
              //cout<<endl;
              if(v[j]<v[j+1])
              {
                  flag=1;
                  break;
              }
          }
          if (flag==0)
            break;
      }
      if(mainflag==1)
      {
           cout<<"Case#"<<n<<": "<<num;
      }
      else
      {
          sort(v.begin(),v.end());
      cout<<"Case#"<<n<<": ";
      for(int i=0;i<v.size();i++)
        cout<<v[i];
      }


        n++;
        cout<<endl;
  }




    return 0;

}
