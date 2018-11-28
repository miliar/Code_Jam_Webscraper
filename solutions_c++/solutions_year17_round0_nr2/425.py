#include<stdio.h>
#include<string.h>
char a[10000];


int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0,i,j;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        long long int n=0;
        fscanf(in,"%s",a);
        int l = strlen(a);
        for(i=0;i<l-1;i++)
        {
            if(a[i]>a[i+1])
            {
                a[i]-=1;
                for(j=i+1;j<l;j++)
                {
                    a[j]='9';
                }
                break;
            }
        }
        for(j=i;j>0;j--)
        {
            if(a[j]<'0')
            {
                a[j-1]-=1;
                a[j]+=10;
            }
            if(a[j]<a[j-1])
            {
                a[j] = '9';
                a[j-1]-=1;
            }  
        }
        fprintf(out,"Case #%d: ",ll);
        if(a[0]=='0'){
        fprintf(out,"%s",a+1);
        }
        else{fprintf(out,"%s",a);}
        for(i=0;i<l;i++){a[i]=0;}
        fprintf(out,"\n");
    }
}
