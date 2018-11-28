#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,no=0;
    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        int k,i,l,j,f=0,c=0;
        char s[1005];

        scanf(" %s",s);
        l=strlen(s);
        scanf("%d",&k);
        //printf("%d\n",k);
        //printf("%s\n",s);
        for(i=0;i<(l-k+1);i++)
        {
            //printf("%d ",i);
            if(s[i]=='-')
            {
                c++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                    s[j]='-';
                    else
                    s[j]='+';

                }
                //cout<<"yo";
            }

        }
        no++;
        for(i=0;i<l;i++)
        if(s[i]!='+')
        f=1;
        printf("Case #%d: ",no);
        if(f)
        printf("IMPOSSIBLE\n");
        else
        printf("%d\n",c);
        //printf("%s\n",s);
    }

}

