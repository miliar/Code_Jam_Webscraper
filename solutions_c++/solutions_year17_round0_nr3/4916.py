#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main()
{
    int t,l=1;
    cin>>t;
    while(l<=t)
    {
        long long unsigned int n,k,i=1,count=1,j=0,a,b,x,y,count1=1,count2=1;
        cin>>n>>k;
        while(i<k)
        {
            j++;
            count = count*2;
            i = i+count;
        }
        //cout<<j;
         count = j;
         i = n;
         while(j--)
         {
             i = i/2;
         }
        // cout<<count;
        if(count>0)
         j = count-1;
        else
            j = 0;
        // cout<<j;
        while(j--)
         {
             count1 = count1*2;
             count2 = count2+count1;
         }
         count1 = n-count2;
         a = i*pow(2,count);
         if(count1>=a)
           {
               x = count1-a;
               b = pow(2,count)-x;
               if(b==0)
               y = i;
               else
                y = i-1;
           }
           else
           {
               x = a-count1;
               b = pow(2,count)-x;
               if(b==0)
                y = i;
               else
               y = i-1;
           }
           k = k-pow(2,count)+1;
           if(k<=b)
           {
               cout<<"Case #"<<l<<": "<<i/2<<" "<<(i-1)/2<<endl;
           }
           else
           {
               cout<<"Case #"<<l<<": "<<y/2<<" "<<(y-1)/2<<endl;
           }
           l++;
    }
}
