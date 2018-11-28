#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
    int t,n,k,i,cnt,j,x,y,flg,len;
    char s[1001];
    freopen("input2.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>s;
        cin>>k;
        len=strlen(s);
        cnt=0;
        for(j=0;j<len;)
        {
            if(s[j]=='-')
            {
                cnt++;
                x=0;
                y=j;
                if(j+k<=len){while(x<k)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                    j++;x++;

                }
                j=y+1;}
                //cout<<s<<endl;
            }
            if(j+k>len)
                break;
            if(s[j]=='+')
                j++;

        }
        flg=0;
        for(j=0;s[j]!='\0';j++)
        {

            if(s[j]=='-')
            {
                flg=1;break;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(flg==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<cnt<<endl;
    }
}
