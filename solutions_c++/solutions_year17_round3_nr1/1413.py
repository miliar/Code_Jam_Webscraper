#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<utility>
#include<set>
#include <queue>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
using namespace std;
ll r[1005];
ll h[1005];
double pi = 3.1415926535897932384626;
int main()
{
    freopen("inp.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    F(p,1,t+1){

        int n,k;
        cin>>n>>k;
        F(i,0,n){
            cin>>r[i]>>h[i];
        }

        double ans = 0;
        F(i,0,n){
            ll curr = r[i];
            vector<ll> v;
            F(j,0,n){
                if(j == i || r[j] > curr)continue;

                v.pb(r[j]*h[j]);
            }

            ll sum = curr*curr+2*r[i]*h[i];
            //cout<<i<<" "<<sum<<endl;
            sort(v.begin(),v.end());

            if(v.size()>=(k-1)){
                reverse(v.begin(),v.end());
                F(j,0,k-1){
                    sum+=2*v[j];
                    //cout<<i<<" "<<j<<" "<<sum<<endl;
                }
                ans = max(ans,sum*pi);
            }
        }
        printf("Case #%d: %0.8lf\n",p,ans);
        //cout<<"Case #"<<p<<": "<<ans<<endl;
    }
}

                



