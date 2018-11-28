// Example program
#include <iostream>
#include<vector>
using namespace std;
int tidy(unsigned long long n);
int main()
{       
       int t;
       cin>>t;
       for(int k=0;k<t;k++)
       {
        
         int n,ch=0;
        cin>>n;
        while(ch!=1)
          {
             ch=tidy(n);
             n--;
          }
         cout<<"Case #"<<k+1<<": "<<n+1<<"\n";
       }  
 return 0;       
}
int tidy(unsigned long long n)
     {
        unsigned long long temp,i=1;
        int t1;
        vector< int > v;
        temp=n;
        t1=temp%10;
        temp=temp/10;
        if(t1==0)
         return 0;
        
        v.push_back(t1);
        while(temp)
          {
            v.push_back(temp%10); 
            if(v[i-1]>=v[i])
                  i++;
            else 
              return 0;
            
            temp=temp/10;
          }
  return 1;
  
   }
