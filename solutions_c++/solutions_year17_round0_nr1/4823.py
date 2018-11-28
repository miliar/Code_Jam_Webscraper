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

int A[MAX + 100];

int main()
{
    read();
    write();
    cpp_io();

    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        string str;
        int k;
        cin >> str >> k;
        int N=str.length();
        int cnt=0, ans=0;
        FOR(i, N) A[i]=(str[i]=='+');
        FOR(i, N-k+1){
            if(!A[i]){
                FOR(j, k) A[i+j]^=1;
                ans++;
            }
        }
        FOR(i, N) if(!A[i]) ans=-1;
        if(ans!=-1)
            cout << FMT("Case #%d: %d", cs, ans) << "\n";
        else
            cout << FMT("Case #%d: IMPOSSIBLE", cs) << "\n";
    }
    return 0;
}





