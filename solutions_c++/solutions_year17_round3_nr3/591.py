#include <cstdio>
#include <vector> 
using namespace std;

int N,K;
double P[100];
double U;

int cmp(double a, double b){return a < b;}

void run(){
    scanf("%d %d",&N,&K);
    scanf("%lf",&U);
    for(int i=1;i<=N;i++) scanf("%lf",&P[i]);
    vector <double> V;
    for(int i=1;i<=N;i++) V.push_back(P[i]);
    V.push_back(1);
    sort(V.begin(),V.end(),cmp);
    double tmp = U;

    for(int i=1;i<=N;i++){
        double incr = V[i] - V[i-1];
        // printf("i = %d incr = %lf\n",i,incr);
        if(incr * i <= tmp){
            tmp -= incr * i;
            for(int j=0;j<i;j++) V[j] += incr;
        }else{
            for(int j=0;j<i;j++) V[j] += tmp / i;
            break;   
        }
    }

    double ans = 1.0;
    for(int i=0;i<V.size();i++){
        // printf("[%lf]",V[i]);
        ans *= V[i];
    }
    printf("%lf\n",ans);

}

int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        run();
    }
    return 0;
}