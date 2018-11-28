#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const double pi = acos(-1);
const int N = 1e6+10;
int cas = 1, n, k;

struct Node{
    ll r, h;
}p[N];

bool cmp(Node a, Node b){
    if( a.h * a.r == b.h * b.r) return a.r > b.r;
    return a.h * a.r > b.h * b.r;
}

ll solve(ll j, ll mr){
    vector<Node> v;
    for(int i=0;i<n;i++){
        if(i == j || p[i].r > p[j].r) continue;
        v.push_back(p[i]);
    }
    if(v.size() + 1 < k) return 0;
    sort(v.begin(), v.end(), cmp);
    ll ans = 0;
    for(int i=0;i<k-1;i++){
        ans += v[i].r * v[i].h * 2;
    }
    ans += p[j].r * p[j].h * 2;
    ans += mr * mr;
    return ans;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    while(T--){
        cin >> n >> k;
        for(int i=0;i<n;i++){
            cin >> p[i].r >> p[i].h;
        }
        printf("Case #%d: ", cas++);
        ll ans = 0;
        for(int i=0;i<n;i++){
            ll t = solve(i, p[i].r);
            if(t > ans) ans = t;
        }
        printf("%.9f\n", pi * ans);
    }
    return 0;
}
