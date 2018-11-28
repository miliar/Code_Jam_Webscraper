#include <bits/stdc++.h>
using namespace std;

#define fi          "input.txt"
#define fo          "output.txt"
#define fe          ""
#define fileopen    freopen(fi,"r",stdin);freopen(fo,"w",stdout);freopen(fe,"w",stderr)

#define FOR(i,a,b)  for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n)    for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)

#define xy          pair<int64,int>
#define int64       long long
#define ld          long double
#define vi          vector<int>
#define vxy         vector<xy>
#define vi64        vector<int64>

#define X           first
#define Y           second
#define pb          push_back
#define init(a,v)   memset(a,v,sizeof(a))
#define Sz(s)       (int)(s.size())
#define EL          cout<<endl
#define digit(x)    ('0'<=x&&x<='9')
#define ran(l,r)    ((1LL*rand()*rand())%((int)(r)-(int)(l)+1)+(int)(l))

#define prec(n)     fixed<<setprecision(n)

#define bit(n, i)   (((n) >> (i)) & 1)
#define bitcount(n) __builtin_popcountll(n)

#define db(x)       cerr << #x << " = " << (x) << ", ";
#define endln       cerr << "\n";
#define chkpt       cerr << "-----\n";

#define stop(t)     if (test==t) cerr<<"\n========Test "<<test<<"========\n"; else {cout<<"\n";return;}

const int OO = (int) 2e9+5;
const int64 OO64 = (int64) 1e18+5;
const int MOD = (int) 1e9+7;
const long double Pi = acos((long double) -1);
const int N = (int) 1e2+5;

int dp[N][N][N],cnt[N],a[N],n,p;

int solve2() {
    return cnt[1]/2+(cnt[1]%2);
}

int solve3() {
    dp[0][0][0] = 0;
    FOR(i,0,cnt[1]) FOR(j,0,cnt[2]) {
        if (i==j && j==0) continue;
        if (i>0 && j>0) dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][0]+1);
        if (i>2) dp[i][j][0] = max(dp[i][j][0], dp[i-3][j][0]+1);
        if (j>2) dp[i][j][0] = max(dp[i][j][0], dp[i][j-3][0]+1);
    }
    int res = 0;
    FOR(i,0, cnt[1]) FOR(j,0,cnt[2]) {
        res = max(res, dp[i][j][0]+(i<cnt[1]||j<cnt[2]));
    }
    return res;
}

int solve4() {
    dp[0][0][0] = 0;
    int d[100][4],b[100][4],m=0,m2=0;
    FOR(i1,0,4) FOR(i2,0,4) FOR(i3,0,4) {
        if ((i1+i2*2+i3*3)%4==0 && i1+i2+i3>0) {
            d[++m][1]=i1;
            d[m][2]=i2;
            d[m][3]=i3;
        }
    }
    FOR(i,1,m) {
        db(d[i][1])
        db(d[i][2])
        db(d[i][3])
        endln;
    }
    bool choose[100];
    init(choose,true);
    FOR(i,1,m) FOR(j,i+1,m) {
        if (d[i][1]<=d[j][1] && d[i][2]<=d[j][2] && d[i][3]<=d[j][3])
            choose[j]=false;
    }
    FOR(i,1,m) if (choose[i]) {
        m2++;
        b[m2][1] = d[i][1];
        b[m2][2] = d[i][2];
        b[m2][3] = d[i][3];
    }
    m = m2;
    chkpt;
    FOR(i,1,m) {
        db(b[i][1])
        db(b[i][2])
        db(b[i][3])
        endln;
    }
    FOR(i,0,cnt[1]) FOR(j,0,cnt[2]) FOR(k,0,cnt[3]) {
        if (i==j && j==0 && k==0) continue;
        FOR(t,1,m) if (i>=b[t][1] && j>=b[t][2] && k>=b[t][3]) {
            dp[i][j][k] = max(dp[i][j][k], dp[i-b[t][1]][j-b[t][2]][k-b[t][3]]+1);
        }
    }
    int res = 0;
    FOR(i,0, cnt[1]) FOR(j,0,cnt[2]) FOR(k,0,cnt[3]) {
        res = max(res, dp[i][j][k]+(i<cnt[1]||j<cnt[2]||k<cnt[3]));
    }
    return res;
}

void solve(int test) {
    int bn = 0;
    init(dp,0);
    init(cnt,0);
    cin>>n>>p;
    FOR(i,1,n) cin>>a[i];
    FOR(i,1,n) {
        bn+=(a[i]%p==0);
        cnt[a[i]%p]++;
    }
//    stop(3);
    if (p==2) cout<<solve2()+bn<<endl;
    if (p==3) cout<<solve3()+bn<<endl;
    if (p==4) cout<<solve4()+bn<<endl;
}

int main() {
    fileopen;
    int T;cin>>T;
    FOR(t,1,T) {
        cout<<"Case #"<<t<<": ";
        solve(t);
    }
}
