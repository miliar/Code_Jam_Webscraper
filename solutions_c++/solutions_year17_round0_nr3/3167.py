//AUTOR:MURRUGARRA JEFFRI ERWIN
//UNIVERSIDAD: UNIVERSIDAD NACIONAL DE TRUJILLO
#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i (1<<31)-1

int main(){
/*
   freopen("C-large.in", "r", stdin);
   freopen("C-large.txt", "w", stdout);
*/
int n,web=1;
scanf("%d",&n);
REP(i,n)
{
    lli s,p;
    scanf("%lld %lld",&s,&p);
    map<lli,lli>m;
    queue<lli>q;
    q.push(s);
    m[s]++;
    lli suma=0;
    while(suma+m[q.front()]<p)
    {
        lli tope=q.front();
        suma+=m[tope];
        lli val=tope-1;
        if(val%2==0)
        {
            lli val2=val/2;
            if(m.count(val2)<=0)
            q.push(val2);
            m[val2]+=(2*m[tope]);
        }
        else
        {
            lli val3=val/2,val4=val3+1;
            if(m.count(val4)<=0)
            q.push(val4);
            if(m.count(val3)<=0)
            q.push(val3);
            m[val3]+=m[tope];
            m[val4]+=m[tope];
        }
        q.pop();
    }
    lli res=q.front()-1,res2,res3;
    if(res%2==0)
    {
        res2=(res/2);
        res3=(res/2);
    }
    else
    {
        res2=res/2;
        res3=(res/2)+1;
    }

    printf("Case #%d: %lld %lld\n",web++,res3,res2);
}
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


