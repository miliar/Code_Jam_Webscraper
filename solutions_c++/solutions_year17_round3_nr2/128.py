#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define rep1(i,n) for(int i = 1; i < n; i++)
#define repv(i,n) for(int i = n-1; i >= 0; i--)
#define fi first
#define sc second
#define pb push_back
using namespace std;
typedef long long ll;

char BUF[3500000];
inline void I(int&a){scanf("%d",&a);}
inline void I(int&a,int&b){scanf("%d%d",&a,&b);}
inline void I(int&a,int&b,int&c){scanf("%d%d%d",&a,&b,&c);}
inline void I(int&a,int&b,int&c,int&d){scanf("%d%d%d%d",&a,&b,&c,&d);}
inline void L(ll&a){scanf("%lld",&a);}
inline void L(ll&a,ll&b){scanf("%lld%lld",&a,&b);}
inline void L(ll&a,ll&b,ll&c){scanf("%lld%lld%lld",&a,&b,&c);}
inline void L(ll&a,ll&b,ll&c,ll&d){scanf("%lld%lld%lld%lld",&a,&b,&c,&d);}
inline void S(string&str){str.clear();scanf("%s",BUF);int s=strlen(BUF);rep(i,s)str.pb(BUF[i]);}
inline void SV(vector<int>&v){v.clear();scanf("%s",BUF);int s=strlen(BUF);rep(i,s)if('a'<=BUF[i]&&BUF[i]<='z')v.pb(BUF[i]-'a');else v.pb(BUF[i]-'A');}

const auto EPS = 1e-10;
const auto INF = 100000000;
const auto MOD = 1000000007;
typedef pair<int,int> P;

int n, m;
int table[1440];

struct B{
    int st, en;
    int len;
    bool operator<( const B& right) const {
        return len < right.len;
    }
};


void solve(){
    int fa = 0, mo = 0;
    P fch[1000], mch[1000];
    vector<B> ff, mm;
    //vector<int> ff, mm;
    cin >> n >> m;
    memset(table,0,sizeof(table));
    rep(i,n){
        cin >> fch[i].first >> fch[i].second;
        for(int j = fch[i].first; j < fch[i].second; j++) table[j] = 1;
        fa += fch[i].second-fch[i].first;
    }
    rep(i,m){
        cin >> mch[i].first >> mch[i].second;
        for(int j = mch[i].first; j < mch[i].second; j++) table[j] = 2;
        mo += mch[i].second-mch[i].first;
    }
    sort(fch,fch+n);
    sort(mch,mch+m);
    rep(i,n){
        int st = fch[i].second-1;
        int counter = -1;
        while(true){
            st++;
            if(st == 1440) st = 0;
            counter++;
            if(table[st] == 1){
                B tmp;
                tmp.st = fch[i].second;
                tmp.en = st;
                tmp.len = counter;
                ff.push_back(tmp);
                break;
            } else if(table[st] == 2){
                break;
            }
        }
    }
    rep(i,m){
        int st = mch[i].second-1;
        int counter = -1;
        while(true){
            counter++;
            st++;
            if(st == 1440) st = 0;
            if(table[st] == 2){
                B tmp;
                tmp.st = mch[i].second;
                tmp.en = st;
                tmp.len = counter;
                mm.push_back(tmp);
                break;
            } else if(table[st] == 1){
                break;
            }
        }
    }
    sort(ff.begin(),ff.end());
    sort(mm.begin(),mm.end());
    rep(i,ff.size()){
        int pos = ff[i].st;
        if(pos == 1440) pos = 0;
        rep(j,ff[i].len){
            if(fa == 720) break;
            table[pos] = 1;
            fa++;
            pos++;
            if(pos == 1440) pos = 0;
        }
    }
    rep(i,mm.size()){
        int pos = mm[i].st;
        if(pos == 1440) pos = 0;
        rep(j,mm[i].len){
            if(mo == 720) break;
            table[pos] = 2;
            mo++;
            pos++;
            if(pos == 1440) pos = 0;
        }
    }
    if(fa != 720 && mo != 720){
        rep(i,1440) if(table[i] == 0) table[i] = 1;
    } else if(fa == 720){
        rep(i,1440) if(table[i] == 0) table[i] = 2;
    } else if(mo == 720){
        rep(i,1440) if(table[i] == 0) table[i] = 1;
    }
    int ans = 0;
    for(int i = 0; i < 1440; i++){
        if(table[i] != table[(i+1)%1440]){
            ans++;
        }
    }
    cout << ans << endl;
}

int main(){
    int T;
    cin >> T;
    rep(i,T){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
