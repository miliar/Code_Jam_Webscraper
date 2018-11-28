#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
  int t,i,j,k,n,c=0;
  cin>>t;
  while(t--)
  {
    c++;
    char str[20];
    cin>>str;
    n=strlen(str);
    bool temp=false,temp2=false;
    vector<int> ans;
    bool temp3=true;
    int cnt=0;
   for(i=0;i<n-1;i++)
   {
    if(str[i]-'0'>str[i+1]-'0')
    {
      if(str[i]=='1')
      {

        temp=true;
        break;
      }
      else
      {
        ans.push_back((str[i]-'0'-1));
        temp2=true;
        break;

      }
    }
    else if(str[i]==str[i+1])
    {
    cnt++;
    }
    else 
    {
      cnt=0;
      ans.push_back(str[i]-'0');

    }

   }
   cout<<"Case #"<<c<<": ";

   if(temp)
   {
    for(j=0;j<n-1;j++)
      cout<<"9";
    cout<<endl;
   }
   else if(temp2)
   {
    for(j=0;j<ans.size();j++)
      cout<<ans[j];
    for(j=i+1-cnt;j<n;j++)
      cout<<"9";
    cout<<endl;
   }
   else
    cout<<str<<endl;
  }






	return 0;
}