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
tt=1;
cin>>t;
while(t--)
{
    int  n,k;
    cin>>n>>k;
    priority_queue<int> heaps;
    heaps.push(n);
    for(int i=1;i<=k-1;i++)
    {
        int temp=heaps.top();
        heaps.pop();
        if(temp==1)
            break;
        if(temp%2==0)
        {
            heaps.push(temp/2);
            heaps.push((temp/2)-1);
        }
        else
        {
 heaps.push(temp/2);
  heaps.push(temp/2);
        }
    }

      int temp=heaps.top();
   cout<<"Case #"<<tt<<": ";
        if(temp%2==0)
        {
        cout<<temp/2<<" "<<(temp/2)-1;
        }
        else
        {
   cout<<temp/2<<" "<<(temp/2);
 }
 cout<<endl;
    tt++;
}

    return 0;

}
