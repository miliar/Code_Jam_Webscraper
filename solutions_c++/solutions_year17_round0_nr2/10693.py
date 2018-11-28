#include <stdio.h>

int main()
{
    int flag,fflag,T,N,i,fnum,tidy,temp,num1,num2,factor;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&N);
        Loop: fnum=N;temp=fnum;flag=0;fflag=0;factor=1;
        while(temp){
            temp=temp/10;
            factor=factor*10;
        }
        while(factor>1){
            factor=factor/10;
            if(flag==0)
            {
                num1=fnum/factor;
                num2=num1;
            }
            if(flag==1)
            {
                num1=num2;
                num2=fnum/factor;
            }
            fnum=fnum%factor;
            flag=1;
            if(num1>num2)
                {N=N-1;goto Loop;}
        }
        if(fflag==0)
            printf("Case #%d: %d\n",i,N);
    }
    return 0;
}

