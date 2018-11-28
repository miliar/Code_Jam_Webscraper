#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
using namespace std;
char s[20];
int T;
void solve(){
    int len = strlen(s);
    char c;
    for(int i=0;i<len;++i){
        if(i>0 && s[i]<s[i-1]){
            for(int j=i;j<len;++j)
                s[j]='9';
            for(int j=i-1;j>=0;--j){
                if(j==0){
                    s[j]--;
                    return;
                }
                if(s[j]>s[j-1]){
                    s[j]--;
                    return;
                }
                else{
                    s[j]='9';
                }
            }
        }
    }

}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int c=1;c<=T;++c){
        scanf("%s",&s);
        solve();
        printf("Case #%d: ",c);
        int len = strlen(s);
        for(int i=0;i<len;++i)
            if(s[i]!='0')
                printf("%c",s[i]);
        printf("\n");
    }
    return 0;
}

