#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int i,K,j;
        string str;
        cin>>str;
        cin>>K;
        int len=str.length();
        int count=0;
        for(i=0;i<len-K+1;i++)
        {
            if(str[i]=='-')
            {
                for(j=i;j<K+i;j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
                count++;
            }
           // cout<<"i ";
        }
        int flag=0;
        for(i=len-K;i<len;i++)
        {
            if(str[i]=='-')
            {
                flag=1;
                break;
            }
        }
        cout<<"Case #"<<k<<": ";
        if(flag)
        {
            cout<<"IMPOSSIBLE";
        }
        else
            cout<<count;
        cout<<endl;
    }
    return 0;
}
