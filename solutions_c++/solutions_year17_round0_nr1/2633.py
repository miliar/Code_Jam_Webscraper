#include<stdio.h>
int main()
{
    int T;
    int count;
    scanf("%d",&T);
    for(int j = 1; j <= T; j++)
    {
        char string[1005];
        int K;
        int index = 0;
        count = 0;
        scanf("%s",string);
        scanf("%d",&K);
        int len = strlen(string);
        //printf(" string : %s length : %d flip_size : %d",string,len,K);
        while(index != len)
        {
            if(string[index] == '+')
            {
                index++;
            }
            else
            {
                if(index + K -1 >= len)
                    break;
                for(int temp = 0; temp < K; temp++)
                {
                    if(string[index + temp] == '+')
                        string[index + temp] = '-';
                    else
                        string[index +temp] = '+';
                }
                count++;
                index++;
            }
        }
        if(index != len)
            printf("Case #%d: IMPOSSIBLE\n",j);
        else
            printf("Case #%d: %d\n",j,count);
    }
return 0;
}