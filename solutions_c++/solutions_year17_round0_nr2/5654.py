#include <iostream>
using namespace std;
int main() 
{
    int p,t,k,c,a[20],s,i,j;
   long long int n;
    cin>>t;
    p=1;
    while(p<=t)
    {  k=0;
        cin>>n;
        while(n)
     { a[k++]=n%10;
       n/=10;
       }    for(i=0;i<k-1;i++)
    {j=i+1;
     if(a[i]<a[j])
      {  s=i; while(s>=0){a[s--]=9;}
          a[j]-=1;
         }
    }  
        cout<<"case #"<<p<<": ";
        for(i=k-1;i>-1;i--)
        {   if(a[i]==0&&i==k-1)
              i--;
            cout<<a[i];
        }
     p++;
     cout<<endl;
    }
    return 0;
}