#include <cstdio>
#include <algorithm>
using namespace std;

long long int T, D, N;

struct Data{
    long long int id;
    long long int K;
    long long int S;
    long double time;
};

struct Data data[2000];

bool cmp(struct Data a, struct Data b){
    return a.time<b.time;
}

int main(){
    scanf("%lld", &T);
    for(long long int t=1; t<=T; t++){
        scanf("%lld %lld", &D, &N);
        for(long long int n=0;n<N;n++){
            scanf("%lld %lld", &data[n].K, &data[n].S);
            
            data[n].id = n;
            data[n].time = (long double)(D-data[n].K)/data[n].S;
        }
        sort(data, data+N, cmp);
        printf("Case #%lld: %.6Lf\n", t, (double)D/data[N-1].time );
    }

}
