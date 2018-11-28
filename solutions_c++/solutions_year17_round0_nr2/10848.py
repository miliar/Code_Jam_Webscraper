#include<iostream>
using namespace std;
int main()
{
    int T,N,i,f=0,j,t,r,sm,yeh=0;
    cin>>T;       // input number of Test cases
    for(i=1;i<=T;i++)
    {
        cin>>N;
 
        f=0;yeh=0;
       
        for(j=N;j>=1;j--)
        {
            t=j;yeh=0;f=0;
            while(t!=0)
            {
                r=t%10;
                if(f==0)
                {sm=r;f=1;}
                else
                {
                 if(r<=sm)
                  sm=r;
                  else
                  {
                    yeh=1;break;
                  }
                }
               t=t/10;
             }
             if(yeh==0)
               break;
         }
       
       cout << "Case #" << i << ": " << j<< endl;
     }
    return 0;
 }
