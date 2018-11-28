#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         INT_MAX
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,n,i;
    pair<double,double> A[1005];
    double d,maxi;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>d>>n;
        maxi=0;
        for(i=0;i<n;i++)
        {
            cin>>A[i].F>>A[i].S;
            maxi=max(maxi,(d-A[i].F)/A[i].S);
        }
        cout<<"Case #"<<t<<": ";
        cout<<fixed<<setprecision(8)<<d/maxi<<endl;
    }
    return 0;
}
