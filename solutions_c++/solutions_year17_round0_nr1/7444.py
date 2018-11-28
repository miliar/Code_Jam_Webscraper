#include <cmath>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int main()
{
    freopen("ab.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k,temp,count1,count2=1,flag;
    char s[1002];
    cin>>t;
    while(t--)
    {
        flag=0;
        count1=0;
        cin>>s;
        cin>>k;
        temp=strlen(s);

        for(int i=0;i<=(temp-k);i++)
        {
            if(s[i]=='-')
              {
                  for(int j=i;j<i+k;j++)
                  {
                      if(s[j]=='+')
                        s[j]='-';
                      else
                        s[j]='+';
                  }
                  count1++;
              }
        }
        for(int i=temp-1;i>temp-k;i--)
        {
          if(s[i]=='-')
        {
            flag=1;
            break;

        }
        }
        if(flag==1)
           cout<<"Case #"<<count2++<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<count2++<<": "<<count1<<endl;
    }
    return 0;
}
