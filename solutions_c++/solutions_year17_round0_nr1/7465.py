#include<iostream>
#include<string.h>
using namespace std;
int main()
    {
    int t;
    cin>>t;
    int u[100];
    int i,j;
    for(i=0;i<t;i++)
        {
        int k;
        char s[1000];
        cin>>s;
        cin>>k;
        int count=0;
        int l=strlen(s);
        for(j=0;j<=(l-k);j++)
            {
            if(s[j]=='-')
                {
                count++;
                int y;
                for(y=j;y<j+k;y++)
                    {
                    if(s[y]=='+')
                        s[y]='-';
                    else
                        s[y]='+';
                }
            }
           
        }
        int flag=0;
        for(j=0;j<l;j++)
            {
            if(s[j]=='-')
                flag=1;
        }
        if(flag==1)
            count=-1;
        u[i]=count;
    }
    for(i=0;i<t;i++)
        {
        if(u[i]!=-1)
        cout<<"Case #"<<i+1<<": "<<u[i]<<"\n";
        else
        cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";    
    }
}
