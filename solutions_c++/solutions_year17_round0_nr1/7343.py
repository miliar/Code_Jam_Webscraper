#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k;
    char a[1001];
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        cin>>a;
        cin>>k;
        int len=strlen(a)-k;
        int i,count=0;
        for(i=0;i<(len);i++)
        {
            if(a[i]!='+')
            {
                for(int j=i;j<(i+k);j++)
                {
                    if(a[j]=='-')
                        a[j]='+';
                    else
                        a[j]='-';
                }
                ++count;
            }
        }
        int flag=0;
        char d=a[len];
        if(d=='-')
            ++count;
        for(int l=len+1;l<strlen(a);l++)
        {
            if(a[l]!=d)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
        else
        {
                cout<<"Case #"<<z<<": "<<(count)<<endl;
        }
        flag=0;
    }
}
