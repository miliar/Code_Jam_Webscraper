#include<bits/stdc++.h>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
typedef unsigned long long int  ull;
typedef long long int  ll;
#define FR freopen("input.txt", "r", stdin);
#define FW freopen("output.txt", "w", stdout);
#define SETPRES  std::setprecision(6),std::fixed;
#define pb push_back
#define mp make_pair
#define INF 10000000
#define mod 1000000007
#define all(x) x.begin(), x.end()
#define  Help_me  ios_base::sync_with_stdio(false);
template <class T1>
T1 GCD(T1 A,T1 B)
{
if(B==0)
return A;
else
return GCD(B,A%B);
}
template <class T2>
   T2 mulmod(T2 a,T2 b)  {T2 x=0,y=a%mod;while(b){
           if(b%2==1){x=(x+y)%mod;}
           y=(2*y)%mod;b=b/2;}return x%mod;}
template<class T3>
   T3 power(T3 a,T3 b){T3 x=1,y=a%mod;while(b){if(b%2==1){x=mulmod(x,y)%mod;}y=mulmod(y,y)%mod;b=b/2;}return x%mod;}
template<class T4>
bool cmp(T4 x,T4 y)
{
    return x>y?1:0;
}
vector<int> ns;
vector<int> digits;
bool solve(int idx,bool tight,int prev)
{
if(idx==digits.size())
    return false;
if(!tight)
{
    for(int i=idx;i<digits.size();i++)
    {
        ns.push_back(9);
    }
    return false;
}
  if(prev>digits[idx])
    return  true;
for(int i=digits[idx];i>=prev;i--)
{
    ns.push_back(i);
    if(solve(idx+1,tight&&digits[idx]==i,i))
    {
        ns.pop_back();
    }
    else
        return false;
}
return true;
}
int main()
{
Help_me
#ifndef ONLINE_JUDGE
    //string s="646";
    //stringstream(s)>>number;
    FR
  FW
    #endif
    int t;
    int tt;
    cin>>t;
    tt=1;
    while(t--)
    {
        ull num;
        cin>>num;
        while(num)
        {
            digits.push_back(num%10);
            num=num/10;
        }
        reverse(digits.begin(),digits.end());
        solve(0,true,0);
        bool flag=true;
cout<<"Case #"<<tt<<": ";
  int limit=0;
  if(ns[0]==0)
    limit=1;
        for(int i=limit;i<ns.size();i++)
{
cout<<ns[i];
  }
        cout<<endl;
        tt++;
digits.clear();
ns.clear();
    }
    return 0;

}
