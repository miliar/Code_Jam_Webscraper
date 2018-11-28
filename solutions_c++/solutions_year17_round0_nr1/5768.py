#include<bits/stdc++.h>
using namespace std;       // Author @MD.Chand Alam

int main()
{
   freopen( "input.txt", "r", stdin );
   freopen( "output.txt", "w", stdout );

    int t;
    cin>>t;

    for(int cs=1;cs<=t;cs++)
    {

        string str;
        int k,step=0;
        cin>>str>>k;
        int flag=0;
        for(int i=0;i<=str.size()-k;i++)
        {
            if(str[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
             step++;
            }
        }
           int c=0;
           for(int i=0;i<str.size();i++)
           {
               if(str[i]=='+')
                 c++;
           }
          if(c==str.size())
            flag=1;
       if(flag==1)
       cout<<"Case #"<<cs<<": "<<step<<endl;
       else
        cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}

