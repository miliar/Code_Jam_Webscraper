#include<stdio.h>
#include<string.h>
char s[100];
int n;
bool dfs(int now,char minLimit,bool maxLimit){
    if(now == n) return true;
    if(s[now] < minLimit && maxLimit == true){
        return false;
    }
    if(maxLimit == false){
        s[now] = '9';
        return dfs(now + 1,minLimit,false);
    }
    if(dfs(now+1,s[now],true) == true) return true;
    if(s[now] > minLimit){
        s[now] -= 1;
        return dfs(now+1,s[now],false);
    }
    return false;
}
void doit(){
    scanf("%s",s);
    n = strlen(s);
    dfs(0,'0',true);
    if(s[0] == '0'){
        n--;
        for(int i=0;i<n;i++) s[i] = s[i+1];
    }
    s[n] = 0;
    printf("%s\n",s);
}
int main(){
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        doit();
    }
}
