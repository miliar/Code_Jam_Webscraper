#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define pii pair <int, int>
#define pll pair <ll,ll>
using namespace std;
const int ma = 1e5+5;
int main()
{
  //freopen("i2.txt","r",stdin);
  //freopen("o.txt","w",stdout);
  int t;
  cin>>t;
  for(int p=1;p<=t;p++)
  {
    string st;
    cin>>st;
    if(st.length()==1)
      cout<<"Case #"<<p<<": "<<st<<endl;
    else
    {
      int i;
      string ans="";
      for(i=0;i<st.length()-1;i++)
      {
        if(st[i] > st[i+1])
        {
          break;
        }
      }
      if(i==st.length()-1)
        cout<<"Case #"<<p<<": "<<st<<endl;
      else
      {
        if(st[i]=='1')
        {
          int tp=i;
          while(tp>=0 and st[tp]=='1')
          {
            tp--;
          }
          if(tp>=0) 
          {
            int tp1=tp;
            char ch = st[tp];
            while(tp1>=0 and st[tp1]==ch)
            {
              tp1--;              
            }
            for(int j=0;j<=tp1;j++)
            ans+=st[j];
            ans+=(--st[tp1+1]);
            for(int j=tp1+2;j<st.length();j++)
              ans+='9';
          }
          else //all ones and 0
          {
            for(int j=0;j<st.length()-1;j++)
              ans+='9';
          }

        }
        else
        {
            int tp1=i;
            char ch = st[i];
            while(tp1>=0 and st[tp1]==ch)
            {
              tp1--;              
            }
            for(int j=0;j<=tp1;j++)
            ans+=st[j];
            ans+=(--st[tp1+1]);
            for(int j=tp1+2;j<st.length();j++)
              ans+='9';
        }
        cout<<"Case #"<<p<<": "<<ans<<endl;
      }

    }
  }
  return 0;
}