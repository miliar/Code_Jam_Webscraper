#include <bits/stdc++.h>
using namespace std;
#define md int(1600)
#define inf int(1e9+100)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b ;i++)
#define DOW(i,b,a) for(int i=(b),_a=(a); i>=_a ;i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define pii pair<int,int>
#define ll long long

int xx[4]={0,0,1,-1};
int yy[4]={1,-1,0,0};
char c[4];
int a[md][md],b[md][md];
int n,m;


int main()
{
    //freopen("inp.txt","r",stdin);
    freopen("D-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tcase;
    scanf("%d",&tcase);
    c[1]='+'; c[2]='x'; c[3]='o';
    FOR(o,1,tcase)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%d%d",&n,&m);
        FOR(i,1,m)
        {
            char s[5];
            int x,y;
            scanf("%s",s);
            scanf("%d%d",&x,&y);
            FOR(j,1,3)
            if (s[0]==c[j])
            {
                a[x][y]=j;
                b[x][y]=j;
            }
        }
        int vt=0;
        FOR(j,1,n)
        if (a[1][j]==0) a[1][j]=1;
        else if (a[1][j]==2) { a[1][j]=3; vt=j; }
        else if (a[1][j]==3) vt=j;

        if (vt==0) {vt=1; a[1][1]=3;}

        FOR(j,2,n-1)
        a[n][j]=1;

        FOR(i,2,n)
        if (i!=vt) a[i][i]=2;
        else a[i][1]=2;

        int cnt=0,res=0;
        FOR(i,1,n)
        FOR(j,1,n)
        {
            if (a[i][j]==1 || a[i][j]==2) res+=1;
            if (a[i][j]==3) res+=2;

            if (a[i][j]!=b[i][j]) cnt++;
        }

        printf("Case #%d: %d %d\n",o,res,cnt);

        FOR(i,1,n)
        FOR(j,1,n)
        if (a[i][j]!=b[i][j])
            printf("%c %d %d\n",c[a[i][j]],i,j);


    }
}
