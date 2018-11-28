#include<bits/stdc++.h>
using namespace std;
char s[20];
int main()
{
     //freopen("i.in","r",stdin);
	//freopen("o.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%s",s);
        int n=strlen(s);
        int r=0;int p=0,q=0,m=0,y=0,j;
        for( j=1;j<n;j++)
        {
            if(s[j-1]!=s[p])
                p=j-1;
            if(s[j]<s[j-1])
            {
                s[j-1]=s[j-1]-1;
                m=1;


                    if(s[j-1]=='0')
                        r=1;

                y=1;
                    break;
            }

        }
        int o=j;
   //     printf("%d\n",r);
        printf("Case #%d: ",i);
        if(y==1)
        {
            if(r==1)
            {
                for(int j=0;j<n-1;j++)
                {
                    printf("%c",'9');
                }
                printf("\n");
            }
            else if(m==1)
            {
                for(int j=0;j<p;j++)
                {
                    printf("%c",s[j]);
                }
                printf("%c",s[o-1]);
                for(int j=p+1;j<o;j++)
                {
                    printf("%c",'9');
                }
                for(int j=o;j<n;j++)
                {
                    printf("%c",'9');
                }
                printf("\n");
            }
        }
        else
            printf("%s\n",s);

    }
    return 0;
}
