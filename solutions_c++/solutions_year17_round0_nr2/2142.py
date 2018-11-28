#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX_LEN = 20;

char s[MAX_LEN];
int num[MAX_LEN];
int ans[MAX_LEN];
int len;

bool found;

void dfs(int dep, int lb, int same){
    if (dep == len){
        found = true;
        return;
    }
    if (same){
        for (int i = num[dep]; i >= lb; --i){
            ans[dep] =  i;
            dfs(dep+1, i, i==num[dep]);
            if (found) return;
        }
    }
    else{
        for (int i = 9; i >= lb; --i){
            ans[dep] =  i;
            dfs(dep+1, i, false);
            if (found) return;
        }
    }
}

int main(){
    freopen("/Users/eajoy/Downloads/B-large.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int CASE = 1; CASE <= T; ++CASE){
        scanf(" %s", s);
        len = (int)strlen(s);
        for (int i = 0; i < len; ++i)
            num[i] = s[i]-'0';
        found = false;
        dfs(0, 0, true);
        long long answer = 0;
        for (int i = 0; i < len; ++i)
            answer = answer*10 + ans[i];
        printf("Case #%d: %lld\n", CASE, answer);
    }
    return 0;
}
