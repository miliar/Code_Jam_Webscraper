#include<bits/stdc++.h>
using namespace std;


int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


    int t;

    cin >> t;

    int j=1;
    while(j<=t)
    {
     string s;

     int flag=1;
     cin >> s;


   for(int i = 0 ; i < s.size()-1 ; i++)
     {
         if(s[i]>s[i+1])
         {
          flag=0;
          break;
         }
     }


    if(flag==0){
     for(int i = s.size()-1 ; i >= 0 ; i--)
     {
      if(s[i]<s[i-1])
      {
          s[i-1]=s[i-1]-1;
          for(int j = i ; j < s.size() ; j++)
          s[j]='9';
      }
      else
      {
          s[i]=s[i];
      }

     }
     s.erase(0, s.find_first_not_of('0'));
    }

     cout<<"Case #"<<j<<": "<<s<<"\n";
    j++;
    }
    return 0;
}
