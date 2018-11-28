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
#define RND(a, b) (rand()%((b)-(a)+1)+(a))

const int MAXN=100100;
int n,k;
string s;
int ar[MAXN];
int ar2[MAXN];


int greedy(){
    int q=0;
    memcpy(ar2, ar, sizeof(int)*n);
    forn(i, n){
        if(!ar2[i]){
            forr(j, i, i+k){
                if(j>=n){
                    return -1;
                }
                ar2[j]=!ar2[j];
            }
            //~ forn(j, n) cout << (ar2[j]?'+':'-');
            //~ cout << endl;
            q++;
        }
    }
    return q;
}

int brute(){
    int b=-1;
    int in=0;
    forn(i, n) if(ar[i]) in|=1<<i;
    
    forn(bm, 1<<(n-k+1)){
        int st=in;
        forn(i, n-k+1) if(bm&(1<<i)){
            forr(j, i, i+k){
                st^=1<<j;
            }
        }
        
        if(st==(1<<n)-1){
            int q=__builtin_popcount(bm);
            if(b==-1) b=q;
            else b=min(b, q);
        }
    }
    return b;
}

void solve(){
    cin >> s >> k;
    n=sz(s);
    
    //~ n=RND(1, 25);
    //~ s.resize(n);
    //~ forn(i, n) s[i]=RND(0, 1)? '+':'-';
    //~ k=RND(1, n);
    //~ cout << s << ' ' << k << endl;
    
    forn(i, n) ar[i]=s[i]=='+';
    int q=greedy();
    //~ int qb=brute();
    //~ if(q!=qb){ dprint(q);
    //~ dprint(qb);}
    //~ assert(q==qb);
    if(q==-1) cout << "IMPOSSIBLE";
    else cout << q;
}


int main() {
    freopen("A-large.in", "r", stdin);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    forr(TCC, 1, TC+1){
    //~ for(int TCC=1; ; TCC++){
        cout << "Case #" << TCC << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
