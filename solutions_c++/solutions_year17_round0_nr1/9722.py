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

typedef pair<string,int> P;

int main() {
    int t;
    cin >> t;
    rep(c, t){
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();

        map<string, int> MP;
        queue<P> Q;
        Q.push(make_pair(s, 0));
        MP[s]=1;
        bool f = true;
        while(!Q.empty()){
            auto p = Q.front();
            Q.pop();
            string t = p.first;
            int cnt = p.second;
            MP[t] = 1;
            if(t == string(n, '+')) {
                f = false;
                printf("Case #%d: %d\n", c + 1, cnt);
                break;
            }

            rep(i, n - k + 1){
                string tt = t;
                FOR(j, i, i+k) tt[j] = (t[j]=='+' ? '-' : '+');
                if(MP[tt]) continue;
                Q.push(make_pair(tt, cnt+1));
            }
        }
        if(f){
            printf("Case #%d: IMPOSSIBLE\n", c + 1);
        }
    }

    return 0;
}
