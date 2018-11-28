#include <bits/stdc++.h>
using namespace std;

int n,k,s;
bool p[1010];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d\n",&n);
    for(int i = 0; i < n; i++){
        for(int j = 0;; j++){
            char ch;
            scanf("%c",&ch);
            if(ch == '-') p[j] = 0;
            if(ch == '+') p[j] = 1;
            if(ch == ' '){
                s = j;
                break;
            }
        }
        scanf("%d\n",&k);
        int sol = 0;
        for(int j = 0; j < s; j++){
            if(!p[j]){
                sol++;
                for(int m = j; m < j+k; m++){
                    if(m >= s){
                        sol = -1;
                        break;
                    }
                    p[m] = !p[m];
                }
            }
            if(sol == -1) break;
        }
        if(sol == -1) printf("Case #%d: IMPOSSIBLE\n",i+1);
        else printf("Case #%d: %d\n",i+1,sol);        
    }
}