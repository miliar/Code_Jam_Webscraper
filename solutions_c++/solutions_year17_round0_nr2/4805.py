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
#define MOD 1000000007
#define MAX 200000
#define pb push_back
#define mkpr make_pair
#define pii pair<int, int>
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

int N;
int dp[20][20][2];
int A[MAX + 100];

int func(int p, int prev, int tight)
{
    if(p==N) return true;
    int &ret=dp[p][prev][tight];
    if(ret!=-1) return ret;
    int st=prev;
    int ed=9;
    if(tight) ed=A[p];
    ret=false;
    FORR(i, st, ed+1){
        ret |= func(p+1, i, tight&&(i==ed));
    }
    return ret;
}

int main()
{
    read();
    write();
    //cpp_io();

    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        MEM(dp, -1);
        string str;
        cin >> str;
        N=str.length();
        FOR(i, N) A[i]=str[i]-'0';
        func(0, 0, true);
        int p=0, prev=0, tight=true;
        cout << FMT("Case #%d: ", cs);
        while(p<N){
            //dbg(cs, p);
            int st=prev;
            int ed=9;
            if(tight) ed=A[p];
            int np, nprev, ntight;
            FORR(i, st, ed+1){
                if(func(p+1, i, tight&&(i==ed))){
                    np=p+1, nprev=i, ntight=tight&&(i==ed);
                }
            }
            if(nprev) cout << nprev;
            p=np, prev=nprev, tight=ntight;
        }
        cout << "\n";
    }
    return 0;
}





