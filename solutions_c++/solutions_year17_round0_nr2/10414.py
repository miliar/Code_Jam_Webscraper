#include <bits/stdc++.h>
using namespace std;
int N,TC;
int check(int p){
    for(int j=0; j<5; j++,p/=10)
        if(p/10%10>p%10)  return 0;
    return 1;
}
void doit(){
    scanf("%d",&N);
    for(int i=N; i; i--)
        if(check(i)){
            printf("%d\n", i);
            break;
        }
}

int main(){
    scanf("%d",&TC);
    for(int i=1; i<=TC; i++){
        printf("Case #%d: ",i);
        doit();
    }
}
