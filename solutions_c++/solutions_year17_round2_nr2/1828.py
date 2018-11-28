#include <bits/stdc++.h>

using namespace std;

/* Template Begins */

#define FOR(i,N) FORR(i, 0, N)
#define FORR(i,a,b) FOTR(i, a, b, 1)
#define FOTR(i,a,b,c) for(int i=(a);i<(b);i+=(c))
#define FOREACH(it, x) for(__typeof__((x).begin()) it=(x).begin();it!=(x).end();it++)
#define MEM(a,x) memset(a,x,sizeof(a))
#define BCHK(a,x) (((a)>>(x))&1)
#define BSET(a,x) ((a)|(1<<(x)))
#define BCLR(a,x) ((a)&(~(1<<(x))))
#define BTGL(a,x) ((a)^(1<<(x)))
#define FMT(...) (sprintf(CRTBUFF, __VA_ARGS__)?CRTBUFF:0)
#define read() freopen("input.txt","r",stdin)
#define write() freopen("output.txt","w",stdout)
#define cpp_io() {ios_base::sync_with_stdio(false);cin.tie(NULL);}
#define BUFFSIZE 30000
#define INF 1000000000
#define MOD 1000000009
#define MAX 200000
#define BASE 1000000007
#define pb push_back
#define mkpr make_pair
#define pii pair<int, int>
#define fi first
#define si second
typedef long long ll;

char CRTBUFF[BUFFSIZE];

#define dbg(args...) {cout<<"-->";debugger::call(#args,args);cout<<"\n";}
struct debugger{
    static void call(const char* it){}
    template<typename T, typename ... aT>
    static void call(const char* it, T a, aT... rest){
        string b;
        for(;*it&&*it!=',';++it) if(*it!=' ')b+=*it;
        cout<<b<<"="<<a<<" ";
        call(++it, rest...);
    }
};

/* Template Ends */

struct State{
    short n;
    short CL[6];
    short prev, first;
    bool operator<(const State &B) const{
        if(n==B.n){
            //dbg(n, prev, B.prev);
            if(prev==B.prev){
                if(first==B.first){
                    FOR(j, 6){
                        if(CL[j]!=B.CL[j])
                            return CL[j]<B.CL[j];
                    }
                }
                return first<B.first;
            }
            return prev<B.prev;
        }
        return n<B.n;
    }

    void print() const{
        dbg(n, prev, first);
        FOR(j, 6) dbg(j, CL[j]);
    }
};

unordered_map<ll, int> dp;

bool check(State &S, int j)
{
    return (j!=S.prev&&(S.n!=1||j!=S.first)&&S.CL[j]);
}

ll get_hash(State &S)
{
    ll ret=0;
    ret=ret*BASE+S.n;ret%=MOD;
    ret=ret*BASE+S.prev;ret%=MOD;
    ret=ret*BASE+S.first;ret%=MOD;
    FOR(j, 6)
        ret=ret*BASE+S.CL[j];ret%=MOD;
    return ret;
}

bool func(State S)
{
    if(S.n==0) return true;
    ll hsh=get_hash(S);
    if(dp.count(hsh)) return (dp[hsh]!=-1);
    bool can=false;
    dp[hsh]=-1;
    FOR(j, 6){
        if(check(S, j)){
            State K=S;
            K.CL[j]--, K.n--, K.prev=j;
            if(K.first==-1)K.first=j;
            can|=func(K);
            if(can){
                dp[hsh]=j;
                break;
            }
        }
    }
    return can;
}

int A[MAX + 100];

int main()
{
    read();
    write();
    map<int, char>MCOL;
    MCOL[0]='R';
    MCOL[1]='O';
    MCOL[2]='Y';
    MCOL[3]='G';
    MCOL[4]='B';
    MCOL[5]='V';
    cpp_io();
    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        dp.clear();
        State S;
        cin >> S.n;
        FOR(i, 6) cin >> S.CL[i];
        S.prev=S.first=-1;
        bool can=func(S);
        cout << FMT("Case #%d: ", cs);
        if(can){
            State K=S;
            while(K.n){
                ll hsh=get_hash(K);
                int j=dp[hsh];
                cout << MCOL[j];
                K.CL[j]--, K.n--, K.prev=j;
                if(K.first==-1)K.first=j;
            }
        }
        else{
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }

    return 0;
}






