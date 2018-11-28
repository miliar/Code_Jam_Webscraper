
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int t,i,cnt,fl,j,k,m,l;
    char s[1005];
    cin>>t;
    m=1;
    while(t--)
    {   i=0;
        cin>>s>>k;
        cnt=0;
        fl=0;
        l=strlen(s);
        while(s[i]!='\0')
        {
            if(s[i]=='+')
            {
                i++;
            }
            if(i+k-1>=l)
             break;
            if(s[i]=='-')
            {
              for(j=i;j<=i+k-1;j++)
            {   
                if(s[j]=='+')
                  s[j]='-';
                else if(s[j]=='-')
                  s[j]='+';
                
            }

            cnt++;
            }
            
            
        }
       
        for(j=0;s[j]!='\0';j++)
        {
            if(s[j]=='-')
             fl=1;
        }
        if(fl==0)
        {
            cout<<"Case #"<<m<<": "<<cnt<<"\n";
        }
        else if(fl==1)
        {
            cout<<"Case #"<<m<<": "<<"IMPOSSIBLE\n";
            
        }
        m++;
    }
}


