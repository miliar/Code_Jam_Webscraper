#include<iostream>

using namespace std;


int cal(int n)
{
int k=0,m=0,l=0,s=0,p=0;
   
    
     
 
 
      k=n%10;
      p=n/10;
      l=p%10;
     p= p/10;
      m=p%10;
      p=p/10;
      s=p%10;
      
  if(l<=k && m<=l&&s<=m)     
{

   return n;
    
}
else 
{
    cal(n-1);

}

}
   
int main()
{


 int t,n;
 cin>>t;
 int b=1;
 while(t--)
   {
 
   int r=0;
      cin>>n;
      
   r=  cal(n);
 
 cout<<"case #"<<b<<": "<<r<<"\n";
 
 b++;
 }return 0;
 }
 
 
 
 
 
 
 
 
