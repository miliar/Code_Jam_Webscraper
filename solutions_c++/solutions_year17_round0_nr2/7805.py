#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include <fstream>
using namespace std;


int main()
{
    ofstream myfile;
  myfile.open ("output.txt");

    int t,d,j;
    cin>>t;
    int k=1;
    while(t--)
    {

      long long int n,n1,check=0;
      cin>>n;
      n1=n;
      vector <int>a,b;

      while(n1>0)
      {
          int i=1;
          b.push_back(n1%10);
          if(n1%10==0)
            check=1;

          n1=n1/10;
          i++;
      }

      for(int i=b.size()-1;i>=0;i--)
        a.push_back(b[i]);

      for(int i=0;i<a.size()-1;i++)
      {
          if(a[i+1]<a[i])
          {
              for( j=i+1;j<a.size();j++)
                a[j] = 9;

                if(a[i]!=1)
                {
                    j=i;
                    d=a[i];
                    while(a[j-1]==d&&j>=1)
                    {
                        a[j]=9;
                    j--;
                    }
                    a[j]--;
                    break;
                }

                else {
                            a.erase(a.begin() + (a.size()-1));
                            for( j=0;j<a.size();j++)
                                a[j]=9;
                                break;
                    }


          }




      }
      myfile<<"Case #"<<k<<": ";

      for(int i=0;i<a.size();i++)
        {
            myfile<<a[i];

        }

    k++;
      myfile<<endl;

    }



return 0;
}
