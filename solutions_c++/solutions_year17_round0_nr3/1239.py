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

void solve(int test){

    long long n,k;
    cin >> n >> k;

    map<long long,long long>a;
    priority_queue<long long>q;

    a[n]++;
    q.push(n);

    P("Case #%d: ",test);

    while(!q.empty())
    {
        long long x = q.top();
        q.pop();

        if(k <= a[x])
        {
            P("%I64d %I64d\n",x/2,(x-1)/2);
            return;
        }

        else
        {
            k -= a[x];
            if(!a.count(x/2)) q.push(x/2);
            a[x/2] += a[x];
            if(!a.count((x-1)/2)) q.push((x-1)/2);
            a[(x-1)/2] += a[x];
        }

    }

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
