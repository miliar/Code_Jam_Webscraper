#include <cstdio>
#define MAX 18

FILE *output;
long long N, TC;

void init(){
    N = 0;
}

void input(){
    scanf("%lld", &N);
}

int getLength(long long num){
    int len = 0;
    while(num!=0) len++, num/=10;
    return len;
}

void result(long long num){
    long long res = 0;
    long long K;
    K = N;
    long long arr[MAX], arr2[MAX];
    int len = 0, org;
    while(K != 0){
        arr[len] = K%10;
        arr2[len++] = K%10;
        K/=10;
    }
    org = len;
    while(true){
        
        bool isFind = true;
        long long pre = arr[0];
        int j;
        for(j = 1; j<len; j++){
            if(pre >= arr[j]) pre = arr[j];
            else {
                arr[j]--;
                for(int z = j-1; z>=0; z--)
                    arr[z] = 9;
                isFind = false;
                break;
            }
        }
        if(arr[len-1] <= 0) len--;
        if(isFind){
            long long tmp = 0;
            for(j = len-1; j>=0; j--)
                tmp = (tmp*10) + arr[j];
            fprintf(output, "Case #%lld: %lld\n", num, tmp);
            break;
        }
        
    }
}


int main(){
    output = fopen("out.txt", "w");
    scanf("%lld", &TC);
    for(long long i = 1; i<=TC; i++){
        init();
        input();
        result(i);
    }
    fclose(output);
    return 0;
}
