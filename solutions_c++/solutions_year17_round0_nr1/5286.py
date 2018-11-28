#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-Large.out","w",stdout);
    int t,p=1;
    cin>>t;
    while(t--){
        string s;
        int k,count=0;
        cin>>s>>k;
        int n=s.length();
        for(int i=0;i<n;i++){
            if(s[i]=='+')
                continue;
            else if(s[i]=='-'){
                count++;
                if((i+k)<=n){
                    for(int j=i;j<k+i;j++){
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                }
                else{
                    for(int i=n-1;i>=n-k;i--){
                        if(s[i]=='-')
                            s[i]='+';
                        else
                            s[i]='-';
                    }
                    break;
                }
            }
        }
        int flag=1;
        for(int i=0;i<n;i++){
            if(s[i]=='-'){
                flag=0;
                break;
            }
        }
        if(flag==1){
            cout<<"Case #"<<p++<<": "<<count<<endl;
        }
        else
            cout<<"Case #"<<p++<<": "<<"IMPOSSIBLE"<<endl;


    }
    return 0;
}
