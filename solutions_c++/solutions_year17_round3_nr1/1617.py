#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <queue>
#include <math.h>
#include <set>
#include <map>
#include <climits>
#include <stack>
#define INF 0x3f3f3f3f
#define debug(x) printf("%d\n",x)
#define gcd(a,b) __gcd(a,b)
#define mem(a,x) memset(a,x,sizeof(a))
#define mp make_pair
#define pb push_back
const double PI  =3.141592653589793238463;
using namespace std;
typedef long long ll;
int __,_;
vector<pair<int, int> > pancakes;
int main()
{
    freopen("/Users/zhou_rui/Desktop/A-large.in.txt", "r", stdin);
    freopen("/Users/zhou_rui/Desktop/testttt.txt", "w", stdout);
    scanf("%d",&__);
    for(_= 1;_<=__;_++){
        pancakes.clear();
        int n,k;
        scanf("%d %d",&n,&k);
        for(int i = 0;i<n;i++){
            int r,h;
            scanf("%d %d",&r,&h);
            pancakes.pb(mp(r,h));
        }
        double best = 0;
        for(int i = 0;i<n;i++){
            priority_queue<double>  contrib;
            int btr = pancakes[i].first;
            for(int j = 0;j<n;j++){
                if(pancakes[j].first<=btr&&j!=i){
                    contrib.push(PI*2.0*pancakes[j].first*pancakes[j].second);
                }
            }
            if(contrib.size()<k-1)continue;
            double tota = PI*btr*btr+PI*2.0*pancakes[i].first*pancakes[i].second;
            int counted = 0;
            while(counted<k-1&&!contrib.empty()){
                tota += contrib.top();
                counted++;
                contrib.pop();
            }
            if(tota>best){
                best = tota;
            }
            
        }
        printf("Case #%d: %.7lf\n",_,best);
    }
    
    return 0;
}

