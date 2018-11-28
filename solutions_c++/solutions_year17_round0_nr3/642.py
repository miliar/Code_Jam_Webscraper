#include <bits/stdc++.h>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

void solve() {
    int64_t N,K; std::cin >> N >> K;
    int64_t a = 1;
    for (;;) {
        if (K <= a) {
            int64_t b = N / a;
            int64_t T = N % a;
            if (K <= T) b++;
            std::cout << b/2 << " " << (b-1)/2 << std::endl;
            return;
        }
        K -= a;
        N -= a;
        a <<= 1;
    }
}

int main() {
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

