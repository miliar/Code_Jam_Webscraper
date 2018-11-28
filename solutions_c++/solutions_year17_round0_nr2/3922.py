#include<cstdio>
#include<cstring>
using namespace std;
const int maxn=20;
char s[maxn];
int main()
{
    //freopen("F:\\Users\\zheng\\Desktop\\B-large.in","r",stdin);
    //freopen("F:\\Users\\zheng\\Desktop\\A.txt","w",stdout);
    int T,ca=1;scanf("%d",&T);
    while(T--)
    {
        scanf("%s",s);
        int len=strlen(s);
        int pos=-1;
        for(int i=0;i+1<len;i++)
            if(s[i]>s[i+1])
            {
                pos=i;
                break;
            }
        while(1)
        {
            if(pos<0)break;
            s[pos]--;
            if(pos==0)
            {
                break;
            }
            if(s[pos]>=s[pos-1])break;
            pos--;
        }
        if(s[0]=='0')
        {
            for(int i=0;i<len-1;i++)
                s[i]='9';
            s[len-1]=0;
        }
        else if(pos>=0)
        {
            for(int i=pos+1;i<len;i++)
                s[i]='9';
        }
        printf("Case #%d: %s\n",ca++,s);
    }
    return 0;
}
