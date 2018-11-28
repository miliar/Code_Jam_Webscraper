#include<iostream>
#include<math.h>
using namespace std;
int main()
{
   int temp,ch,k,i,j,n,a[10],count,x;
   for(i=0;i<10;i++)
   	a[i]=10;
   //scanf("%d",&ch);
   cin>>ch;
   //if(ch>100||ch<1)
   	//exit(0);
   for(k=0;k<ch;k++)
   { cin>>n;

      //if(n>1000||n<1)
   	     //exit(0);

      for(i=n;n>0;n--)
         {
              for(i=0;i<10;i++)
   	           a[i]=10;
            i=n;
          temp=i;
            count=0;

            x=ceil(log10(i));
            if(i==1000)
                x=4;
            if(i==100)
                x=3;
            if(i==10)
                x=2;
            if(i==1)
               x=1;


           for(j=0;j<x;j++)
        	{
        		a[j]=i%10;
        		i=i/10;
        		count++;
        	}
          j=0;
          while(a[j]>=a[j+1])
          {
            count--;
            j++;
          }

          if(count==1)
      	   break;
        }
      //printf("Case #%d: %d\n",k+1,temp);
      cout<<"Case #"<<k+1<<": "<<temp<<"\n";
    }
    return 0;
}

