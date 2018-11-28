#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
    int t,p=1;
    scanf("%d",&t);
    while(p<=t)
    {
        int k,count=0;
        char s[1009],s1[1009];
        scanf("%s%d",s,&k);
        //printf("s=%s\n",s);
        int l=strlen(s);
        memset(s1,'+',l);
        int i=0;
        s1[l]=0;
        //printf("l=%d s1=%s\n",l,s1);
        if(strcmp(s,s1)==0)
        count=0;
        else
        {
        while(s[i]=='+')
        i++;
        //printf("i1=%d\n",i);
        for(;i<l;)
        {
            count++;
            if(i+k>l)
                break;
            else
            {
            for(int j=0;j<k;j++)
            {
                if(s[i+j]=='+')
                s[i+j]='-';
                else
                s[i+j]='+';
            }
                while((s[i]=='+')&&(i<l))
                i++;
               // printf("i2=%d\n",i);
            }
            if(strcmp(s,s1)==0)
            break;
        }
        }
        if(strcmp(s,s1)==0)
        printf("Case #%d: %d\n",p,count);
        else
        printf("Case #%d: IMPOSSIBLE\n",p);
        p++;
    }
    return 0;
}
