#include <iostream>
#include <string.h>
using namespace std;

int main()
{
   
    int t,n,k,j=0,n1,n2,n3;
   freopen("B-small-attempt1.in","r",stdin);
    scanf("%d",&t);
    
    for(int i = 0 ; i < t ; i++)
    {
        j=0;
        scanf("%d",&n);
        k=n;
        
        if(n==1000)
            printf("case #%d: 999\n",i+1);
        while(k>0)
        {
            k = k/10;
            j++;
        }
        
        if(j==1)
            printf("case #%d: %d\n",i+1,n);
        
       else if(j==2)
        {
            n2=n%10;
            n1=n/10;
            if(n1>n2)
            {
                n1-=1;
                n2=9;
                printf("case #%d: %d\n",i+1,n1*10+n2);
            }
            else if(n1<=n2)
                printf("case #%d: %d\n",i+1,n);
        }
        
        else if(j==3)
        {
            n3=n%10;
            n2=((n%100)-n3)/10;
            n1=n/100;
            
            if(n3>=n2 && n2>=n1)
                printf("case #%d: %d\n",i+1,n);
            
            else if(n1>=n2 && n2 > n3)
            {n1-=1;
                n2=9;
                n3=9;
                printf("case #%d: %d\n",i+1,n1*100+n2*10+n3);
            }
            else if(n1>=n2 && n2 < n3)
            {n1-=1;
                n2=9;
                n3=9;
                printf("case #%d: %d\n",i+1,n1*100+n2*10+n3);
            }
            else if(n1<n2 && n2>n3)
            {
                n1=n1;
                n2-=1;
                n3=9;
                printf("case #%d: %d\n",i+1,n1*100+n2*10+n3);
            }
            
            else if(n1>n2 && n2>=n3)
            {
                n1-=1;
                n2=9;n3=9;
                printf("case #%d: %d\n",i+1,n1*100+n2*10+n3);
            }

        }
        
    }
   // freopen("output_file_name.out","w",stdout);
}

