#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
using namespace std;

int N, K;
int A[1005][3];

typedef pair<int,int> ii;
typedef pair<ii,int> iii;
int target;

int cmp(iii a1, iii a2){
    if(a1.second == target) return 1;
    if(a2.second == target) return 0;
    double t1 = a1.first.first;
    double t2 = a1.first.second;
    double t3 = a2.first.first;
    double t4 = a2.first.second;
    return t1 * t2 > t3 * t4;
}


double test(int idx){
    vector <iii> V;
    for(int i=1;i<=N;i++){
        // if(i == idx) continue;
        if(A[i][0] <= A[idx][0]){
            V.push_back(iii(ii(A[i][0], A[i][1]),i));
        }
    }
    target = idx;
    // printf("idx = %d  %d\n",idx,V.size());
    if(V.size() < K) return 0.00;
    sort(V.begin(), V.end(), cmp);
    assert(V[0].second == idx);
    double sum = 0.0;
    
    double max_r = 0.00;
    for(int i=0;i<K;i++){
        max_r = max(max_r, (double)V[i].first.first);
        // if(V[i].second == idx) found = true;
        // printf("[%d][%d]\n",V[i].first.first, V[i].first.second);
        sum += 2.000 * M_PI * (double)V[i].first.first * (double)V[i].first.second;
    }
    assert(fabs(max_r - V[0].first.first) < 1e-6);
    // if(found) sum += 2.0 * M_PI * (double) V[K-1].first.first * (double)V[K-1].first.second;
    // sum += 2.0 * M_PI * (double)A[idx][0] * (double)A[idx][1];
    sum += M_PI * (double)V[0].first.first * (double)V[0].first.first;

    // printf("idx = %d, sum = %lf\n",idx,sum);
    return sum;
}

double test2(int mask){
    vector <ii> V;
    double max_r = 0.0;
    for(int i=1;i<=N;i++){
        if(mask & (1<<(i-1))){
            V.push_back(ii(A[i][0],A[i][1]));
            max_r = max(max_r, (double)A[i][0]);
        }
    }
    if(V.size() != K) return 0.00;

    double sum = 0.0;
    for(int i=0;i<K;i++) sum += 2.0 * M_PI * (double)V[i].first * (double)V[i].second;
    return sum + M_PI * max_r * max_r;
}

void run(){
    scanf("%d %d",&N, &K);
    for(int i=1;i<=N;i++) scanf("%d %d", &A[i][0], &A[i][1]);

    double maxval = 0.00;
    // double maxvaltest = 0.000;
    // for(int i=1;i<(1<<N);i++){
        // maxvaltest = max(maxvaltest,test2(i));
        // printf("i = %x   test = %lf\n",i,maxvaltest);
    // }
    for(int i=1;i<=N;i++){
        maxval = max(maxval,test(i));
        // printf("i = %d, maxval = %lf\n",i,maxval);
    }
    // assert(fabs(maxval - maxvaltest) < 1e-6);;
    printf("%.10lf\n", maxval);
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