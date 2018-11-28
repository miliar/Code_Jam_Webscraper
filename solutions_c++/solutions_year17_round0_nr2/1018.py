#include<cstdio>

char a[20];

int solve(){
    int ptr = 0;
    for (int i=1;a[i];i++){
        if (a[i] < a[i-1]){
            a[ptr] --;
            while (a[++ptr]) a[ptr] = '9';
            break;
        }
        else if (a[i] > a[i-1]) ptr = i;
    }
    return a[0] == '0';
}

int main (){
    int T;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        scanf("%s", a);
        printf("Case #%d: %s\n", i, a+solve());
    }
}
