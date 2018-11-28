#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include <fstream>
using namespace std;


int main()
{
    int c=1;
    ofstream myfile;
  myfile.open ("output.txt");

    int t;
    cin>>t;
    while(t--)
    {
      int k,ans=0,check=0,zero=0,flag=0;
      string s;
      cin>>s>>k;
      int l= s.size();

      for(int i=0;i<l;i++)
          if((s[i]=='-')&&(i+k<=l))
          {
              ans++;
              for(int j=0;j<k;j++)
              {
                  if(s[i+j]=='-')
                    s[i+j]='+';

                    else s[i+j]='-';
              }

          }

      for(int i=0;i<l;i++)
        if(s[i]=='-')
      {
          myfile<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
            c++;
          check=1;
          break;

      }

        if(check==0)
        {
            myfile<<"Case #"<<c<<": "<<ans<<endl;
                    c++;
        }

    }



return 0;
}
