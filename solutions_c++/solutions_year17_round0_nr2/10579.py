#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
    {
    long long int rm,z,j=1,k,i,a,b[100];
    cin>>a;
    for(i=0;i<a;i++)
        {
         cin>>b[i];
        k=b[i];
        z=k;
         for(j=1000000;j>0;--j)
          {
             rm=z%10;
             z=z/10;
             
             if(rm < z%10)
               {  k=k-1;
                  z=k;
                
               }
            
           }
           
            cout<<"Case #"<<i+1<<": " <<k<<"\n";
             
           }       
        
          }