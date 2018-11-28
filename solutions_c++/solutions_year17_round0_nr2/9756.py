#include<iostream>

using namespace std;

int main()
{
    int t,i,j,k,l=1;
    long long int r;
    cin>>t;
    while(l<=t)
    {
        cin>>r;
        cout<<"Case #"<<l<<":"<<" ";
        if(r<10) cout<<r;
        else 
        {
         int a[20];
         j=0;
         
         while(r>0)
         {
             a[j++]=r%10;
             r=r/10;
         }
         for(i=1;i<j;i++)
         {
             if(a[i-1]<a[i])
             {
                 a[i]=a[i]-1;
                 for(k=0;k<i;k++) a[k]=9;
             }
         }
         for(i=j-1;i>=0;i--) 
          if(a[i]!=0)
           cout<<a[i];
        }
        cout<<endl; 
        l++;
    }
    return 0;
}
