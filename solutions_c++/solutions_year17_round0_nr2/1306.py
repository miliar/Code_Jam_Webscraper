#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll __int64
#define bug cout<<"here"<<endl
#define fread freopen("B-large.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

int a[30];
int len;

void dfs(int index)
{
    if(index>=len||index<0)
        return;
    a[index]--;
    if(index==0)
        return;
    if(a[index-1]<=a[index])
        return;
    a[index]=9;
    dfs(index-1);
}

int main()
{
//    fread;
//    fwrite;
    int tc;
    char ch[30];
    scanf("%d",&tc);
//    gets(ch);
    int cs=1;
    while(tc--)
    {
        scanf("%s",ch);
//        printf("%s  haha\n",ch);

        len=strlen(ch);
        for(int i=0;i<len;i++)
        {
            a[i]=ch[i]-'0';
        }
//        for(int i=0;i<len;i++)
//            cout<<a[i];
//        cout<<endl;
        int index=len;
        for(int i=1;i<len;i++)
        {
            if(a[i]<a[i-1])
            {
                index=i;
                break;
            }
        }
        for(int i=index;i<len;i++)
            a[i]=9;
//        cout<<"index: "<<index<<endl;
        if(index<len)
            dfs(index-1);
        printf("Case #%d: ",cs++);
        int flag=0;
        for(int i=0;i<len;i++)
        {
            if(a[i]==0)
            {
                continue;
            }
            flag=1;
            printf("%d",a[i]);
        }
        if(!flag)
            printf("0");
        puts("");
    }
    return 0;
}
