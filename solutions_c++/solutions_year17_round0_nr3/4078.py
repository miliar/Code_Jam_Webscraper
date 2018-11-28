#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

LL n, k;

struct Sit{
    int L, R, mid, len;
    Sit(int _L, int _R){
        L = _L, R = _R, mid = (L + R) >> 1; len = R - L + 1;
    }
    bool friend operator<(const Sit a, const Sit b){
        if(a.len == b.len) return a.mid > b.mid;
        return a.len < b.len;
    }
};

priority_queue<Sit> Q;

int main(){
    freopen("2.txt", "r", stdin);
    freopen("1.txt", "w", stdout);
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; cas ++){
        scanf("%lld%lld", &n, &k);
        while(!Q.empty()) Q.pop();
        Q.push(Sit(1, n));
        for(int i = 1; i < k; i ++){
            Sit tp = Q.top();
            Q.pop();
//            printf("%d %d %d-----\n", tp.L, tp.mid, tp.R);
            if(tp.L != tp.mid) Q.push(Sit(tp.L, tp.mid - 1));
            if(tp.R != tp.mid) Q.push(Sit(tp.mid + 1, tp.R));
        }
        Sit tp = Q.top();
        printf("Case #%d: %d %d\n", cas, max(tp.mid - tp.L, tp.R - tp.mid), min(tp.mid - tp.L, tp.R - tp.mid));
    }
    return 0;
}
