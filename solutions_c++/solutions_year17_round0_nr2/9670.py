#include<stdio.h>
#include<conio.h>

#include<list>
#include<iostream>
using namespace std;
//void flip(char [],int ,int );
int main()

{

freopen("B-small-attempt0.in","r",stdin);
freopen("Tidy_output.out","w",stdout);


    int t,l,k=9,i;
    int num,n;

    scanf("%d",&t);

      for(i=1;i<=t;i++)
    {

        scanf("%d",&n);
        num=n;
        while(num>0)
        {
            l=num%10;
            num=num/10;

            if(l>k)
            {
                n=n-k-1;
                num=n;
                k=9;
            }
            else
            {
            k=l;
            }

        }


   k=9;

 printf("Case #%d: %d\n",i,n);




    }
    return 0;



}
