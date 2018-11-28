#include<bits/stdc++.h>
#include <stdio.h>

using namespace std;

#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<char,long long >

#define all(c) (c).begin(), (c).end()
#define REP(i,n) for(__typeof(n) i = 0; i < n; i++)
#define REP1(i,n) for(__typeof(n) i = 1; i <= n; i++)
void fun(){
    double d;
    long int n;
    cin>>d>>n;
    double c=0;
    REP(i, n){
        double distance,ss;
        cin>>distance>>ss;
        c=max(c,(d-distance)/ss);
    }
    double aaaa=d/c;
    cout<<fixed<<setprecision(12)<<aaaa;
}
int main()
{

  freopen("E:\\input.txt", "r", stdin);
  freopen("E:\\output.txt", "w", stdout);

    int t=1;
    cin>>t;
    REP1(i, t)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    return 0;
}
