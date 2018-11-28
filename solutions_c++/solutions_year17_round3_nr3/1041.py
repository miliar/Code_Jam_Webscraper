//Template from Competitve Programming 3
#include <cstdio>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

#define INF 1000000000
#define LOG_LEVEl 0
#define PB push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long double ld;

ld tc(vector<ld> x, ld u);
ld min(ld a, ld b){
    if (a>b) return b;
    return a;
}
void runTests();

int main(){
    if (LOG_LEVEl>0) runTests();

    int T; scanf("%d", &T);
    for (int i = 1; i<=T; i++){
        int N,K; scanf("%d %d",&N,&K);
        ld u; scanf("%Lf",&u);
        vector<ld> x; while(N--){
            ld t; scanf("%Lf",&t);
            x.PB(t);
        }
        printf("Case #%d: %.74Lf\n",i,tc(x,u));

    }
    return 0;
}

void runTests(){
    printf("Running tests\n");
    vector<ld> x; x.PB(0.5000);x.PB(0.7000);x.PB(0.8000);x.PB(0.6000);
    ld u = 1.4000;
    ld a1 = tc(x,u);
    printf("x = %Lf\n",a1);
    assert (a1+0.000001>1.000000 &&a1-0.00001<1.00000);
    printf("Test 1 passed\n");
    x.clear(); x.PB(0.0000); x.PB(0.0000);
    u = 1;
    a1 = tc(x,u);
    assert (a1+0.000001>0.25 && a1-0.000001<0.25);
    printf("Test 2 passed\n");
    x.clear(); x.PB(0.4); x.PB(0.6); u = 0.1; a1=tc(x,u);
    printf("x %Lf\n",a1);
    assert(a1+0.000001>0.3 && a1-0.000001<0.3);
    printf("Test 3 passed\n");
    x.clear(); x.PB(0); x.PB(0); x.PB(0); x.PB(1); u = 2; a1=tc(x,u);
    printf("x %Lf\n",a1);
    assert(a1+0.000001>0.296296296296296296 && a1-0.000001<0.296296296296296296);
    printf("Test 4 passed\n");
}

ld tc(vector<ld> x, ld u){
    ld s = (ld) x.size();
    if (s==1) return min(1.0000,x[0]+u);

    priority_queue<ld, vector<ld>, greater<ld> > pq; for (ld j:x) pq.push(j);
    bool perfectCase = false;

    while (!perfectCase && u-(ld)0.00000001>0){
        if (LOG_LEVEl) printf("U = %Lf\n",u);

        vector<ld> j;
        j.PB(pq.top()); pq.pop();

        while (!pq.empty() && pq.top()==j[0]){
            j.PB(pq.top()); pq.pop();
        }
        if (LOG_LEVEl) for (ld i:j) printf("J %Lf\n",i);

        if (pq.empty()){
            ld p = min(j[0]+u/s,(ld)1);
            if (LOG_LEVEl)printf("Pq is empty %ld %Lf %Lf\n",j.size(),p,s);
            ld toReturn = pow(p,s);
            if (LOG_LEVEl)printf("Returnign %Lf\n",toReturn);
            return toReturn;
        }

        ld difference = pq.top()-j[0];
        if (LOG_LEVEl) printf("Difference %Lf\n",difference);
        if (difference*s>=u){
            for (int i = 0; i<(int)j.size(); i++){
                j[i]+=u/(ld)j.size();
            }
            u = 0;
        } else{
            for (int i = 0; i<(int)j.size(); i++){
                ld newj = j[i]+difference;
                j[i]=min(newj,(ld)1);
                u-=difference;
            }
        }
        for (ld i:j) pq.push(i);
    }

    ld ans = 1;
    while (!pq.empty()){
        ans*=pq.top();
        if (LOG_LEVEl) printf("Ans*=%Lf\n",pq.top());
        pq.pop();
    }
    if (LOG_LEVEl) printf("Returning %Lf\n",ans);
    return ans;
}
