#include<iostream>
using namespace std;
int main()
{
  int f=2,i,t,n,a[100],b[100];
  cin>>t; int k=0;
while(t--)
{k++;
   cin>>n;
while(n>0) {

   if(n<=9)
   {
  cout<<"Case #"<<k<<": "<<n<<endl;
  //k++;
  break;
   }
   i=0;
   int a1=n;
  while(a1>0)
    {
    //  i=0;
        a[i]=a1%10;
        a1=a1/10;
        i++;
       }

for(int j=i-1;j>0;j--)
{
  if(a[j]<=a[j-1])
  f=0;
  else
   { f=1; break; }

}
if(f==0) { cout<<"Case #"<<k<<": "<<n<<endl; break; //k++;
}
else { n--; }

     }
     }
}
