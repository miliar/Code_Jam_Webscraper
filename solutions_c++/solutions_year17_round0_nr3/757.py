#include <cstdio>
#include <map>
#include <queue>
int main(){
    int T;
    scanf("%d",&T);
    for(int tc = 1; tc <= T; tc++){
        long long N,K;
        scanf("%lld%lld",&N,&K);
        printf("Case #%d: ",tc);
        std::priority_queue<long long> pq;
        pq.push(N);
        std::map<long long,long long> m,c;
        m[N]=1;
        while(!pq.empty()){
            auto t = pq.top();
            pq.pop();
            if(t < 1 || c[t]) continue;
            c[t] = 1;
            t--;
            m[t/2] += m[t+1];
            m[t-t/2] += m[t+1];
            pq.push(t/2);
            pq.push(t-t/2);
        }
        for(auto it = m.rbegin(); it != m.rend();it++){
            K -= it->second;
            if(K <= 0) {
                long long v = it->first - 1;
                printf("%lld %lld\n",v-v/2, v/2);
                break;
            }
        }
    }
}
