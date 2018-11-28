#include "iostream"
#include "cstdio"
#include "cstring"
#include "string"
#include "algorithm"
#include "cmath"
#include "vector"
#include "queue"
#include "map"
#include "set"
#include "stack"
using namespace std;
const int maxn = 10;
const int inf = 0x3f3f3f3f;
typedef pair<long long,int> Node;
Node num[maxn];
int main(){
	int T;
	freopen("A-small-attempt0.in.txt", "r", stdin);  
    freopen("outa1.txt", "w", stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        long long dist;
        int n;
        cin>>dist>>n;
        for(int i = 1;i <= n;++ i){
        	cin>>num[i].first>>num[i].second;
        }
        double res= 0;
        for(int i = 1;i <= n;++ i){
            double ans = 1.0*(dist-num[i].first)/num[i].second;
            res = max(ans,res);
        }
        printf("Case #%d: ",cas);
        printf("%.6lf\n",dist/res);
    }
    return 0;
}