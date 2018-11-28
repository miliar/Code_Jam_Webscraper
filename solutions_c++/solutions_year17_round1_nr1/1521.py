//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define sc1(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d %d",&a,&b)
#define sc3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define scd1(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf %lf",&a,&b)
#define scd3(a,b,c) scanf("%lf %lf %lf",&a,&b,&c)
#define scl1(a) scanf("%lld",&a)
#define scl2(a,b) scanf("%lld %lld",&a,&b)
#define scl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
//#define scl1(a) scanf("%I64d",&a)
//#define scl2(a,b) scanf("%I64d %I64d",&a,&b)
//#define scl3(a,b,c) scanf("%I64d %I64d %I64d",&a,&b,&c)


#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;

using namespace std;
typedef long long int ll;
const ll mod=1000000000 + 7;

char gd[101][101];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.in", "w", stdout);

    int t, T;
    int r, c;
    sc1(t);
    T=t;
    while(t--)
    {
        sc2(r,c);
        for(int i=0; i<r; i++)
        {
            scanf("%s", &gd[i]);
            for(int j=0; j<c; j++)
            {
                if(gd[i][j]!='?')
                {
                    char chr=gd[i][j];
                    j++;
                    while(j<c && gd[i][j]=='?')
                        gd[i][j]=chr, j++;
                    j--;
                }
            }

            for(int j=c-1; j>=0; j--)
            {
                if(gd[i][j]!='?')
                {
                    char chr=gd[i][j];
                    j--;
                    while(j>=0 && gd[i][j]=='?')
                        gd[i][j]=chr, j--;
                    j++;
                }
            }
        }
        for(int j=0; j<c; j++)
        {
            for(int i=0;i<r; i++)
            {
                if(gd[i][j]!='?')
                {
                    char chr=gd[i][j];
                    i++;
                    while(i<r && gd[i][j]=='?')
                        gd[i][j]=chr, i++;
                    i--;
                }
            }

            for(int i=r-1; i>=0; i--)
            {
                if(gd[i][j]!='?')
                {
                    char chr=gd[i][j];
                    i--;
                    while(i>=0 && gd[i][j]=='?')
                        gd[i][j]=chr, i--;
                    i++;
                }
            }
        }

        printf("Case #%d:\n", T-t);
        for(int i=0; i<r; i++)
        {
            printf("%s\n", gd[i]);
        }
    }

    return 0;
}

























