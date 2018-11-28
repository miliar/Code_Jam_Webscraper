#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define pdd pair<double,double>
#define pdi pair<double,int>
#define F first
#define S second
#define mp make_pair
#define INF 1e15

using namespace std;

int T;
double D;
int N;
pdd horse[1005];
vector<pdi> hull;

double intersection(pdd p1, pdd p2){
    return (p2.S-p1.S)/(p1.F-p2.F);
}

int main(){
    freopen("data3.in","r",stdin);
    freopen("data3.out","w",stdout);
    scanf("%d",&T);
    for (int z = 1; z <= T; z++){
        hull.clear();
        scanf("%lf%d",&D,&N);
        for (int i = 0; i < N; i++) scanf("%lf%lf",&horse[i].S,&horse[i].F);
        sort(horse,horse+N);
        for (int i = 0; i < N; i++){
            while(hull.size() >= 2){
                pdi t1 = *(hull.end()-1), t2 = *(hull.end()-2);
                if (intersection(horse[i],horse[t2.S]) <= t1.F)
                    hull.pop_back();
                else break;
            }
            if (hull.empty()) hull.push_back(mp(-INF,i));
            else{
                int o = hull.back().S;
                hull.push_back(mp(intersection(horse[i],horse[o]),i));
            }
        }
        double maxT = 0;
        for (pdi p : hull){
            maxT = max(maxT,(D-horse[p.S].S)/horse[p.S].F);
        }
        printf("Case #%d: %.6lf\n",z,D/maxT);
    }
    return 0;
}
