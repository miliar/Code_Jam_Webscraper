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


vector<vector<ll> > C(101 , vector<ll>());
vector<vector<ll> > CW(101 , vector<ll>());
ll MW[101][101] = {0};
ll deg[101] = {0};

vector<ll> D;
vector<ll> V;

ll SP[101][101] = {0};
ld DP[101][101][101] = {0};

ld DP2[101] = {0};

void dijk(ll i){

priority_queue<pair<ll,ll> > PQ;
PQ.push({0,i});
bool mark[101] = {0};
SP[i][i] = 0;
while(!PQ.empty()){
    pair<ll,ll> P;
    P = PQ.top();
    PQ.pop();
    ll w = -P.first;
    ll a = P.second;

    if(!mark[a]){
        mark[a] = 1;

        for(ll c1 = 0; c1 < deg[a]; c1++){
            ll b = C[a][c1];
            if(!mark[b]){
                ll w2 = w + CW[a][c1];
                if(SP[i][b] > w2 || SP[i][b] == -1){
                    PQ.push({-w2 , b});
                    SP[i][b] = w2;
                }
            }
        }
    }
}
}

ld dp(ll i, ll j, ll depth){

if(depth == n)return big*big;
if(i == j)return 0.0;
if(DP[i][j][depth] >= 0.0)return DP[i][j][depth];

ld ans = big*big;
//cerr << i <<" "<< j << "\n";
for(ll c1 = 0; c1 < n; c1++){
    if(c1 != i){

        ll dist = SP[i][c1];
        if(dist != -1){

        if(dist <= D[i]){
            ans = min(ans , ld(dist) / ld(V[i]) + dp(c1,j,depth+1));
        }

        }
    }
}

DP[i][j][depth] = ans;
return ans;


}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    ll a,b,c;

    cin >> T;

    for(ll c4 = 0; c4 < T; c4++){
        cerr << c4 << "\n";
        cin >> n >> q;
        D.clear();
        V.clear();
        for(ll c1 = 0; c1 < n; c1++){
            C[c1].clear();
            CW[c1].clear();
            deg[c1] = 0;
        }

        for(ll c1 = 0; c1 < n; c1++){
            cin >> a >> b;
            D.push_back(a);
            V.push_back(b);
            DP2[c1] = -1;
        }

        for(ll c1 = 0; c1 < n; c1++){
            for(ll c2 = 0; c2 < n; c2++){
                cin >> a;
                MW[c1][c2] = a;
                SP[c1][c2] = -1;
                for(ll c3 = 0; c3 < n; c3++){
                    DP[c1][c2][c3] = -1;
                }
                if(a != -1){
                    C[c1].push_back(c2);
                    CW[c1].push_back(a);
                    deg[c1]++;
                }

            }
        }

        for(ll c1 = 0; c1 < n; c1++){
            dijk(c1);

            if(c4 == -1){
                for(ll c2 = 0; c2 < n; c2++){
                    cerr << SP[c1][c2] << " ";
                }cerr << "\n";
            }
        }
        //cerr << "\n";
        cout << "Case #" << c4+1 << ": ";
        for(ll c1 = 0; c1 < q; c1++){
            cin >> a >> b;
            a--;
            b--;
            ld ans2 = dp(a,b,0);
            cout << setprecision(18) << ans2 << " ";
            if(ans2 < 0)cerr << c4 << " " << ans2 << "\n";
        }
        cout << "\n";
    }

    return 0;
}
