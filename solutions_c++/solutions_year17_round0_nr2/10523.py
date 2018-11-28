#include <iostream>
#include<fstream>


int sorted(int l);


using namespace std;

int main()
 {

    freopen("B-small-attempt0.in","r",stdin);
   freopen("output_file_name.out","w",stdout);


   int t,n,i,k,l,an,a[1000];

   cin>>t;

       for(k=1;k<=t;k++)
       {cin>>a[k];

      for(l=a[k];l>=0;l--)
      {an=sorted(l);
      if(an)
        break;

      }
      if(an)

      cout<<"Case #"<<k<<": "<<l<<endl;
      }

       }



int sorted(int l)
{
int rem,prerem=10,an=1;
while(l!=0)
{ rem=l%10;
   if(rem>prerem)
   {
   an=0;
   break;
   }
   prerem=rem;
   l=l/10;
   }
   if(an)
   return 1;
   else
   return 0;
   }







