#include <bits/stdc++.h>
using namespace std;
string s;
int main()
{
    freopen("test1.txt","r",stdin);
    freopen("file1.txt","w",stdout);
    long t,k;
    long cnt=0;
    cin>>t;
    while(t--)
    {
        cnt++;
        cout<<"Case #"<<cnt<<": ";
        cin>>s;
        cin>>k;
        long l= s.length();
        long ans=0;
        for(long i=0;i<=l-k;i++){
            if(s[i]=='-'){
            for(long j=i;j<i+k;j++){
                if(s[j]=='+')
                s[j]='-';
                else
                s[j]='+';
            }
            ans++;
            }
        }
        int flag=0;
        for(long i=0;i<l;i++){
            if(s[i]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<ans<<endl;
        }
    }
}

