#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define f(i,st,en)for(int i=st;i<en;i++)
#define fi(i,st,en)for(int i=st;i<=en;i++)
typedef vector<int>vi;
typedef long long int ll;
ll conv(string str)
{
  stringstream ss(str);
  ll i;
  ss >> i;
  return i;
}
string str;
int k;
int main()
{
   freopen("in_large","r",stdin);
   freopen("out_large","w",stdout);


    int t;
    ll n;
    scanf("%d",&t);

    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
      long long int ans=0;
      cin>>str;
      cin>>k;
     // cout<<str<<" "<<k<<endl;
      for(int i=0;i<str.size();i++){
            //cout<<str<<endl;
            if(str[i]=='-'){
                ans++;

                if((i+k)<=str.size())
                for(int j=i;j<(i+k)&&j<str.size();j++){
                       //  cout<<j<<endl;
                        if(str[j]=='+')
                             str[j]='-';
                        else
                             str[j]='+';
                }
            }
      }
      bool flag=false;
      for(int i=0;i<str.size();i++)
            if(str[i]=='-'){flag=true;break;}
      if(!flag)
      cout<<ans<<endl;
      else
      cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
