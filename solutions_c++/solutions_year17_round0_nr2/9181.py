#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
#define MAXN 20
int a[MAXN];
int len;
bool non_decrease(int j){
    for(int k = j; k < len - 1; k++){
        if (a[k] < a[k+1]){
            return false;
        }
    }
    return true;
}

int main(){
    int T,t=0;
    long long n, tmp;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> T;
    while(t < T){
        t++;
        cin >> n;
        memset(a, 0, sizeof(a));
        tmp = n;
        len = 0;
        while(tmp > 0){
            a[len++] = tmp % 10;
            tmp /= 10;
        }
        for (int j=0; j < len; j++ ) {
            if (non_decrease(j)){
                break;
            } else {
                a[j] = 9;
                a[j+1] -= 1;
            }
        }
        n = 0;
        for (int j = len-1; j >= 0; j--){
            n *= 10;
            n += a[j];
        }
        printf("Case #%d: %lld\n", t, n);
    }
    return 0;
}
