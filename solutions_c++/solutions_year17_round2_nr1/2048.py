/// i am on fire
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <string.h>

using namespace std;

const int N=200005;
const int M=1005;

typedef long long ll;
typedef pair<ll,ll>ii;
typedef pair<int,ii>node;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

double pos[M],v[M],d;
int n;
double latest(){
 double mx=0.0;
 for(int i=0;i<n;i++){
    mx=max(mx,(d-pos[i])/(v[i]));
 }
 return mx;
}
bool ok(double speed,double mx){
 double t=d/speed;
 if(t-mx>0.00000000001)
    return 1;
 return 0;
}
int main(){

    freopen("test.in","r",stdin);
    freopen("A.out","w",stdout);;
    int t,c=1;
    scanf("%d",&t);
    while(t--){
        scanf("%lf%d",&d,&n);
        for(int i=0;i<n;i++){
            scanf("%lf%lf",&pos[i],&v[i]);
        }
          double low=0,high=1e16,mx=latest();
          for(int i=0;i<500;i++){
            double mid=(low+high)/2.0;
            if(ok(mid,mx))
                low=mid;
            else
                high=mid;
          }
        printf("Case #%d: %.6f\n",c++,low);

    }
    return 0;
}
