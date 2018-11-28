#include <bits/stdc++.h>

using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll big = 1000000007ll;
ll big2 = 1000000009ll;
ll n,m,q,T,k;

ll M[101][101] = {0};
ll M2[101][101] = {0};

ll MP[101][101] = {0};
ll MK[101][101] = {0};

vector<int> match;
vector<bool> seen;
template<class G>
bool find(int j, G &g){
    if(match[j] == -1)return 1;
    seen[j] = 1; int di = match[j];
    trav(e, g[di]){
        if(!seen[e] && find(e ,g)){
            match[e] = di;
            match[j] = -1;
            return 1;
        }
    }
    return 0;
}

template<class G>
int dfs_matching(G &g, int N, int M){
    match.assign(M, -1);
    rep(i,0,N){
        seen.assign(M, false);
        trav(j,g[i]){
            if(find(j, g)){
                match[j] = i;
                break;
            }
        }
    }
    return M - count(all(match), -1);
}

void fixp(){

    bool mark1[301] = {0};
    bool mark2[301] = {0};
    match.clear();
    seen.clear();
    for(ll c1 = 0; c1 < n; c1++){
        for(ll c2 = 0; c2 < n; c2++){
            if(MP[c1][c2] == 1){
                mark1[c1+c2] = 1;
                mark2[c2-c1+n-1] = 1;
            }
        }
    }

    vector<vector<ll> > C(301 , vector<ll>());

    for(ll c1 = 0; c1 < 2*n-1; c1++){
        if(mark1[c1] == 0){
            for(ll c2 = min(n-1,c1); c2 >= 0; c2--){
                ll c3 = c1-c2;
                if(c3 < n){
                    if(mark2[c3-c2+n-1] == 0){
                        C[c1].push_back(c3-c2+n-1);
                    }
                }
            }
        }
    }

    dfs_matching(C, 2*n-1, 2*n-1);

    for(ll c1 = 0; c1 < 2*n-1; c1++){
        if(match[c1] != -1){
            ll c2 = match[c1];
            ll c3 = c1-n+1;
            MP[(c2-c3)/2][(c3+c2)/2] = 1;
        }
    }
}

ll fixk(){

    bool mark1[101] = {0};
    bool mark2[101] = {0};
    vector<ll> P;
    vector<ll> Q;
    for(ll c1 = 0; c1 < n; c1++){
        for(ll c2 = 0; c2 < n; c2++){
            if(MK[c1][c2] == 1){
                mark1[c1] = 1;
                mark2[c2] = 1;
            }
        }
    }

    for(ll c1 = 0; c1 < n; c1++){
        if(!mark1[c1])P.push_back(c1);
    }

    for(ll c1 = 0; c1 < n; c1++){
        if(!mark2[c1])Q.push_back(c1);
    }

    for(ll c1 = 0; c1 < P.size(); c1++){
        MK[P[c1]][Q[c1]] = 1;
    }

}

char pars(ll i){
 if(i == -1)return ' ';
 if(i == 0)return '+';
 if(i == 1)return 'x';
 if(i == 2)return 'o';
 return 'X';
 }

ll eva(){
ll ans = 0;
for(ll c1 = 0; c1 < n; c1++){
    for(ll c2 = 0; c2 < n; c2++){
        if(M[c1][c2] == 0 || M[c1][c2] == 1)ans++;
        if(M[c1][c2] == 2)ans+=2;
    }
}
return ans;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    cin >> T;

    for(ll c4 = 0; c4 < T; c4++){
        for(ll c1 = 0; c1 < 101; c1++){
            for(ll c2 = 0; c2 < 101; c2++){
                M[c1][c2] = -1;
                MP[c1][c2] = 0;
                MK[c1][c2] = 0;
            }
        }
        cin >> n >> m;
        for(ll c1 = 0; c1 < m; c1++){
            char ch;
            ll a,b;
            cin >> ch >> a >> b;
            a--;
            b--;
            if(ch == '+')M[a][b] = 0, MP[a][b] = 1;
            if(ch == 'x')M[a][b] = 1, MK[a][b] = 1;
            if(ch == 'o')M[a][b] = 2, MP[a][b] = 1, MK[a][b] = 1;
        }
        fixp();
        fixk();


        vector<pair<ll,ll> > ANS;
        vector<char> ANS2;

        for(ll c1 = 0; c1 < n; c1++){
            for(ll c2 = 0; c2 < n; c2++){
                ll c3 = -1;
                if(MP[c1][c2])c3++;
                if(MK[c1][c2])c3+=2;
                char ch = pars(c3);
                if(M[c1][c2] != c3){
                    ANS.push_back({c1+1,c2+1});
                    ANS2.push_back(ch);
                }
                M[c1][c2] = c3;
            }
        }
        ll ans = eva();
        cout << "Case #" << c4+1 << ": " << ans << " " << ANS.size() << "\n";
        for(ll c1 = 0; c1 < ANS.size(); c1++){
            cout << ANS2[c1] << " " << ANS[c1].first << " " << ANS[c1].second << "\n";
        }
    }
    return 0;
}
