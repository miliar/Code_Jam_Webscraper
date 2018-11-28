#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("inputashot.txt","r",stdin);
    freopen("outputa.txt","w",stdout);
    int test,count=0,flag=0;
    cin>>test;
    int n=test;
    while(test)
    {

        string s;
        count=0;
        cin>>s;
        int k;
        cin>>k;
        //input
        for(int i=0;i<s.length()-(k-1);i++)
        {
            if(s[i]=='-')
            {
                s[i]='+';
                for(int j=i+1;j<(i+1)+(k-1);j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                count++;
            }
        }
        cout<<"Case #"<<n-test+1<<": ";
        for(int i=s.length()-k+1;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                cout<<"IMPOSSIBLE"<<endl;
                flag=1;
                break;
            }
        }
        if(!flag)
            cout<<count<<endl;
        flag=0;
        test--;
    }
    return 0;
}
