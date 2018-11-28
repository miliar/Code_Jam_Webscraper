#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
int main()
{
    ll tc,k,i,j,flag,cminus,l,swap;
    char str[1010];
    cin>>tc;
    for(i=1;i<=tc;i++)
    {
        cin>>str;
        cin>>k;
        flag=1;
        swap=0;
        for(j=0;j <= strlen(str)-k;j++)
        {
            if(str[j]=='+')
                continue;
            else
            {
                swap++;
               // cminus=0;
                for(l=j;l<j+k;l++)
                {
                    if(str[l]=='-')
                    {
                 //       cminus++;
                        str[l]='+';
                    }
                    else
                    {
                        str[l]='-';
                    }
                }
                /*if(cminus==k)
                    flag=1;
                else
                    flag=0;*/
            }
        }
        /*cout<<swap<<" "<<cminus<<"\n";*/
        cminus=0;
 //       cout<<j<<"\n";
        for(l=j;l<strlen(str);l++)
        {
            if(str[l]=='-')
            {
                cminus++;
                break;
            }
        }
        if(cminus==0)
            cout<<"Case #"<<i<<": "<<swap<<"\n";
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<"\n";
            
    }
}
