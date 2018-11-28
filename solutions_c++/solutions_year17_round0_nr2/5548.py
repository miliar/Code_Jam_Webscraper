#include <iostream>
#include <cstdio>
#include <vector>

#include <cstring>
using namespace std;
int main()
{
  int t,i,j,k,n,c=0;
  cin>>t;





  //wdkgdfvuiwgd
  while(t--)
  {



//cout<<"abse yajssdgsgdd"

for(i=0;i<1;i++)
{
  
}

    c++;
    char auxillary[20];
    cin>>auxillary;
    n=strlen(auxillary);
    bool ykbh=false,ykbh2=false;
    vector<int> wtf;
    bool ykbh3=true;
    int adhm=0;
   for(i=0;i<n-1;i++)
   {
    if(auxillary[i]-'0'>auxillary[i+1]-'0')
    {
      if(auxillary[i]=='1')
      {

        ykbh=true;
        break;
      }
      else
      {
        wtf.push_back((auxillary[i]-'0'-1));

        ykbh2=true;
        break;

      }
    }
    else if(auxillary[i]==auxillary[i+1])
    {
    adhm++;
    }
    else 
    {
      
      for(j=0;j<adhm+1;j++)
      wtf.push_back(auxillary[i]-'0');
adhm=0;
    }

   }
   //cout<<adhm;
   //dlshofwdhifh
   /*ldgwdf




   edidfgbd
   q
   do
   {
     /* code 
   } while (do
   {
     /* code 
   } while (d););*/
   cout<<"Case #"<<c<<": ";

   if(ykbh)
   {
    for(j=0;j<n-1;j++)
      cout<<"9";
    cout<<endl;
   }
   else if(ykbh2)
   {
    for(j=0;j<wtf.size();j++)
      cout<<wtf[j];
    for(j=i+1-adhm;j<n;j++)
      cout<<"9";
    cout<<endl;
   }
   else
    cout<<auxillary<<endl;
  }






	return 0;
}