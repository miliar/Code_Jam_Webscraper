#include<bits/stdc++.h>

int main()
{
    int T,A[25];
    int i,var;
    int count_test=0;
    char S[25];
    scanf("%d",&T);
    while(T--)
    {
        ++count_test;
        int xx=0;
        scanf("%s",S);
        int length=strlen(S);
        for(i=length-1;i>=0;i--)
        {
            A[xx]=S[i]-48;
            xx++;
        }
        for(i=1;i<xx;i++)
        {
            if(A[i]>A[i-1])
            {
                A[i]--;
                for(var=i-1;var>=0;var--)
                    A[var]=9;
            }
        }
        printf("Case #%d: ",count_test);
        if(A[xx-1]!=0)
            printf("%d",A[xx-1]);
        for(i=xx-2;i>=0;i--)
        {
            printf("%d",A[i]);
        }
        printf("\n");
    }
return 0;
}
