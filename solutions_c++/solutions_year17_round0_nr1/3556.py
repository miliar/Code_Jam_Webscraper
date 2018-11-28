#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <algorithm>

using namespace std;

const int MAXN=1000+10;

char s[MAXN];
int k;

void change(char &s){
    if(s=='+') s='-';
    else s='+';
}


int main(){
    //freopen("in.txt","r",stdin);
    int T;
    scanf("%d",&T);
    int time=0;
    while(T--){
        scanf("%s%d",s,&k);
        int n=strlen(s);
        int ans=0;
        for(int i=0;i<n;i++){
           if(i+k-1>n-1) break;
           if(s[i]=='-'){
                ++ans;
                for(int j=0;j<k;j++){
                    change(s[i+j]);
                }
           }
        }
        bool flag=false;
        for(int i=0;i<n;i++){
            if(s[i]=='-'){
                flag=true;
                break;
            }
        }
        printf("Case #%d: ",++time);
        if(!flag)
        printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}

