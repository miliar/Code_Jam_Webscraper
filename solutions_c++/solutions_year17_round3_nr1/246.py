#include <bits/stdc++.h>

using namespace std;

double pi = acos(-1);

struct Pcake{
    int r, h;
    double a;

    bool operator<(const Pcake & rhs) const{
        if(a == rhs.a){
            if(r == rhs.r){
                return h < rhs.h;
            }
            return r > rhs.r;
        }
        return a > rhs.a;
    }
};

int N, K;

vector<Pcake> ps (N);
vector<vector<long double > > mem;

long double solve(int pos, int k, int r){
    if(pos == N) return 0.0;
    if(k == K) return 0.0;
    if(mem[k][r] != -1.0) return mem[k][r];
    if(ps[pos].r < r ) return 0.0;
    long double extra = pi*ps[pos].r*ps[pos].r - pi*(r*r) + 2 * pi * ps[pos].r * ps[pos].h;
    long double test = max( solve( pos+1, k, r), solve( pos+1, k+1, ps[pos].r) + extra);
    mem[k][r] = test;
//    cout << pos << " " << k << " " << r << " " << mem[k][r] << endl;
    return mem[k][r];
}

int main()

{
    freopen("A-large (1).in","r",stdin);
//freopen("in.txt","r",stdin);
    freopen("outreal.txt","w",stdout);
    ios::sync_with_stdio(false); cin.tie(0);
    int T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        cin >> N >> K;
        ps.assign(N, {0,0,0.0});
        vector<vector<Pcake> > combis (N, vector<Pcake> ());
        int maxr = 0;
        for(int i = 0; i < N; i++){
            cin >> ps[i].r >> ps[i].h;
//            maxr = max(maxr, ps[i].r);
            ps[i].a = pi * 2 * ps[i].r * ps[i].h;
        }
        //sort(ps.begin(),ps.end());
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(i == j) continue;
                if(ps[i].r >= ps[j].r){
                    combis[i].push_back(ps[j]);
                }
            }
        }
        for(int i = 0; i < N; i++){
            sort(combis[i].begin(), combis[i].end());
        }
        double ans = 0;
        for(int i = 0; i < N; i++){
            if(combis[i].size() < K-1) continue;
            double temp = 0;
            for(int j = 0; j < K-1; j++){
                temp += combis[i][j].a;
            }
            ans = max(ans, temp + pi * ps[i].r * ps[i].r + ps[i].a);
        }
//        mem.assign(K+1, vector<long double> (maxr+1, -1.0));
        cout << "Case #" << cnt << ": ";
        cout << fixed << setprecision(8) << ans << endl;
    }


    return 0;
}
