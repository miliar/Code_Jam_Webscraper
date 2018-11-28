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

struct Rect{
    char ch;
    int x1, y1, x2, y2;
    Rect(){}
    Rect(char ch, int x1, int y1, int x2, int y2){
        this->ch=ch;
        this->x1=x1, this->x2=x2;
        this->y1=y1, this->y2=y2;
    }
};

char A[100][100];

void do_fill(char ch, int x1, int y1, int x2, int y2)
{
    FORR(i, x1, x2+1)
        FORR(j, y1, y2+1)
            A[i][j]=ch;
}

bool check(char ch, int x1, int y1, int x2, int y2)
{
    if(x1<0||y1<0) return false;
    FORR(i, x1, x2+1)
        FORR(j, y1, y2+1)
            if(A[i][j]!=ch&&A[i][j]!='?')
                return false;
    return true;
}

void func(Rect &r, int x1, int y1, int x2, int y2)
{
    do_fill(r.ch, x1, y1, x2, y2);
    r=Rect(r.ch, x1, y1, x2, y2);
}

int main()
{
    read();
    write();
    cpp_io();
    int TC;
    cin >> TC;
    FORR(cs, 1, TC+1){
        MEM(A, 0);
        map<char, vector<pii> > POS;
        int n, m;
        cin >> n >> m;
        FOR(i, n) FOR(j, m) cin >> A[i][j];
        FOR(i, n) FOR(j, m) POS[A[i][j]].pb({i, j});
//        cout << FMT("Case #%d:\n", cs);
//        FOR(i, n){
//            FOR(j, m) cout << A[i][j];
//            cout << "\n";
//        }
        vector<Rect> vec;
        for(auto it: POS){
            if(it.fi=='?') continue;
            int x1, y1, x2, y2;
            tie(x1, y1)=it.si[0];
            tie(x2, y2)=it.si[0];
            for(auto p: it.si){
                if(p.fi<x1)x1=p.fi;
                if(p.si<y1)y1=p.si;
                if(p.fi>x2)x2=p.fi;
                if(p.si>y2)y2=p.si;
            }
            do_fill(it.fi, x1,y1, x2, y2);
            vec.pb(Rect(it.fi, x1, y1, x2, y2));
        }
        for(auto &r: vec){
            while(check(r.ch, r.x1,  r.y1,   r.x2,   r.y2+1))
                   func(r,    r.x1,  r.y1,   r.x2,   r.y2+1);
        }
        for(auto &r: vec){
            while(check(r.ch, r.x1,  r.y1-1, r.x2,   r.y2))
                   func(r,    r.x1,  r.y1-1, r.x2,   r.y2);
        }
        for(auto &r: vec){
            while(check(r.ch, r.x1,  r.y1,   r.x2+1, r.y2))
                   func(r,    r.x1,  r.y1,   r.x2+1, r.y2);
        }
        for(auto &r: vec){
            while(check(r.ch, r.x1-1,r.y1,   r.x2,   r.y2))
                   func(r,    r.x1-1,r.y1,   r.x2,   r.y2);

        }
        cout << FMT("Case #%d:\n", cs);
        FOR(i, n){
            FOR(j, m) cout << A[i][j];
            cout << "\n";
        }
    }
    return 0;
}





