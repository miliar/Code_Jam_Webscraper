#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int M[101][101][101][101];
int hd, ad, hk, ak, B, D;

vvi neighs(vi& V) {
    vvi ans;
    int x = V[0], y = V[1], z = V[2], w = V[3];
    vi U;
    if(x > 0 && y >= z) {
        U = {0,0,0,0};
        ans.push_back(U);
    }
    else if (x > 0) {
        U = {max(hd - w, 0), y, z, w};
        ans.push_back(U);
        U = {max(x - w, 0), y, z - y, w};
        ans.push_back(U);
        U = {max(x - w, 0), y + B, z, w};
        ans.push_back(U);
        U = {max(x - max(w - D, 0), 0), y, z, max(w - D, 0)};
        ans.push_back(U);
    }
    return ans;
}

int ind(vi& V) {
    return M[V[0]][V[1]][V[2]][V[3]];
}

void vset(vi& V, int x) {
    M[V[0]][V[1]][V[2]][V[3]] = x;
}

int main(){
    int T, ans;
    cin >> T;
    for(int t = 1; t <= T; t++){
        memset(M, 0, sizeof M);
        cin >> hd >> ad >> hk >> ak >> B >> D;
        queue<vi> Q;
        vi V = {hd, ad, hk, ak};
        Q.push(V);
        ans = 0;
        vset(V, 1);
        while(!Q.empty()){
            vi V = Q.front();
            Q.pop();
            vvi N = neighs(V);
            if(N.size() == 1) {
                ans = ind(V);
                break;
            }
            for(vi& U : neighs(V)) if(ind(U) == 0) {
                vset(U, ind(V) + 1);
                Q.push(U);
            }
        }
        if(ans > 0) {
            printf("Case #%d: %d\n", t, ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
    }
    return 0;
}
