#include <bits/stdc++.h>
#define ll long long

using namespace std;
ifstream fin("C:\\Users\\ASUS\\Desktop\\A-small-attempt1.in");
ofstream fout("C:\\Users\\ASUS\\Desktop\\A-small-attempt1.txt");
ll solve(string s, ll n, ll k,ll pos)
  { //cout<<s<<" "<<pos<<endl;
    ll flag=1;
    for(int i=0;i<n;i++)
      if (s[i]!='+')
       flag=0;
    if (flag)
      return 0;
    ll mn;
    ll ans=9999999999;
    for(int i=0;i<n-k+1;i++)
    { if (i>pos)
       { string a=s;
         for(int j=i;j<i+k;j++)
         if (s[j]=='-')
           a[j]='+';
         else
           a[j]='-';
        ll x=solve(a,n,k,i)+1;
        ans=min(ans,x);
        }
    }
    return ans;
  }


int main()
{
    ll  tc;
    fin>>tc;

    for(int w=1;w<=tc;w++){
    string s;
    ll k;
    fin>>s>>k;
   ll n;
    n=s.length();
    ll res=solve(s,n,k,-1);
    fout<<"Case #"<<w<<": ";
    if (res==9999999999)
      fout<<"IMPOSSIBLE"<<endl;
    else
      fout<<res<<endl;}
}
