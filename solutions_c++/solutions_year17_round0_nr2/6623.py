#include<stdio.h>
#include<string.h>
#include<math.h>
int long long n;
int tt;

long long int power(int x,int y){
    long long int prod=1;
    for(int i=0;i<y;i++){
        prod = prod*x;
    }
    return prod;
}

int count9(long long int num, int k=0){
    while(1){
        if(num%power(10,k)==(power(10,k)-1)){
            k++;
        }
        else break;
    }
    return k-1;
}


int checkOrder(long long int num){
        long long int newnum=num;
    int lastrem=10;
    while(1){
        int newrem = newnum%10;
        if(newnum!=0){
            if(newrem<=lastrem){
                    lastrem=newrem;
            }
            else{
                return 0;
            }
        }
        else{
            break;
        }
        newnum = newnum/10;
    }
    return 1;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("outputtnl.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; test++){
        printf("Case #%d: ", test);
        scanf("%lld",&n);
        while(n!=0){
            if(checkOrder(n)==1){
                break;
            }
            n=n-power(10,count9(n));
        }
        printf("%lld\n",n);
    }
    return 0;
}
