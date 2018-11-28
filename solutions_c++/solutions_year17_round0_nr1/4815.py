#include<bits/stdc++.h>

int main()
{
    int T,n;
    int i,j,k,f;
    int var;
    int counter;
    int count_test=0;
    char s[1005];
    int A[1005];
    scanf("%d",&T);
    while(T--)
    {
        counter=0,
        f=0,
        var=0;
        ++count_test;
        scanf("%s%d",s,&k);
        int length=strlen(s);
        for(n=0;n<length;n++)
        {
            if(s[n]=='+')
                {
                    A[var]=1;
                    var++;
                }
            else
               {
                   A[var]=-1;
                   var++;
               }
        }
        for(i=0;i<=var-k;i++)
        {
            if(A[i]==-1)
            {
                for(j=i;j<i+k;j++)
                {
                    A[j]*=-1;
                }
                counter++;
            }
        }
        for(n=0;n<var;n++)
            if(A[n]==-1)
                f=1;
        if(f==1)
            printf("Case #%d: IMPOSSIBLE\n",count_test);
        else
            printf("Case #%d: %d\n",count_test,counter);
    }
    return 0;
}
