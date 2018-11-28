#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
const int MAX=1003;
int main(void)
{
    freopen("D:/fun time/A-small-attempt0.in","r",stdin);
    int t,test=1;
    int n,k;
    char str[MAX];
    cin>>t;
    while(t--)
    {
        cin>>str;
        cin>>k;
        n=(int)strlen(str);
        int flip=0,flag=1;
        for(int i=0;str[i];i++)
        {
            if(str[i]=='-')
            {
                if(i+k>n)
                {
                    flag=0;
                    break;
                }
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                ++flip;
            }
        }
        if(flag)
            cout<<"Case #"<<test++<<": "<<flip<<endl;
        else
            cout<<"Case #"<<test++<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
