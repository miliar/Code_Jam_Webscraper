#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;
int main()
{
     int t,j,count,x,c,i,y;
     string s;
     char ca;
     cin >> t;

     for(int p=1;p<=t;p++)
     {j=0;
     count=0;

         cin >> s;
y=s.size();
         cin>>x;
    for(int i=0;i<y;i++)
    {
       if(s[i]=='-')
       {int f=i;
       c=0;
       j=f;
            if(j+x-1<y)
           while(j<=f+x-1 && j<y)
           {
               c++;
               if(s[j]=='-')
                s[j]='+';
               else
                s[j]='-';
               j++;
           }
           if(c==x)
            count++;
       }
       else
        continue;

    }
    for( i=0;i<y;i++)
    {
        if(s[i]=='-')
        {
            cout << "Case #"<<p<<": IMPOSSIBLE"<<endl;
            break;
        }
    }
    if(i==y)
        cout << "Case #"<<p<<": "<<count<<endl;

     }return 0;
}
