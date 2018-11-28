#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t;
    vector <int> v;
    cin>>t;
    for(int i=0;i<t;i++)
    {
      string s;
      int count=0;
      cin>>s;
      int k;
      cin>>k;
      for(int j=0;j<=s.length()-k;j++)
      {
          if(s[j]=='-')
          {

             for(int l=0;l<k;l++)
              {
                  if(s[l+j]=='-')
                    s[l+j]='+';
                else
                  s[l+j]='-';

              }
              count++;
          }

      }
      for(int j=s.length()-k+1;j<s.length();j++)
      {
          if(s[j]=='-')
          {
            count=-1;
            break;

          }

      }
       v.push_back(count);
       s.clear();
    }
    for(int i=0;i<v.size();i++)
    {
        if(v.at(i)==-1)
            cout<<"case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"case #"<<i+1<<": "<<v.at(i)<<endl;

    }

}
