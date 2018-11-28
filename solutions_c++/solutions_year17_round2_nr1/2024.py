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
#define fi first
#define si second
#define vi vector<int>
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

int A[MAX + 100], B[MAX+100];

double calc(int st, int ed, int v)
{
    double s=(ed-st);
    double tm=(s/v);
    return tm;
}

int main()
{
    read();
    write();
    cpp_io();
    cout << fixed << setprecision(10);
    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        int d, n;
        cin >> d >> n;
        FOR(i, n) cin >> A[i] >> B[i];
        double tm=0;
        for(int i=n-1; i>=0; i--){
            tm=max(calc(A[i], d, B[i]), tm);
        }
        double ans=d/tm;
        cout << FMT("Case #%d: ", cs) << ans << "\n";
    }
    return 0;
}





