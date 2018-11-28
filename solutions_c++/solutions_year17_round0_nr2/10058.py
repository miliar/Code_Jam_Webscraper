#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define rep(i,n) FOR(i,0,n)
#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define SZ(x) (int)(x).size()
#define mset(a,x) memset(a,x,sizeof(a))
#define dbg(x) cout<<#x<<": "<<(x)<<"\n"
#define OUT(x) cout<<(x)<<"\n"
#define FASTIO cin.tie(0),ios::sync_with_stdio(0)
#define pb push_back
#define mp make_pair

int solve(int x){
    for(int i = x; i >= 0; --i){
        string s = to_string(i);
        bool f = true;
        rep(j, s.size() - 1){
            if(s[j] > s[j+1]) {
                f = false;
                break;
            }
        }
        if(f) return i;
    }
    return 0;
}

int main(){
    int t;
    cin>>t;
    rep(c, t){
        int x;
        cin>>x;
        int ans = solve(x);
        printf("Case #%d: %d\n", c+1, ans);
    }

    return 0;
}