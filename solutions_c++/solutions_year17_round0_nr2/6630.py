#include<stdio.h>
#include<string.h>
main()
{
    freopen("B-large.in","r+",stdin);
    freopen("tidynumber.out","w+",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        char A[25];
        scanf("%s",A);
        int Alen = strlen(A);
        for(int i=0;i<Alen-1;i++)
        {
            if(A[i] > A[i+1])
            {
                A[i]--;
                for(int j = i+1;j<Alen;j++)
                    A[j] = '9';
                break;
            }
        }
        for(int i=Alen-1;i>=1;i--)
        {
            if(A[i] < A[i-1])
            {
                A[i] = '9';
                A[i-1]--;
            }
        }
        while(A[0]=='0')
        {
            for(int i = 0;i<Alen-1;i++)
                A[i] = A[i+1];
            Alen--;
        }
        printf("Case #%d: ",l);
        for(int i=0;i<Alen;i++)
            printf("%c",A[i]);
        printf("\n");
    }
}
