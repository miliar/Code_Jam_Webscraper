//touch {a..m}.in; tee {a..m}.cpp < template.cpp
#include <bits/stdc++.h>
using namespace std;
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define pb push_back
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define dprint(v) cout << #v"=" << v << endl //;)

const int MAXN=100100;
ll n;

bool is_tidy(ll x){
    char buf[1024];
    sprintf(buf, "%lld", x);
    for(int i=1; buf[i]; i++)
        if(buf[i]<buf[i-1]) return false;
    return true;
}
ll brute( ll x){
    for(ll i=x; ; i--)
        if(is_tidy(i)) return i;
    return 0;
}

ll greedy(ll x){
    char buf[1024];
    sprintf(buf, "%lld", x);
    for(int i=1; buf[i]; i++){
        if(buf[i]<buf[i-1]){
            buf[i-1]--;
            for(int j=i; buf[j]; j++)
                buf[j]='9';
            for(int j=i-1; j; j--){
                if(buf[j]<buf[j-1]){
                    buf[j]='9';
                    buf[j-1]--;
                }
            }
        }
    }
    return atoll(buf);
}

void solve(){
    cin >> n;
    ll q=greedy(n);
    cout << q;
}

int main() {
    //~ dforn(i, 1000010){
        //~ if(i%1000==0)dprint(i);
        //~ if(greedy(i)!=brute(i)){
            //~ dprint(i);
            //~ dprint(greedy(i));
            //~ dprint(brute(i));
            //~ assert(false);
        //~ }
    //~ }
    
    freopen("B-large.in", "r", stdin);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
