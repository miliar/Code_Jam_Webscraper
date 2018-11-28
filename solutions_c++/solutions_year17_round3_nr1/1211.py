//Template from Competitve Programming 3
#include <cstdio>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>

#define INF 1000000000
#define LOG_LEVEl 1
#define PB push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

long double doTc(vii p, int k);
long double height(ii x);
long double PI = 3.14159265358979323846264338327950;

bool myCompare(const ii &lhs, const ii &rhs);
void doTests();

int main(){
    int t; scanf("%d",&t);
    for (int i = 1; i<=t; i++){
        int n,k; scanf("%d %d",&n,&k);
        vii x;
        while(n--){
            int a,b; scanf("%d %d",&a,&b);
            x.PB(ii(a,b));
        }
        printf("Case #%d: %.9Lf\n",i,doTc(x,k));
    }
    return 0;
}

void doTests(){
    printf("Doing tests\n");
    vii x;
    x.PB(ii(9,3)); x.PB(ii(7,1)); x.PB(ii(10,1)); x.PB(ii(8,4));
    printf("%.9Lf\n",doTc(x,2));
}

long double doTc(vii p, int k){
    sort(p.begin(), p.end());
    reverse(p.begin(), p.end());
    long double best = -1;
    //printf("%lu %d\n",p.size(), k);
    for (int i = 0 ; i+k<=(int)p.size(); i++){
        //printf("%d\n",i);
        ii base = p[i];
        ///printf("base = %d %d\n",base.first,base.second);
        vii next; for (int j = i+1; j<(int)p.size(); j++) next.PB(p[j]);
        sort(next.begin(), next.end(), myCompare);
        reverse(next.begin(), next.end());

        long double answer = height(base) + (long double) base.first*
            (long double) base.first*PI;
        //printf("base answer is %.9Lf\n",answer);
        for (int j = 0; j+1<k; j++){
            //printf("Adding %.9Lf to ans\n",height(next[j]));
            answer+=height(next[j]);
        }
        best = max(best,answer);
        //printf("Bes");
    }
    //printf("Best answer is %.9Lf\n",best);
    /*
    if (k==1){
        double ans = -1;
        for (ii x:p){
            double new = (height(x)+x.first*x.first*PI;
            ans = max(ans,(height(x)+x.first*x.first*PI));
        }
        if (best+0.000001<ans || ans+0.000001<best){
            printf("Error mine %.9Lf given %.9Lf\n",best,ans);
        }
    }*/
    return best;
}

bool myCompare(const ii &lhs, const ii &rhs){
    return height(lhs)<height(rhs);
}

long double height(ii x){
    return PI * (long double) x.first * (long double) x.second * (long double) 2;
}
