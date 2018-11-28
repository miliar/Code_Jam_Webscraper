#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    FILE *fp=fopen("inp3.txt","r");
    FILE *fp1=fopen("out3.txt","w+");
    int j,l,t,m,h,height;
    long long int i,n,k,r,even_no,odd_no,even_count,odd_count;
    long long int prev,temp_even,temp_odd,temp_even_no,temp_odd_no;
    fscanf(fp,"%d",&t);
    //printf("%d\n",t);
    for(l=0;l<t;l++)
    {
        even_count=0;
        temp_even=0;
        temp_odd=0;
        temp_even_no=0;
        temp_odd_no=0;
        odd_count=0;
        even_no=0;
        odd_no=0;
        h=0;
        prev=1;
        fscanf(fp,"%lld %lld",&n,&k);
        height=floor(log(k)/log(2));
        prev=pow(2,height)-1;
       // printf("k=%lld prev=%lld height=%d\n",k,prev,height);
        if(n%2==0)
        {
            even_no=n;
            even_count=1;
        }
        else
        {
            odd_no=n;
            odd_count=1;
        }
        while(h<height)
        {
            temp_even=0;
            temp_odd=0;
            if(even_count!=0)
            {
                temp_even=even_count;
                temp_odd=even_count;
                if((even_no/2)%2==0)
                {
                    temp_even_no=even_no/2;
                    temp_odd_no=(even_no-1)/2;
                }
                else
                {
                    temp_odd_no=even_no/2;
                    temp_even_no=(even_no-1)/2;
                }
            }
            if(odd_count!=0)
            {
                if(((odd_no-1)/2)%2==0)
                {
                    temp_even+=2*odd_count;
                    temp_even_no=(odd_no-1)/2;
                }
                else
                {
                    temp_odd+=2*odd_count;
                    temp_odd_no=(odd_no-1)/2;
                }
            }
            even_no=temp_even_no;
            even_count=temp_even;
            odd_no=temp_odd_no;
            odd_count=temp_odd;
            h++;
        }
        if(even_no>odd_no)
        {
            if(even_count>=k-prev)
            {
                even_no--;
                fprintf(fp1,"Case #%d: %lld %lld\n",l+1,(even_no-even_no/2),even_no/2);
                printf("Case #%d: %lld %lld\n",l+1,(even_no-even_no/2),even_no/2);
            }
            else
            {
                odd_no--;
                fprintf(fp1,"Case #%d: %lld %lld\n",l+1,(odd_no-odd_no/2),odd_no/2);
                printf("Case #%d: %lld %lld\n",l+1,(odd_no-odd_no/2),odd_no/2);
            }
        }
        else
        {
            if(odd_count<k-prev)
            {
                even_no--;
                fprintf(fp1,"Case #%d: %lld %lld\n",l+1,(even_no-even_no/2),even_no/2);
                printf("Case #%d: %lld %lld\n",l+1,(even_no-even_no/2),even_no/2);
            }
            else
            {
                odd_no--;
                fprintf(fp1,"Case #%d: %lld %lld\n",l+1,(odd_no-odd_no/2),odd_no/2);
                printf("Case #%d: %lld %lld\n",l+1,(odd_no-odd_no/2),odd_no/2);
            }
        }
    }
}
