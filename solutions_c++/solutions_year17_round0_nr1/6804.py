#include<stdio.h>
#include<string.h>
#include<map>
#include<string>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int i,j,k,l,t,flag,len,res,co=1;
    char s[1009];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s %d",s,&k);
        map<string,int> mp;
        map<string,int>::iterator it;
        len=strlen(s);
        mp[s]=1;
        flag=res=0;
        while(1)
        {
            flag=0;
            for(i=0;i<len;i++)
            {
                if(s[i]=='-')
                {
                    j=i;
                    flag=1;
                    res++;
                    break;
                }
            }
            //printf("%s %d %d\n",s,res,flag);
            if(flag)
            {
                if(j+k>=len)
                    j=len-k;
                for(l=j;l<j+k;l++)
                {
                    if(s[l]=='-')
                        s[l]='+';
                    else
                        s[l]='-';
                }
                //printf("%s\n",s);
                it=mp.find(s);
                if(it!=mp.end())
                {
                    flag=2;
                    break;
                }
                else
                    mp[s]=1;
            }
            else
                break;
        }
        if(flag==2)
            printf("Case #%d: IMPOSSIBLE\n",co++);
        else
            printf("Case #%d: %d\n",co++,res);
    }
    return 0;
}
