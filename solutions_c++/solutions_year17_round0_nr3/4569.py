#include <iostream>
#include <queue>

using namespace std;

typedef long long ll;

void print_debug(priority_queue<ll> Q) {
    while(!Q.empty()) {
        cout << Q.top() << " ";
        Q.pop();
    }
    cout << endl;
}

int main(int argn, char* argv[]) {
    freopen("/Users/jorgemoag/Downloads/C-small-2-attempt0.in.txt", "r", stdin);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll N,K; scanf("%lld%lld",&N,&K);
        priority_queue<ll> Q;
        Q.push(N);
        //print_debug(Q);
        ll L = 0, R = 0;
        while(K--) {
            ll x = Q.top(); Q.pop();
            L = x >> 1;
            R = (x >> 1) - 1 + x %2;
            Q.push(L); Q.push(R);
            //print_debug(Q);
        }
        printf("Case #%d: %lld %lld\n", t, L, R);
    }
}
