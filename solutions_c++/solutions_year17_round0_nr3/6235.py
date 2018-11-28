#include <bits/stdc++.h>
using namespace std;
int N, M, nxt[1001001], prv[1001001], num, a[1001001];
int f(int p, int q){
    if(p > q) swap(p, q);
    return (q-p)/2;
}

int g(int p, int q){
    if(p > q) swap(p, q);
    return (q-p) - ((q-p)/2);
}
struct data{
    int x, y;
    data(){}
    data(int x, int y):x(x),y(y){}
    bool operator < (const data &r) const{
        int fx = f(x, y), fy = f(r.x, r.y), gx = g(x, y), gy = g(r.x, r.y);
        if(fx == fy && gx == gy) return x > r.x;
        if(fx == fy) return gx < gy;
        return fx < fy;
    }
};

priority_queue <data> Q;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.out", "w", stdout);
    int i, j, T, dap, dap1, dap2;
    cin>>T;
    for(int t=1; t<=T; t++){
        scanf("%d %d" ,&N, &M);
        Q.push(data(0, N+1));
        nxt[0] = N+1, prv[N+1] = 0;
        for(i=0; i<M; i++){
            data X = Q.top();
            while(1){
                if(Q.empty()) break;
                X = Q.top();
                if(nxt[X.x] == X.y && prv[X.y] == X.x) break;
                else Q.pop();
            }
            X = Q.top();
            int ans = (X.y - X.x) / 2 + X.x;
            a[++num] = ans;
            nxt[X.x] = ans, prv[X.y] = ans;
            nxt[ans] = X.y, prv[ans] = X.x;
            Q.push(data(X.x, ans));
            Q.push(data(ans, X.y));
            dap = ans;
            dap1 = f(X.x, X.y);
            dap2 = g(X.x, X.y);
        }
        printf("Case #%d: %d %d\n", t, dap2-1, dap1-1);
        while(!Q.empty()) Q.pop();
        for(i=0; i<=N+1; i++) prv[i] = nxt[i] = 0;
        num = 0;
    }
}
