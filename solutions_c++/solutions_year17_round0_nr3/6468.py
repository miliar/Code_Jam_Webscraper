#include<stdio.h>
#include<conio.h>
#include<algorithm>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
  ifstream input;
  input.open("C-small-1-attempt0.in");
  ofstream output;
  output.open("codejam");
  int t,z=0;
  input>>t;
  while(t-->0)
  {
    z++;
    long long int a[10000]={0},b[10000],n,i,k,p,q,r;
    input>>n>>k;
    a[1]=n;
    for(i=2;i<2*n;i++)
    {
       if(i%2==0)
       {
           if(a[i/2]==0||a[i/2]==1)
             continue;
           else
           {
           if(a[i/2]%2==0)
            a[i]=(a[i/2]/2)-1;
           else
            a[i]=a[i/2]/2;
           }
       }
       else
       {
           if(a[(i-1)/2]==0||a[(i-1)/2]==1)
             continue;
           else
           {
           if(a[(i-1)/2]%2==0)
            a[i]=(a[(i-1)/2]/2);
           else
            a[i]=a[(i-1)/2]/2;
           }
       }
    }
   // for(i=0;i<=2*n;i++)
      //  cout<<a[i]<<" ";
    for(i=0;i<=2*n;i++)
        b[i]=a[i];
    sort(b,b+(2*n));
    reverse(b,b+(2*n));
    // for(i=0;i<2*n;i++)
       // cout<<b[i]<<" ";
      int j=b[k-1];
    for(i=0;i<=2*n;i++)
    {
        if(a[i]==j)
        p=i;
    }
   // cout<<a[p]<<" ";
    q=2*p;
    r=(2*p)+1;
    output<<"case #"<<z<<": "<<a[r]<<" "<<a[q]<<endl;
  }
}
