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
ll n,m,T,k;

string nts(ll x){
    ostringstream ss;
    ss << x;
    return ss.str();
}

vector<ll> A;
vector<ll> P;
ll D[4] = {0};
unordered_map<ll,ll> M;

ll has(ll n1,ll n2, ll n3, ll prev){
    return n1*101*101*5 + n2*101*5 + n3*5 + prev;
}


ll dp(ll n1, ll n2, ll n3, ll prev){
if(n1+n2+n3 == 0)return 0;
ll h = has(n1,n2,n3,prev);
if(M.find(h) != M.end())return M[h];
ll ans = 0;
ll a2 = 0;
if(prev == 0)a2++;
if(n1 != 0){
    ans = max(ans , a2+dp(n1-1,n2,n3,(prev+1)%4));
}
if(n2 != 0){
    ans = max(ans , a2+dp(n1,n2-1,n3,(prev+2)%4));
}
if(n3 != 0){
    ans = max(ans , a2+dp(n1,n2,n3-1,(prev+3)%4));
}
M[h] = ans;
return ans;
}

ll giveans(){
ll ans = 0;
ll sum = 0;
for(ll c1 = 0; c1 < n; c1++){
    if(sum%k == 0){
        ans++;
    }
    sum += P[c1];
}
return ans;
}

void fixp(){
vector<vector<ll> > C(4 , vector<ll>());
for(ll c1 = 0; c1 < n; c1++){
    //cerr << A[c1]%k << "\n";
    C[A[c1]%k].push_back(A[c1]);
}

if(k == 2){
    for(ll c1 = 0; c1 < C[0].size(); c1++){
        P.push_back(C[0][c1]);
    }
    for(ll c1 = 0; c1 < C[1].size(); c1++){
        P.push_back(C[1][c1]);
    }
}

if(k == 3){

    for(ll c1 = 0; c1 < C[0].size(); c1++){
        P.push_back(C[0][c1]);
    }

    ll a1 = 1;
    ll a2 = 2;
    if(C[2].size() > C[1].size()){
        a1 = 2;
        a2 = 1;
    }

    ll l = 0;
    for(ll c1 = 0; c1 < C[a1].size(); c1++){
        P.push_back(C[a1][c1]);
        if(l < C[a2].size()){
            P.push_back(C[a2][l]);
            l++;
        }
    }
}

if(k == 4){

    for(ll c1 = 0; c1 < C[0].size(); c1++){
        P.push_back(C[0][c1]);
    }

    ll c2s = ll(C[2].size());
    for(ll c1 = 0; c1 < c2s-c2s%2; c1++){
        P.push_back(C[2][c1]);
    }

    ll a1 = 1;
    ll a2 = 3;
    if(C[3].size() > C[1].size()){
        a1 = 3;
        a2 = 1;
    }

    ll l = 0;
    for(ll c1 = 0; c1 < C[a1].size(); c1++){
        P.push_back(C[a1][c1]);
        if(l < C[a2].size()){
            P.push_back(C[a2][l]);
            l++;
        }
    }

    if(c2s%2 == 1){
        P.push_back(C[2][c2s-1]);
    }
}

/*
for(ll c1 = 0; c1 < n; c1++){
    cerr << P[c1] << " ";
}
*/

if(P.size() != n){
    cerr << "invalid size\n";
}

}


ll ans2(){
M.clear();
for(ll c1 = 0; c1 < n; c1++){
    D[A[c1]%4]++;
}
ll ans = D[0];
ans += dp(D[1],D[2],D[3],0);
return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    ll a,b,c;

    cin >> T;

    for(ll c4 = 0; c4 < T; c4++){
        D[0] = 0;
        D[1] = 0;
        D[2] = 0;
        D[3] = 0;
        cin >> n >> k;

        A.clear();
        P.clear();

        for(ll c1 = 0; c1 < n; c1++){
            cin >> a;
            A.push_back(a);
        }

        fixp();
        ll ans = giveans();
        if(k == 4){

            ll a2 = ans2();

            if(ans < a2){
               // cerr <<c4 << ":  "<< ans << " " << a2 << "  -  " << D[0] << "," << D[1] << "," << D[2] << "," << D[3] << "\n";

            }

            if(ans > a2){cerr << "HASDJKDHASJKDHASJKDH\n";}

            if(ans < a2)ans = a2;
        }
        cout << "Case #" << c4+1 << ": " << ans << "\n";
    }

    return 0;
}
