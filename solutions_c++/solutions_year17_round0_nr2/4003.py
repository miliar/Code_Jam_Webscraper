#include<bits/stdc++.h>
using namespace std;
#define maxn 200
char s[maxn];
char ans[maxn];
int len;
bool flag;
bool judge(int num,int pos)
{
    for(int i=pos;i<len;++i)
    {
        if(num>s[i]) return false;
        if(num<s[i]) return true;
    }
    return true;
}
int main()
{
    int T;
    //freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas)
    {
        scanf("%s",s);
        printf("Case #%d: ",cas);
        len=strlen(s);
        flag=true;
        for(int i=0;i<len;++i)
        {
            if(!flag) {ans[i]='9'; continue;}
            for(int j='0';j<=s[i]+1;++j)
                if(!judge(j,i))
                {
                    ans[i]=j-1;
                    if(j-1!=s[i]) flag=false;
                    break;
                }
        }
        int st=0;
        for(int i=0;i<len;++i)
            if(ans[i]!='0')
            {
                st=i;
                break;
            }
        for(int i=st;i<len;++i) putchar(ans[i]);
        puts("");
    }
    return 0;
}
