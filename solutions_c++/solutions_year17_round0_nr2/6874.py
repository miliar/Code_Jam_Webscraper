#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<cctype>
#include<map>
#include<stack>
#include<cstdlib>
#include<queue>
#include<vector>
#include<algorithm>
#include<bitset>
#include<algorithm>
#include<set>
#include<limits.h>

using namespace std;
typedef long int LD;
typedef long long int LLD;
typedef float F;
typedef double LF;
typedef unsigned int U;
typedef unsigned long int LU;
typedef unsigned long long int LLU;
typedef char C;


/*----------simple input section ------------ */
#define sf scanf
#define sfi(x) scanf("%d",&x)
#define sfc(x) scanf("%c",&x)
#define sfi2(x,y) scanf("%d%d",&x,&y)
#define sfll2(x,y) scanf("%lld%lld",&x,&y)
#define sfu2(x,y) scanf("%llu%llu",&x,&y)
#define sfl(x) scanf("%ld",&x)
#define sfll(x) scanf("%lld",&x)
#define sfd(x) scanf("%lf",&x)
#define sfu(x) scanf("%llu",&x)
#define sfs(x) scanf("%s",x)


/*----------simple input section ------------ */
#define pf printf
#define pfi(x) printf("%d\n",x)
#define pfl(x) printf("%ld\n",x)
#define pfll(x) printf("%lld\n",x)
#define pfu(x) printf("%llu\n",x)
#define pfs(x) printf("%s\n",x)
#define pfc(x) printf("%c\n",x)
#define pfd(x) printf("%lf\n",x)

/*----------file input section ------------ */

#define f_input  freopen("B-large.in","r",stdin);
#define f_output freopen("B-large.out","w",stdout);

#define pb(x) push_back(x)
#define PI acos(-1.0)
#define sq(x) (x)*(x)
#define mem(x,y) memset(x,y,sizeof(x))
#define TEST int cs,T;sfi(T);getchar();for(cs=1;cs<=T;cs++)
#define nn printf("\n")
// xx-> diagonal -> 8 horizontal/vertical->4

const int xx[] = {0, 1, 0, -1, -1, 1, -1, 1};
const int yy[] = {1, 0, -1, 0, 1, 1, -1, -1};

// KX-> Knight moves
const int kx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
const int ky[] = {1, 2, 2, 1, -1, -2, -2, -1};


/******** debug **********/
#define chk1 printf("hi......1  \n")
#define chk2 printf("hi......2  \n")




#define mod 1000000007
#define eps 10e-8
#define sz 100005
#define sz1 302
#define sz2 5
/******* start my code ********/
char str[sz1];
char str2[sz1];
int check()
{
    int i,j,k,l;
    l=strlen(str2);
    for(i=l-1;i>=1;i--)
    {
        if(str2[i]<str2[i-1])
        {
            return i;
        }
    }
    return 0;
}
int main()
{
    f_input;
    f_output;
    int i,j,k,n,pos;
    TEST
    {
        sfs(str);
        strcpy(str2,str);
        pos=check();
        while(pos)
        {
            str2[pos]='9';
            if(strcmp(str2,str)>0){
            for(i=pos-1;i>=0;i--)
            {
                if(str2[i]!='0'){
                    str2[i]=str2[i]-1;
                    break;
                }
                else
                {
                    str2[i]='9';
                }
            }
            }
            pos=check();
        }
        pf("Case #%d: ",cs);
        for(i=0;str2[i];i++)
        {
            if(str2[i]=='0') continue;
            pf("%c",str2[i]);
        }
        nn;
    }
    return 0;
}
/*

*/
