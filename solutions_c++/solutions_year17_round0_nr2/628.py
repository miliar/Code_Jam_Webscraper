#include <bits/stdc++.h>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

bool is_tidy(int64_t N) {
    std::string s; std::stringstream ss; ss << N; ss >> s;
    REP(i,SZ(s)-1) if(s[i]>s[i+1]) return false;
    return true;
}

int64_t naive(int64_t N) {
    do {
        if(is_tidy(N)) return N;
    } while (--N);
}

void solve() {
    int64_t N; std::string s;
    {
        std::cin >> N; std::stringstream ss; ss << N; ss >> s;
    }
    bool changed = true;
    while (changed) {
        changed = false;
        REP(i,SZ(s)-1) {
            if (s[i] > s[i+1]) {
                s[i]--;
                for (int k = i+1; k < SZ(s); k++) {
                    s[k] = '9';
                }
                changed = true;
                break;
            }
        }
    }
    int64_t ans; std::stringstream ss; ss << s; ss >> ans;
    std::cout << ans << std::endl;
}

int main() {
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

