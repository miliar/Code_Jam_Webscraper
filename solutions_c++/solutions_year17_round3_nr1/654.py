#include <cstdio>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

double pi;
pair<double,double> P[1009];

int cmp(pair<int,int> a, pair<int,int> b){
    if ((double)a.first*a.second>(double)b.first*b.second) return 1;
    else if ((double)a.first*a.second<(double)b.first*b.second) return -1;
    else return int(a.first-b.first);
}

int main(){
    freopen("A-large (2).in","r",stdin);
    freopen("1cAsmalllarge.out","w",stdout);
    pi = acos(-1);
    //printf("%f",pi);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, K;
        scanf("%d %d", &N, &K);
        for (int i = 0; i < N; i++){
            int r, h;
            scanf("%d %d", &r, &h);
            P[i].first = pi*r*r;
            P[i].second = 2*pi*r*h;
        }
        std::sort(P,P+N);
        double ans = 0;
        for (int i = K-1; i < N; i++){
            priority_queue<double> Q;
            for (int j = 0; j < i; j++){
                Q.push(P[j].second);
            }
            double sum = 0;
            for (int j = 0; j < K-1; j++){
                sum += Q.top();
                Q.pop();
            }
            ans = max(ans,sum+P[i].second+P[i].first);
        }
        printf("Case #%d: %f\n", t, ans);
    }
}
