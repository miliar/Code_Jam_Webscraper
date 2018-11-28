#include <iostream>
#include<algorithm>
using namespace std;
int main() { int i,t,p,k;
   int n,a[1002]={-1};
   cin>>t;
   int test=1;
    while(test<=t)
    {    long int n,a[1001]={-9};
        cin>>n>>k;
        i=0;
        if(k==n/2 && n%2==0)
       { a[i+1]=1;a[i]=0;}
       else
        {a[0]=n;
        
        for(p=0;p<k;p++)
        {if(a[i]%2==0&&a[i]!=0)
          {a[i+1]=a[i]/2;
              a[i]=(a[i]/2)-1;
          
           }
         else
         {a[i+1]=a[i]/2;
             a[i]=a[i]/2;
         }
          if(p==k-1)
           break;
         sort(a,a+i+2);i++;
         
        }
            
     }
    cout<<"case #"<<test++<<": "<<a[i+1]<<" "<<a[i]<<endl;
        
    }    
    return 0;
}