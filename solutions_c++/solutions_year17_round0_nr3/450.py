#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("Clargeoutput.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        long long N, K;
        scanf("%lld %lld", &N, &K);
        priority_queue<pair<long long,long long> > Q;
        Q.push(make_pair(N,1));
        long long k = 0;
        long long x,y;
        while (k<K){
            pair<long long,long long> p = Q.top();
            Q.pop();
            while (!Q.empty() && Q.top().first==p.first){
                p.second += Q.top().second;
                Q.pop();
            }
            if (p.first>0){
                x = p.first/2;
                y = (p.first-1)/2;
                Q.push(make_pair(x,p.second));
                Q.push(make_pair(y,p.second));
            }
            k += p.second;
        }
        printf("Case #%d: %lld %lld\n", t, x, y);
    }
}
