#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("controlcliffe.txt");
   long t,z=0;
   input>>t;
   while(t--)
   {
       z++;
       long n,i;
       double d,k,s;
       double a[1000],temp=0.000001,f;
       input>>d>>n;
       for(i=0;i<n;i++)
       {
           input>>k>>s;
           a[i]=(d-k)/s;
           if(a[i]>temp)
            temp=a[i];
       }
       f=d/temp;
       output<<"case #"<<z<<": "<<fixed<<setprecision(6)<<f<<endl;
   }
}
