#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
char change(char c){
    if(c=='-')
        return '+';
    else
        return '-';
}
int main(){
    freopen("C:/Users/jn/Downloads/A-large.in","r",stdin);
    freopen("E:/out.txt","w",stdout);
    int T,k,cas=1;
    string s;
    cin>>T;
    while(T--){
        cin>>s>>k;
        int ans=0;
        for(int i=0;i<s.length();++i){
            if(s[i]=='-'){
                if(i<s.length()-k+1){
                    ans++;
                    for(int j=0;j<k;++j)
                        s[i+j]=change(s[i+j]);
                }
                else{
                    ans=-1;
                    break;
                }
            }
        }
        if(ans==-1)
            printf("Case #%d: IMPOSSIBLE\n",cas++);
        else
            printf("Case #%d: %d\n",cas++,ans);
    }
}
