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
#define MEM(a,x) memset(a,x,sizeof(a))
#define MP make_pair
using namespace std;
typedef long long ll;
int t;
vector<pair<int, int>> horses;
int main()
{
    freopen("/Users/zhou_rui/Desktop/A-large.in.txt", "r", stdin);
    freopen("/Users/zhou_rui/Desktop/outtotest.txt","w",stdout);
    scanf("%d",&t);
    for(int test= 1;test<=t;test++){
        int d,n;
        horses.clear();
        scanf("%d %d",&d,&n);
        for(int i = 0;i<n;i++){
            int p,v;
            scanf("%d%d",&p,&v);
            horses.push_back(make_pair(p, v));
        }
        double maxt=0;
        for(int i = 0;i<n;i++){
            if(horses[i].first<d){
                double ttt = ((double)d-horses[i].first)/(double)horses[i].second;
                if(ttt>maxt){
                    maxt=ttt;
                }
            }
        }
        printf("Case #%d: %lf\n",test,(double)d/maxt);
    }
    return 0;
}

