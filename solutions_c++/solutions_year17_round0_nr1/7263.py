#include<iostream>
#include<string.h>
using namespace std;

int main()
{
    int test,num,len,flip,j;
    char s[1001];
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        flip=0;
        cin>>s>>num;
        len = strlen(s);
        len=len-num;
        for(j=0;j<=len;j++)
        {
            if(s[j]=='+')
            {
                continue;
            }
            flip++;
            for(int k=0;k<num;k++)
            {
                if(s[j+k]=='-')
                    s[j+k]='+';
                else
                    s[j+k]='-';
            }
        }
        len=len+num;
        for(j=0;j<len;j++)
            if(s[j]=='+')
                continue;
            else
                break;
        if(j==len)
            cout<<"Case #"<<i<<": "<<flip<<endl;
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }
}
