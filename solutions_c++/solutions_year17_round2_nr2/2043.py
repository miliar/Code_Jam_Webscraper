#include <bits/stdc++.h>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

bool is_legit(const std::string& P) {
    if (P.front() == P.back()) return false;
    REP(i,SZ(P)-1) if(P[i]==P[i+1]) return false;
    return true;
}

std::string solve_simple(int R, int Y, int B) {
    struct Pony { int n; char c;
        bool operator<(const Pony& rhs) const { return n < rhs.n; }
    };
    Pony P[3] = { Pony{R,'R'}, Pony{Y,'Y'}, Pony{B,'B'} };
    std::string soln; soln.reserve(R+Y+B);
    std::sort(P, P+3);
    std::reverse(P, P+3);
#if 0
    std::cout << std::endl;
    REP(i,3) std::cout << P[i].c << ": " << P[i].n << std::endl;
#endif
    if (P[0].n == 1) return "RYB";
    if (P[1].n == 0) return "IMPOSSIBLE";

    REP(_,P[0].n) soln.push_back(P[0].c);
    P[0].n = 0;
    soln.push_back(P[1].c);
    P[1].n--;
    REP(k,3) if(k>0) {
        REP_R(i,SZ(soln)-1) if(P[k].n) if(soln[i]==soln[i+1]) {
            soln.insert(i+1, 1, P[k].c);
            P[k].n--;
        }
    }
    REP(k,3) if(k>0) {
        REP_R(i,SZ(soln)-1) if(P[k].n) if(soln[i]!=P[k].c) if(soln[i+1]!=P[k].c) {
            soln.insert(i+1, 1, P[k].c);
            P[k].n--;
        }
    }
    if (!is_legit(soln)) return "IMPOSSIBLE";
    return soln;
}

void solve() {
    int N,R,O,Y,G,B,V; std::cin >> N >> R >> O >> Y >> G >> B >> V;
    std::string soln = solve_simple(R, Y, B);
    std::cout << soln << std::endl;
    //assert(soln == "IMPOSSIBLE" || is_legit(soln));
}

int main() {
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

