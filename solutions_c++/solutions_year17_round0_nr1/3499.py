#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int N,I,i,j;
    cin>>N;
    string s;
    int k;
    for(I=1;I<=N;I++)
    {
        cin>>s>>k;
        int cnt=0;
        for(i=0;i<=s.size()-k;i++)
            if(s[i]=='-')
        {

            cnt++;
            for(j=i;j<i+k;j++)
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
        }
        cout<<"Case #"<<I<<": ";
        int ok=1;
        for(i=0;i<s.size() && s[i]=='+';i++);
        if(i==s.size())
            cout<<cnt<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
