#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<utility>
#include<queue>
#include<stack>
#include<string>


#define ri(X) scanf("%d",&X)
#define rii(X,Y) scanf("%d %d",&X,&Y)
#define rf(X) scanf("%lf",&X)
#define rff(X,Y) scanf("%lf %lf",&X,&Y)
#define mp(X,Y) make_pair(X,Y)
#define pii pair<int,int>
#define FOR(i,j) for(int i=0;i<j;i++)
#define FORC(i,j,c) for(int i=0;i<j;i+=c)

using namespace std;
int T;
double D;
const int mn = 1010;
pii ks[mn];
int N;
double oo = 1e9;
const double eps = 1e-9;

double get_int(double d1, double d2, double v1, double v2){
    return (v1<=v2) ? oo : (d2-d1)/(v1-v2);
}
double last_t(){
    if (N==1) return (D-ks[0].first)/ks[0].second;
    double lt = 0;

    
    FOR(i,N){
        double mint = oo;
        FOR(j,N-1){
            if(ks[j+1].first - ks[j].first > eps){
                mint = min(mint, get_int(ks[j].first, ks[j+1].first, ks[j].second, ks[j+1].second));
            }
        } 
        double dt = mint;
        bool all_reach = true;
        FOR(i,N){
            all_reach = all_reach && (ks[i].first + dt*ks[i].second >= D);
        }
        if(all_reach) {
            double maxt = 0.0;
            FOR(i,N){
                maxt = max(maxt, (D - ks[i].first) / ks[i].second);
            }    
            return maxt + lt;
        }
        ks[0].first += dt*ks[0].second;
        FOR(i,N-1){
            ks[i+1].first += dt * ks[i+1].second;
            if (ks[i+1].first - ks[i].first < eps) {
                ks[i].second = ks[i+1].second;
                ks[i].first = ks[i+1].first;
            }
        }
        lt += mint;
    }    
}

int main(){

    cin >> T;
    FOR(i,T){
        cout << "Case #" << i+1 << ": ";
        cin >> D >> N;
        FOR(j,N){
            cin >> ks[j].first >> ks[j].second;
        }
        sort(ks,ks+N);
        printf("%.6lf\n", D/last_t());
    }

	return 0;
}
