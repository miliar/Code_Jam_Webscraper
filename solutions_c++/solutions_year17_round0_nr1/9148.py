#include "bits/stdc++.h"
using namespace std;
int main()
{
  int t;
  cin>>t;
  for (int T = 0; T <t ; T++) {

    std::vector<char> v;
    v.clear();
    int k;
    string str;
    cin>>str;
    cin>>k;
    for (int i = 0; i < str.length(); i++) {
      v.push_back(str[i]);
    }

    int count;
    count=0;
    while(v.size()>=k)
    {

      if(v.size()<k)
      {break;}
        if(v.back()=='-')
        {
          for(int i=v.size()-k;i<v.size();i++)
          {
            if(v[i]=='+')v[i]='-';
            else
            v[i]='+';
          }
          count++;
          v.pop_back();
        }
        else
        {
          v.pop_back();
        }
    }
    while(v.size()>0&&v.back()=='+')
    {
      v.pop_back();
    }
    if(v.size()>0)
    {
      cout<<"Case #"<<T+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    else
    {
      cout<<"Case #"<<T+1<<": "<<count<<endl;
    }
    v.clear();
  }
}
