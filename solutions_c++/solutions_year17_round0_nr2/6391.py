#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,p=1;
    scanf("%d",&t);
    while (p<=t)
    {
        long long int ans=0;
        char str[20];
        scanf("%s",str);
        int j;
        //printf("str=%s\n",str);
        int l=strlen(str);
        if(l==1)
        ans=str[0]-'0';
        else
        {
        for(int i=l-1;i>0;i=j-1)
        {
            j=i;
            while(str[j]>=str[j-1]&&j>0)
            {
                j--;
            }
            if(j==0)
            continue;
            else
            {
            str[j-1]--;
            int k=j;
            while(k<=i)
            {
                str[k++]='9';
            }
            //printf("%d %d %d %s\n",i,j,k,str);
            }
        }
        for(int i=0;i<l;i++)
        ans=(ans*10)+(str[i]-'0');
        }
        printf("Case #%d: %lld",p,ans);
        printf("\n");
        p++;
    }
    return 0;
}
