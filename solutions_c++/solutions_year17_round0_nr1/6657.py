#include<stdio.h>
#include<string.h>
main()
{
    freopen("A-large.in","r+",stdin);
    freopen("output.out","w+",stdout);
    int t;
    scanf("%d",&t);
    int n;
    for(int l=1;l<=t;l++)
    {
        char A[1005];
        int n;
        scanf("%s %d",A,&n);
        int Alen = strlen(A);
        int counter = 0;
        for(int i=0;i<Alen-n+1;i++)
        {
            if(A[i]=='-')
            {
                for(int j=0;j<n;j++)
                {

                    if(A[i+j]=='+')
                        A[i+j] = '-';
                    else A[i+j] = '+';

                }
                counter++;
            }
        }
        printf("Case #%d: ",l);
        bool prin = false;
        for(int i = Alen-n+1;i<Alen;i++)
        {
            if(A[i]=='-')
            {
                printf("IMPOSSIBLE\n");
                prin = true;
                break;
            }
        }
        if(!prin)
            printf("%d\n",counter);

    }
}
