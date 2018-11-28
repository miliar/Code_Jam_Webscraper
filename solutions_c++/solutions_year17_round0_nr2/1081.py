#include<bits/stdc++.h>
using namespace std;
char s[100];
char ans[100];
int main(){
    int t,C=0;
    scanf("%d",&t);
    unsigned long long int x,y;
    while(t--){
        scanf("%s",s);
        sscanf(s,"%llu",&x);
        printf("Case #%d: ",++C);
        int n=strlen(s);
        int id=-1;
        y=0;
        for(int i=0;i<n;i++){
            y=y*10+s[i]-'0';
            if(i && s[i]<s[i-1]){
                id=i;
                y/=10;
                break;
            }
        }
        if(id==-1){
            puts(s);
            continue;
        }
        unsigned long long int ed = y%10;
        while(y>9 && (y%100)/10==ed){
            y/=10;
        }
        y--;
        while(y*10+9<=x) y=y*10+9;
        printf("%llu\n",y);
    }
}

