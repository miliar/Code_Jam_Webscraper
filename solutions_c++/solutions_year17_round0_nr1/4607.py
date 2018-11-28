#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("codein.txt");
    ofstream cout("codeout.txt");
     int t,i;
     cin>>t;
     i=0;
     while(i<t)
     {
         int k;
      string ch;
      cin>>ch;
      cin>>k;
      int p=0;
      for(int j=0;j<=ch.size()-k;j++)
      {
          if(ch[j]=='-')
          {
              p++;
              ch[j]='+';
              for(int f=1;f<k;f++)
              {
                  if(ch[j+f]=='-')
                    ch[j+f]='+';
                  else ch[j+f]='-';
              }
          }
      }
      bool flag=0;
      for(int j=ch.size()-k;j<ch.size();j++)
      {
          if(ch[j]=='-')
          {
              flag=1;break;
          }
      }
      if(flag)
      cout<<"case #"<<i+1<<": IMPOSSIBLE\n";
      else cout<<"case #"<<i+1<<": "<<p<<endl;
      i++;
     }
    return 0;
}

