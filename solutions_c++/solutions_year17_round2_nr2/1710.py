#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int N, R, O, Y, G, B, V;

struct Color{
    char c;
    int cnt;
    int f;
    Color(char c, int cnt){
        this->c = c;
        this->cnt = cnt;
        this->f = 0;
    }
};

const bool operator<(const Color &A, const Color &B){
    if(A.cnt==B.cnt){
        return A.f>B.f;
    }
    return A.cnt>B.cnt;
}



string solve(){
    string sol(N,'X');
    vector<Color> v;
    v.push_back(Color('R', R));
    v.push_back(Color('Y', Y));
    v.push_back(Color('B', B));
    sort(v.begin(), v.end());
    sol[0] = v[0].c;
    v[0].cnt--;
    v[0].f = 1;
    for(int i=1;i<N;++i){
        sort(v.begin(), v.end());
        int sel = 0;
        if(v[0].c == sol[i-1]){
            sel = 1;
        }
        if(v[sel].cnt==0){
            return "IMPOSSIBLE";
        }
        sol[i] = v[sel].c;
        v[sel].cnt--;
    }
    if(sol[0] == sol[N-1]){
        return "IMPOSSIBLE";
    }
    return sol;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        string sol = solve();
        printf("Case #%d: %s\n", t, sol.c_str());
    }
    return 0;
}

