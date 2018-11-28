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
const int MAXN();

int gen(string t){

    int ret = 0;

    REP(i,t.sz)
    {
        if(t[i] != '.')
            ret = ret*10 + (t[i]-'0');
    }

    return ret;

}

void solve(int test){

    int n,k;
    S("%d%d",&n,&k);

    multiset<int>s;

    string u;
    cin >> u;

    int U = gen(u);

    REP(i,n)
    {
        string x;
        cin >> x;
        int num = gen(x);
        s.insert(num);
    }

    while(U--)
    {
        int num = *s.begin();
        s.erase(s.begin());
        s.insert(num+1);
    }

    double p = 1.0;

    while(!s.empty())
    {
        int num = *s.begin();
        p = p*(num*0.0001);
        s.erase(s.begin());
    }

    P("Case #%d: %.10f\n",test,p);

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
