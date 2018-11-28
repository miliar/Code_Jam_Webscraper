
#include<iostream>
using namespace std;
int countDigit(long long int N)
{ int j=0;
   while(N!=0)
   {
      N=N/10;
      j++;
   }
   return j;

}
void calc(long long int N,int dig,int i)
{
    int a[20],j=dig-1;
    while(N != 0)
     {
      a[j]=N%10;
      N=N/10;
      j--;
     }
     for(int k=0;k<dig-1;k++)
     {
         if(a[k]>a[k+1])
         {
              while(a[k]==a[k-1]&&k>0)
                k--;
              a[k]=a[k]-1;
              for(int l=k+1;l<dig;l++)
              {
                  a[l]=9;

              }

         }


     }
     cout<<"Case #"<<i+1<<": ";
     for(int l=0;l<dig;l++)
     {
         if(a[l]!=0)
         {

         cout<<a[l];
         }

     }
     cout<<"\n";


}
int main()
{
 int T;
 long long int N;
 cin>>T;
 for(int i=0;i<T;i++)
 {
     cin>>N;
     int dig;
     if(N>=1&&N<=9)
     {

         cout<<"Case #"<<i+1<<": "<<N<<endl;
     }
     else
     {
       dig=countDigit(N);
       calc(N,dig,i);

     }
 }
 return 0;
}
