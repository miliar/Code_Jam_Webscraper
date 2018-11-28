#include <bits/stdc++.h>
using namespace std;
char str[10001];
int check[10001];
int t,n;
void  tryit(int i)
{
    if(check[i]==0)
        return;
    else if(check[i]==1)
        {if(str[i]=='+')
        str[i]='-';
        else str[i]='+';
    }
}
bool doit(int index)
{
    if((index-n+1)<0)
        return false;
    else for(int i=index;i>=(index-n+1);i--)
        check[i]=(check[i]+1)%2;
return true;
}

void setcheck()
{
    for(int i=0;i<=1000;i++)
        check[i]=0;
}

int main()
{
scanf("%d",&t);
bool ans=true;
int minans=0;
int caset=0;
while(t--)
{ans=true;
minans=0;
caset++;
setcheck();
    scanf("%s",str);
    scanf("%d",&n);
    int len=strlen(str);
    for(int i=len-1;i>=0;i--)
    {
        tryit(i);
        if(str[i]=='+')continue;
        else if(doit(i)){minans++;continue;}
        else {ans=false;break;}
    }
    if(!ans)
    printf("Case #%d: IMPOSSIBLE\n",caset);
else printf("Case #%d: %d\n",caset,minans);

}






return 0;}