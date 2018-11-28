#include <bits/stdc++.h>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

void flip(char&c) { c = (c=='-')?'+':'-'; }

void solve() {
    std::string s; int K; std::cin >> s >> K;
    int S = SZ(s);

    int ans = 0;
    REP(i,S-K+1){
        if(s[i]=='-'){
            REP(k,K) flip(s[i+k]);
            ans++;
        }
    }
    REP(k,K){
        if(s[S-k-1]=='-'){
            std::cout << "IMPOSSIBLE" << std::endl;
            return;
        }
    }
    std::cout << ans << std::endl;
}

int main() {
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

