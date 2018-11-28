#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int main(){
    int t,i,len,flag,cnt,j;
    char n[25];
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%s",n);
        len=strlen(n);
        flag=1;
       // printf("%s",n);
       while(flag){
            flag=0;
            for(i=1;i<len;i++){
                if(flag){
                    n[i]='9';
                }
                else if(n[i]<n[i-1]){
                    flag=1;
                    n[i-1] = (char)(((int)n[i-1]) - 1);
                    n[i]='9';
                }
            }
       }
       cnt = 0;
       for(i=0;i<len;i++){
            if(n[i]=='0'){
                cnt++;
            }else
                break;
        }
        string ans = "";
        for(int i = cnt; i<len;i++){
            ans+= n[i];
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
