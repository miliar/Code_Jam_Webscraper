/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include <bits/stdc++.h>
using namespace std;
#define REP(i,FN) for(int i=0;i<FN;i++)
#define FOR(i,ST,FN) for(int i=ST;i<=FN;i++)
#define FORD(i,FN,ST) for(int i=FN;i>=ST;i--)
#define FORX(i,c) for(typeof(c.begin())i=c.begin();i!=c.end();i++)
#define pause system("pause")
#define S scanf
#define P printf
#define X first
#define Y second
#define pb push_back
#define PII pair<int,int>
#define mp make_pair
#define sz size()
#define eps 1e-8

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN(2005);

int a[MAXN], d[3], c[3];

char f(int x){
    if(x == 0) return 'R';
    if(x == 1) return 'Y';
    if(x == 2) return 'B';
}

void solve(int test){

    int n,r,o,y,g,b,v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    P("Case #%d: ",test);

    REP(i,2*n)
        a[i] = -1;

    if(r >= y && r >= b)
    {
        if(y+b < r) { P("IMPOSSIBLE\n"); return; }
        d[0] = 0;
        d[1] = 1;
        d[2] = 2;
    }

    else if(y >= r && y >= b)
    {
        if(r+b < y) { P("IMPOSSIBLE\n"); return; }
        d[0] = 1;
        d[1] = 0;
        d[2] = 2;
    }

    else if(b >= r && b >= y)
    {
        if(r+y < b) { P("IMPOSSIBLE\n"); return; }
        d[0] = 2;
        d[1] = 0;
        d[2] = 1;
    }

    c[0] = r, c[1] = y, c[2] = b;

    REP(i,c[d[0]])
    {
        a[i*3] = d[0];
        if(c[d[1]] > 0) a[i*3+1] = d[1], c[d[1]]--;
        else a[i*3+1] = d[2], c[d[2]]--;
    }

    REP(i,c[d[2]])
        a[i*3+2] = d[2];

    REP(i,c[d[0]])
    {
        if(a[i*3] != -1) P("%c",f(a[i*3]));
        if(a[i*3+1] != -1) P("%c",f(a[i*3+1]));
        if(a[i*3+2] != -1) P("%c",f(a[i*3+2]));
    }

    P("\n");

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
