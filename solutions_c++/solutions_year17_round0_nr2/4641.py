#include <iostream>
#include <cstdio>
#include <vector>

#include <cstring>
using namespace std;
int main()
{
  int t,i,j,k,n,c=0;
  cin>>t;
  while(t--)
  {
    c++;
    char arr[20];
    cin>>arr;
    n=strlen(arr);
    bool temp=false,temp2=false;
    vector<int> answer;
    bool temp3=true;
    int cnt=0;
   for(i=0;i<n-1;i++)
   {
    if(arr[i]-'0'>arr[i+1]-'0')
    {
      if(arr[i]=='1')
      {

        temp=true;
        break;
      }
      else
      {
        answer.push_back((arr[i]-'0'-1));

        temp2=true;
        break;

      }
    }
    else if(arr[i]==arr[i+1])
    {
    cnt++;
    }
    else 
    {
      
      for(j=0;j<cnt+1;j++)
      answer.push_back(arr[i]-'0');
cnt=0;
    }

   }
   //cout<<cnt;
   cout<<"Case #"<<c<<": ";

   if(temp)
   {
    for(j=0;j<n-1;j++)
      cout<<"9";
    cout<<endl;
   }
   else if(temp2)
   {
    for(j=0;j<answer.size();j++)
      cout<<answer[j];
    for(j=i+1-cnt;j<n;j++)
      cout<<"9";
    cout<<endl;
   }
   else
    cout<<arr<<endl;
  }






	return 0;
}