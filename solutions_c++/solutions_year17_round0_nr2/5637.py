#include <stdio.h>
#include <string.h>
#define MAX_SIZE 25

int num[MAX_SIZE];
int T, N;

bool check(){
    int i = 0;
    while(num[i] == 0 && i < N)
        i++;
    for(i++; i < N; i++){
        if(num[i] < num[i - 1])
            return false;
    }
    return true;
}

void print_num(){
    int i = 0;
    while(num[i] == 0 && i < N)
        i++;
    for(; i < N; i++){
        printf("%d", num[i]);
    }
    printf("\n");
}

void calc(){
    for(int pos = N - 1; pos >= 0;){
        //print_num();
        if(check()){
            print_num();
            return;
        }
        num[pos]--;
        for(int j = pos; num[j] < 0 && j > 0; j--){
            num[j] = 9;
            num[j - 1]--;
        }
        if(num[pos] == 9)
            pos--;
    }
}

int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        char temp[MAX_SIZE];
        scanf("%s", temp);
        int len = strlen(temp);
        int i = 0;
        N = 0;
        while(temp[i] == '0')
            i++;
        for(;i < len; i++)
            num[N++] = temp[i] - '0';
        printf("Case #%d: ", t);
        calc();
    }
    return 0;
}
