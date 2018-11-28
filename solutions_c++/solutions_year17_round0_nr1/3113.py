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
   freopen("A-large.in", "r", stdin);
   freopen("A-large.txt", "w", stdout);
*/
int n;
scanf("%d",&n);
int web=1;
REP(i,n)
{
    int num;
    string cad;
    cin>>cad;
    scanf("%d",&num);
    int t = cad.size();
    int cont=0;
    REP(j,t-num+1)
    {
        if(cad[j]=='-')
        {
            cont++;
            int l=j+num;
            FOR(k,j,l)
                cad[k]=(cad[k]=='-')?'+':'-';
        }
    }
    int p=t-num;
    bool band=true;
    FOR(j,p,t)
        (cad[j]=='+')?band&=1:band&=0;

    if(!band)
        printf("Case #%d: IMPOSSIBLE\n",web++);
    else
        printf("Case #%d: %d\n",web++,cont);
}
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


