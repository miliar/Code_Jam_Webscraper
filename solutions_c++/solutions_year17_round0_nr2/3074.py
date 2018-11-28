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
   freopen("B-large.in", "r", stdin);
   freopen("B-large.txt", "w", stdout);
*/
int n;
scanf("%d",&n);
int web=1;
REP(i,n)
{
    char cad[20];
    cin>>cad;
    int tam=strlen(cad);
    int val=cad[0]-'0';
    bool band=true;
    FOR(j,1,tam)
    {
        int val2=cad[j]-'0';
        if(val<=val2)
            val=val2;
        else
            band=false;
        if(band==false)
        {
            int k=j;
            bool flag=true;
            while(k!=0&&cad[k]<cad[k-1])
            {
                if(flag)
                {
                    k--;
                    flag=false;
                }
                while(cad[k]=='0')
                    k--;
                cad[k]=cad[k]-1;
            }
            int k2=k+1;
            FOR(k3,k2,tam)
                cad[k3]='9';
            break;
        }
    }
    lli temp;
    sscanf(cad,"%lld",&temp);
    printf("Case #%d: %lld\n",web++,temp);
}
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


