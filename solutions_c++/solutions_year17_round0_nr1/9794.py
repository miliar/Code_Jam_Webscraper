#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        string s;
        cin>>s;
        int n=s.length();
        int k;
        cin>>k;
        int count=0;
        int flag=0;
        for(int j=0;j<n-k+1;j++){
        if(s[j]=='-'){
            for(int a=j;a<j+k;a++){
                if(s[a]=='+')
                s[a]='-';
            else
                s[a]='+';}
                count++;
        }}
        for(int j=0;j<n;j++)
            if(s[j]=='-')
            flag=1;
        cout<<"Case #"<<i<<": ";
        if(flag==0)
            cout<<count<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    }
    return 0;
}

