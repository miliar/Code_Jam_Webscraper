#include <iostream>
#include<string.h>
using namespace std;
int main()
{
    long k,i,j,c=0,n=0,T,l,flag,count,length;
    char s[1002];
    cin>>T;
    for(l=1;l<=T;l++)
    {
    flag=0;
    count=0;
    cin>>s>>k;
    length=strlen(s);
    for(i=0;i<=length-k;i++)
    {
        if(s[i]=='-')
        {
            for(j=0;j<k;j++)
            {
                if(s[i+j]=='-')
                    s[i+j]='+';
                else
                    s[i+j]='-';
            }
            count++;
        }
       
    }
    for(int temp=i;temp<length;temp++)
    {
        if(s[temp]=='-')
        {
            flag=1;
            break;
        }

    }
    if(flag==1)
        cout<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
    else
        cout<<"Case #"<<l<<": "<<count<<endl;
    }
    return 0;
   
}
