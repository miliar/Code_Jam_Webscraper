#include <iostream>
#include <string>

using namespace std;

void mymain(int t)
{
    int n,i,j,k;
    string str;
    cin>>str;
    n=str.length();
    cin>>k;
    int ans=0;
    for(i=0;i<n-k+1;i++)
    {
        if(str[i]=='+') continue;
        for(j=i;j<i+k;j++)
            if(str[j]=='+') str[j]='-';
            else str[j]='+';
        ans++;
    }
    cout<<"Case #"<<t<<": ";
    for(i=0;i<n;i++)
        if(str[i]=='-')
    {
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }
    cout<<ans<<endl;
}

int main()
{
    int T,t;
    cin>>T;
    for(t=0;t<T;t++) mymain(t+1);
    return 0;
}
