#include<bits/stdc++.h>
using namespace std;

const int maxn=18;
char s[maxn+5];

char* work(){
    int n=strlen(s);
    int k=n;
    while(k--){
        for(int i=0;i+1<n;i++){
            if(s[i]>s[i+1]){
                s[i]--;
                for(int j=i+1;j<n;j++)s[j]='9';
                break;
            }
        }
    }
    char* p=s;
    while(*p=='0')p++;
    return p;
}



int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",s);
        printf("Case #%d: %s\n",t,work());
    }
}
