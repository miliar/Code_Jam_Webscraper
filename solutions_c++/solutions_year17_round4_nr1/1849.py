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
const int MAXN(105);

int a[MAXN];

void solve(int test){

    int n,p;
    S("%d%d",&n,&p);
    REP(i,n)
        S("%d",&a[i]);

    int ans = 0;

    if(p == 2)
    {
        REP(i,n)
            a[i] %= p;

        sort(a,a+n);

        int now = 0;

        REP(i,n)
        {
            if(now == 0) ans++;
            now = (now+a[i])%p;
        }
    }

    else if(p == 3)
    {
        int num1 = 0, num2 = 0;

        REP(i,n)
        {
            if(a[i]%p == 0) ans++;
            else if(a[i]%p == 1) num1++;
            else if(a[i]%p == 2) num2++;
        }

        while(num1 > 0 && num2 > 0)
        {
            ans++;
            num1--;
            num2--;
        }

        int now = 0;

        while(num1 > 0 || num2 > 0)
        {
            if(now == 0) ans++;
            if(num1 > 0) now = (now+1)%p, num1--;
            else now = (now+2)%p, num2--;
        }

    }

    else if(p == 4)
    {
        int num1 = 0, num2 = 0, num3 = 0;

        REP(i,n)
        {
            if(a[i]%p == 0) ans++;
            else if(a[i]%p == 1) num1++;
            else if(a[i]%p == 2) num2++;
            else if(a[i]%p == 3) num3++;
        }

        while(num1 > 0 && num3 > 0)
        {
            ans++;
            num1--;
            num3--;
        }

        while(num2 >= 2)
        {
            ans++;
            num2 -= 2;
        }

        if(num2 == 1 && num1 >= 2)
        {
            ans += 2;
            num1 -= 2;
            num2--;
        }

        if(num2 == 1 && num3 >= 2)
        {
            ans += 2;
            num3 -= 2;
            num2--;
        }

        int now = 0;

        while(num1 > 0 || num3 > 0)
        {
            if(now == 0) ans++;
            if(num1 > 0) now = (now+1)%p, num1--;
            else now = (now+3)%p, num3--;
        }

        while(num2 > 0)
        {
            if(now == 0) ans++;
            now = (now+2)%p;
            num2--;
        }

    }

    P("Case #%d: %d\n",test,ans);

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
