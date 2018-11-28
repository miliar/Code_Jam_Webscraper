#include <bits/stdc++.h>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

struct Horse {
    int k, s;
    double t;
    bool operator<(const Horse& rhs) const { return k < rhs.k; }
};

void solve() {
    int D, N; std::cin >> D >> N;
    std::vector<Horse> H(N); REP(i,N) std::cin >> H[i].k >> H[i].s;
    std::sort(ALL(H));
    REP(i,N) {
        const int d = D - H[i].k;
        H[i].t = double(d) / H[i].s;
    }
    REP_R(i,N) if(i<N-1) {
        H[i].t = std::max(H[i].t, H[i+1].t);
    }
    const double ans = D / H[0].t;
    std::cout << std::fixed << std::setprecision(8) << ans << std::endl;
}

int main() {
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

