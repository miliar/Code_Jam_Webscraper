#include <cstdio>
#include <cmath>

long long int po[19] = {
    1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
    1000000000, 10000000000, 100000000000, 1000000000000,
    10000000000000, 100000000000000, 1000000000000000,
    10000000000000000, 100000000000000000,
    1000000000000000000
};

long long int in;
long long int temp;
int solved;
int test;
int dig;
int msb;
int sub;
int a, b;
int main(){
    while(~scanf("%d", &test)){
        for(int t=1; t<=test; t++){
            scanf("%lld", &in);
            if(in >= 1000000000000000000)
                in = 999999999999999999;
            while(in>0){
                //printf("in %lld\n", in);
                temp = in;
                dig = floor(log10(temp))+1;
                solved = 1;
                for(int d=1; d<=dig; d++){
                    a = temp /10 % 10;
                    b = temp % 10;
                    if(a > b){
                        solved = 0;
                        sub = d;
                        msb = a;
                    }
                    temp/=10;
                }
                if(solved){
                    printf("Case #%d: %lld\n", t, in);
                    break;
                }
                else{
                    in=(in/po[sub+1])*po[sub+1]+msb*po[sub]-1;
                }
            }
        }
    }
}
