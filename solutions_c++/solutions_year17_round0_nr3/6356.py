#include<bits/stdc++.h>
using namespace std;
//custom
#define endl ('\n')
#define space (" ")
#define __ ios_base::sync_with_stdio(false);cin.tie(0);
//utils
#define SET(a,b) (memset(a,b,sizeof(a)))
//for vectors
#define pb push_back
#define mp make_pair
typedef vector<int> vi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
//data types
typedef long long ll;
typedef long long LL;
//loops
#define REP(i,a,b) \
    for(int i = int(a);i <= int(b);i++)
#define MEMSET_INF 127 //2bill
#define MEMSET_HALF_INF 63 //1bill

#ifdef DEBUG
    #define debug(args...) {dbg,args; cerr<<endl;}
    #define _
#else
    #define debug(args...)  // Just strip off all debug tokens
    #define _ ios_base::sync_with_stdio(false);cin.tie(0);
#endif 
struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

const int mod = 1000000007;
inline void add(int &x, int y){x+=y; if(x>=mod)x-=mod; if(x<0)x+=mod;}
inline int mul(int x, int y){ return ((LL)x * y)%mod;}
int gcd(int a, int b){ if(b)return gcd(b,a%b); return a;}
int power(int a ,int p){int ret = 1; while(p){if(p&1)ret=mul(ret,a); a=mul(a,a); p/=2;}return ret;}
int phi(int n){ int ret=n; int i = 2; 
    if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    for(i=3; i*i<=n; i++)if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    if(n>1)ret-=ret/n;return ret;
}

const int maxn = 2001000;
const long long INF = 2000000000000000000LL;
long long n;
long long pos[maxn];

struct segment {
    long long l, r;
    segment(long long _L, long long _R){
        l = _L;
        r = _R;
    }

    long long bestPos(){
        long long ans = (l + r) / 2;
        if (ans <= 0){
            ans = 1;
        }
        if (ans > n) ans = n;
        return ans;
    }

    pair<ll, ll> bestLen(){
        if (r - l <= 1){
            return {-1e6, -1e6};
        }
        // debug("bestPos: ", bestPos(), l, r);
        return {min(bestPos() - l, r - bestPos()), max(bestPos() - l, r - bestPos())};
    }

    // long long max_right{
    //     if (r - l + 1 <= 2){
    //         return -1000000;
    //     }
    //     return max(bestPos() - l, r - bestPos());
    // }
};

//magic happens here, pos should be min with len as max
bool operator<(segment y, segment x)
{   
    pair<ll, ll> ybl = y.bestLen();
    pair<ll, ll> xbl = x.bestLen();
    // debug("<: ", ybl.first, ybl.second, xbl.first, xbl.second);
    // return ybl.first > xbl.first ? 1 : ybl.second > xbl.second ? 1 : y.bestPos() < x.bestPos();
    // return make_pair(-ybl, -y.max_right()) < make_pair(-xbl, -x.max_right())? 1 : y.bestPos() < x.bestPos();
    return make_pair(-ybl.first, make_pair(-ybl.second, y.bestPos())) < make_pair(-xbl.first, make_pair(-xbl.second, x.bestPos()));
}

struct forRemSeg {
    long long L, R;
    forRemSeg(long long _L, long long _R){
        L = _L;
        R = _R;
    }
};

bool operator < (forRemSeg x, forRemSeg y){
    return x.L < y.L;
}

//segs operator is now overloaded, so ordering is acc to our wish
set< segment > segs;
set< forRemSeg > seg1;

void add(long long l, long long r){
    segs.insert(segment(l, r));
    seg1.insert(forRemSeg(l, r));
}

void rem(long long l, long long r){
    // debug("removing: ", l, r);
    // auto it = segs.find(segment(l, r));
    // if(it == segs.end())
    //     debug("not able to find")
    segs.erase(segment(l, r));
    seg1.erase(forRemSeg(l, r));
}

void insert(long long x){
    segment Best = *segs.begin();
    pos[x] = Best.bestPos();

    // debug("insert: ", x, pos[x], Best.l, Best.r)

    rem(Best.l, Best.r);
    add(Best.l, pos[x]);
    add(pos[x], Best.r);

    return;
}

int main(){
    _
    int t;
    cin>>t;
    REP(t1, 1, t){
        segs.clear();
        seg1.clear();
        SET(pos, 0);
        ll k;
        cin>>n>>k;
        n += 2;

        add(-INF, INF);
        // add(1, n+2);

        insert(1);
        insert(n);
        // debug(pos[1], pos[n]);

        ll id = 2;
        for(; id <= k+1; id++){
            // cout << "start :\n";
            // for(auto it: segs)
            //     cout << it.l << space << it.r << endl;
            // cout << "end :\n";
            insert(id);
            // debug(id, pos[id]);
        }

        ll Position = pos[k+1];

        set< forRemSeg >::iterator it = seg1.lower_bound(forRemSeg(Position, -1));
        forRemSeg rR = *it;
        it--;
        forRemSeg lL = *it;

        ll left = lL.L;
        ll right = rR.R;

        debug(lL.L, lL.R, rR.L, rR.R, Position);

        ll ls = Position - left - 1;
        ll rs = right - Position - 1;

        cout << "Case #" << t1 << ": " << max(ls, rs) << space << min(ls, rs) << endl;


    }
    return 0;
}
