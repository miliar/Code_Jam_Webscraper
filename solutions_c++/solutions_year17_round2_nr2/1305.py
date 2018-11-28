#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <cassert>

using namespace std;
typedef long long LL;

string repeat(string s, int n){
    string res;
    for(int i = 0; i < n; ++i){
        res += s;
    }
    return res;
}

string replaceGVO(string s, LL G, LL V, LL O){
    if(G > 0){
        LL i = s.find("R");
        s.insert(i, repeat("RG", G));
    }
    if(V > 0){
        LL i = s.find("Y");
        s.insert(i, repeat("YV", V));
    }
    if(O > 0){
        LL i = s.find("B");
        s.insert(i, repeat("BO", O));
    }
    return s;
}

string solve(LL N, LL R, LL O, LL Y, LL G, LL B, LL V){
    if(N == R + G && R == G){
        return repeat("RG", N/2);
    }
    if(N == Y + V && Y == V){
        return repeat("YV", N/2);
    }
    if(N == B + O && B == O){
        return repeat("BO", N/2);
    }
    if(G >= R+1){
        return "IMPOSSIBLE";
    }else{
        R -= G;
    }
    if(V >= Y+1){
        return "IMPOSSIBLE";
    }else{
        Y -= V;
    }
    if(O >= B+1){
        return "IMPOSSIBLE";
    }else{
        B -= O;
    }
    if(R >= Y + B + 1 || Y >= B + R + 1 || B >= R + Y + 1){
        return "IMPOSSIBLE";
    }
    int n2 = N - G - V - O;
    if(R >= Y && R >= B){
        int r = max<LL>(0, Y+B-n2/2);
        string res = repeat("RY", Y-r) + repeat("RB", B-r) + repeat("R", N%2) + repeat("YB", r);
        assert(Y-r + B-r == R - N%2);
        assert(res.size() == N);
        return replaceGVO(res, G, V, O);
    }else if(Y >= B && Y >= R){
        int r = max<LL>(0, B+R-n2/2);
        string res = repeat("YB", B-r) + repeat("YR", R-r) + repeat("Y", N%2) + repeat("BR", r);
        assert(B-r + R-r == Y - N%2);
        assert(res.size() == N);
        return replaceGVO(res, G, V, O);
    }else{ // B >= R && B >= Y
        int r = max<LL>(0, R+Y-n2/2);
        string res = repeat("BR", R-r) + repeat("BY", Y-r) + repeat("B", N%2) + repeat("RY", r);
        assert(R-r + Y-r == B - N%2);
        assert(res.size() == N);
        return replaceGVO(res, G, V, O);
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << t << ": " << solve(N, R, O, Y, G, B, V) << endl;
    }
    return 0;
}

