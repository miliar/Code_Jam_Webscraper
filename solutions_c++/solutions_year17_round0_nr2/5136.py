#include <iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
    long long int c=0,i,tc,t,k,aprev,flag,count,j,len,prev,curr,pprev;
    string s;
    
    cin >> t;
    for(tc=1; tc<=t; tc++)
    {
           cout << "Case #"<<tc<<": ";
           cin >> s;
           len=s.length();
           if(len==1)
                cout << s << endl;
           else
           {
               prev=s[0]-'0';
               for(i=1;i<len;i++)
               {
                   if(i>1)
                        pprev=s[i-2]-'0';
                   curr=s[i]-'0';
                   aprev=prev;
                   if(prev>curr)
                   {
                        s[i-1]=prev-1+'0';
                        prev=s[i-1]-'0';
                        for(j=i;j<len;j++)
                            s[j]='9';
                        break;
                   }
                   prev=curr;
              }
              if(len>2)
              {
                  if(pprev>aprev)
                  {
                      for(j=i-1;j>0;j--)
                      {
                          s[j]='9';
                          s[j-1]=s[j-1]-1;
                      }
                  }
               }
               if(s[0]=='0')
               {
                    s=s.substr(1);
                    cout << s << endl;
               }
               else
                    cout << s << endl;
           }
    }
    
    return 0;
}
