#include <iostream>
#include<string>
using namespace std;
int main() {
	int t;
	cin>>t;
    for(int i=0;i<t;i++)
     {string s;
     cin>>s;
     int k,c=0,j;
     cin>>k;
     int n=s.size();
     for(int j=0;j<=n-k;j++)
       {if(s[j]=='+')
         {}
         else
          {for(int q=j;q<j+k;q++)
             {if(s[q]=='-')
                s[q]='+';
                else
                 s[q]='-';
             }
           c++;
           }
          
       }
     int x=0;
     for(int u=j;u<n;u++)
        {if(s[u]=='-')
            {x=1;
            break;}
        }
        if(x==1)
          {cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;}
        else
         {cout<<"Case #"<<i+1<<": "<<c<<endl;}
     }
	
	// your code goes here
	return 0;
}
