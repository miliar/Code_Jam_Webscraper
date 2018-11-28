#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
char s[1010];
int len,t,k,j,flag,ans;
int main(){
    cin>>t;
    for(int i=1;i<=t;i++){
        ans=flag=0;
        scanf("%s",s);
        cin>>k;
        len=strlen(s);
        for(j=0;j<=len-k;j++){
            if(s[j]=='-'){
                for(int m=0;m<k;m++){
                    if(s[j+m]=='+')s[j+m]='-';
                    else s[j+m]='+';
                }
                ans++;
            }
        }
        for(;j<len;j++){
            if(s[j]=='-'){
                flag=1;
                break;
            }
        }
        if(flag){
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        }else{
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
    return 0;
}
