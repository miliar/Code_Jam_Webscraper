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
int t,n,m;
scanf("%d",&t);
REP(i,t)
{
    string cad;
    scanf("%d %d",&n,&m);
    vector<string>arr;
    REP(j,n)
    {
        cin>>cad;
        arr.PB(cad);
    }
    char temp;
    REP(j,n)
    {
        bool band=true;
        REP(k,m)
        {
            if(band==true&&arr[j][k]!='?')
            {
                band=false;
                if(k!=0)
                {
                    temp=arr[j][k];
                    RFOR(l,k,0)
                        arr[j][l]=temp;
                }
            }
            if(arr[j][k]!='?')
            {
                temp=arr[j][k];
                int k2=k+1;
                while(k2<m&&arr[j][k2]=='?')
                {
                    arr[j][k2]=temp;
                    k2++;
                }
                k=k2-1;
            }
        }
    }
    REP(k,m)
    {
        bool band=true;
        REP(j,n)
        {

            if(band==true&&arr[j][k]!='?')
            {
                band=false;
                if(j!=0)
                {
                    temp=arr[j][k];
                    RFOR(l,j,0)
                        arr[l][k]=temp;
                }
            }
            if(arr[j][k]!='?')
            {
                temp=arr[j][k];
                int j2=j+1;
                while(j2<n&&arr[j2][k]=='?')
                {
                    arr[j2][k]=temp;
                    j2++;
                }
                j=j2-1;
            }

        }
    }
    printf("Case #%d:\n",i+1);
    REP(j,n)
        cout<<arr[j]<<endl;
}
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


