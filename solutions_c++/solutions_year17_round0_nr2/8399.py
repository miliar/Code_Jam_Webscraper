#include <stdio.h>
#include <math.h>

int a[20];
int main()
{
    int t;
    long long temp, temp2,n;
    int len,flag;
    FILE *out;

    out=fopen("output.txt", "wt");
    scanf("%d", &t);
    for(int k=1; k<=t; ++k)
    {
        scanf("%lld", &n);
        temp=n;
        temp2=n;
        len=0;
        while(temp)
        {
            temp/=10;
            len++;
        }

        for(int i=1; i<=len; ++i)
        {
            a[i]=temp2%10;
            temp2/=10;
        }
        flag=1;
        while(flag==1)
        {
            flag=0;
            for(int i=len-1; i>=1;--i)
            {
                if(a[i]< a[i+1])
                {

                    a[i+1]--;
                    if(a[i+1]==0 &&i+1==len)
                    {
                        len--;
                        a[len]='\0';
                    }
                    for(int j=i; j>=1; --j)
                    {
                        a[j]=9;
                    }
                    flag=1;
                }
            }
        }

        fprintf(out, "Case #%d: ",k);
        for(int i=len; i>=1; --i)
        {
            fprintf(out, "%d",a[i]);
        }
        fprintf(out, "\n");

    }
}
