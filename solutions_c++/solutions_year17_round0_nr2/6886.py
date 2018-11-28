/****** HAREE KRISHNA   ******/

/*
                     শুনেছি তোমার ভীষণ রাগ ??
                        সে কি  রাগ,নাকি
                     মগজ কোণে পচন ধরা
                        পুরনো কোডের বাগ ?
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long int lld;
typedef unsigned long long int llu;

#define sf scanf
#define pf printf
#define ff first
#define ss second
#define PI acos(-1.0)
#define sq(x) (x)*(x)
#define nn printf("\n")
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define TEST int test,zz;scanf("%d",&zz);getchar();for(test=1;test<=zz;test++)

#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d %d",&x,&y)
#define sci3(x,y,z) scanf("%d %d %d",&x,&y,&z)

#define pfi(x) printf("%d\n",x)
#define pfi2(x,y) printf("%d %d\n",x,y)
#define pfi3(x,y,z) printf("%d %d %d\n",x,y,z)

#define scs(str) scanf("%s",str)

#define pfs(str) printf("%s\n",str)

#define pb push_back

/*

ASCII Vlaue
A=65,Z=90,a=97,z=122,0=48,9=57
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

*/
#define chk1 printf("chek1\n")
#define chk2 printf("chek2\n")
#define chk3 printf("chek3\n")
#define sz 2005
#define sz1 30

/******   start your code   *******/

char str[sz1];
char str2[sz1];
int check()
{
    int i,j,k,l;
    l=strlen(str2);
    for(i=l-1; i>=1; i--)
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
    int i,j,k,n,pos;
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    TEST
    {
        scs(str);
        strcpy(str2,str);
        pos=check();
        while(pos)
        {
            str2[pos]='9';
            if(strcmp(str2,str)>0)
            {
                for(i=pos-1; i>=0; i--)
                {
                    if(str2[i]!='0')
                    {
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
        //pf("zz = %d\n",zz);
        pf("Case #%d: ",test);
        for(i=0; str2[i]; i++)
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
