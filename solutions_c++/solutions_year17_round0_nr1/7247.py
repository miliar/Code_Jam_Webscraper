#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<string.h>
#include<vector>
#include<map>
using namespace std;

#define mx 10000000
#define ip freopen("in.txt","r",stdin)
#define op freopen("out.txt","w",stdout)

#define sint1(a) scanf("%d",&a)
#define sint2(a,b) scanf("%d %d",&a,&b)
#define sint3(a,b,c) scanf("%d %d %d",&a,&b,&c)



#define sch1(a) scanf("%c",&a)
#define sch2(a,b) scanf("%c %c",&a,&b)
#define sch3(a,b,c) scanf("%c %c %c",&a,&b,&c)



#define ll long long int

#define lpi0(a,b) for(int a=0;a<b;a++)
#define lpd0(a,b) for(int a=b-1;a>=0;a--)

#define lpi1(a,b) for(int a=1;a<=b;a++)
#define lpd1(a,b) for(int a=b;a>0;a--)

#define vi vector<int>
#define pii pair<int,int>
#define mp make_pair

#define mm(a,b) memset(a,b,sizeof(a))



int main()
{
//    ip;
//    op;

    int t;

    sint1(t);

    int cs=1;

    while(t--)
    {
        getchar();
        char s[10000];

        int n;
        scanf("%s %d",s,&n);
        int l=strlen(s);
        int ans=0;
//        cout<<s<<n<<endl;
        for(int i=0;i<=l-n;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i;j<i+n;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
//            printf("%s\n",s);
        }
        int f=0;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                printf("Case #%d: IMPOSSIBLE\n",cs++);
                f=1;
                break;
            }
        }

        if(f==0)
        {
            printf("Case #%d: %d\n",cs++,ans);
        }
    }



}


