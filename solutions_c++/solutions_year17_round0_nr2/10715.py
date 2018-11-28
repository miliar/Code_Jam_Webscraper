#include <cstdio>

long long int pow10[]={1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000, 10000000000000000, 100000000000000000, 1000000000000000000};

int main(){
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("tidynumbers.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int x=1;x<=T;x++){
        long long int N;
        scanf("%lld", &N);
        int digits;
        for(digits=0;N>=pow10[digits];digits++){

        }
        int A[digits];
        for(int i=0;i<digits;i++){
            A[i]=(N%pow10[i+1]-N%pow10[i])/pow10[i];
        }
        bool istidy=false;
        while(!istidy){
            istidy=true;
            for(int i=digits-1;i>0;i--){
                if(!istidy){
                    A[i-1]=9;
                }
                else if(A[i]>A[i-1]){
                    if(A[i]>0){
                        A[i]--;
                        A[i-1]=9;
                    }
                    istidy=false;
                }
            }
        }
        long long int answer=0;
        for(int i=0;i<digits;i++){
            answer+=A[i]*pow10[i];
        }
        printf("Case #%d: %lld\n", x, answer);
    }
    return 0;
}
