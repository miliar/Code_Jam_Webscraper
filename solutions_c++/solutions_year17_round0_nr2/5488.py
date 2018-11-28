#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    int t,p=0;
    cin>>t;
    for(p=0;p<t;p++)
    {
        char s[20],ss[20];
        int i=0,j=0,k=0;
        cin>>s;
        for(i=strlen(s)-1;i>=0;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i]='9';
                for(j=i;j<strlen(s);j++)
                    s[j]='9';
                s[i-1]=(int)(s[i-1])-1;
            }
        }
        if(s[0]=='0')
        {
            cout<<"Case #"<<(p+1)<<": ";
            for(k=1;s[k]!='\0';k++)
                cout<<s[k];
                //ss[k-1]=s[k];
            //cout<<ss;
        }
        else
            cout<<"Case #"<<(p+1)<<": "<<s;
        cout<<endl;
    }
}
