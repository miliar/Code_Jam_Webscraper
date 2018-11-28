#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,a=1;
    scanf("%d",&t);
    while(t){
    //cout<<t<<" ";
    string s;
    int k,ans=0,flag=0;
    cin>>s>>k;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='-')
        {
            //cout<<i<<" lol ";
            ans++;
            if(i+k>s.size())
            {
                flag=1;
                break;
            }
            for(int j=i;j<i+k;j++)
            {
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
        }
    }
        cout<<"Case #"<<a<<": ";
        a++;
        t--;
        if(flag==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}
