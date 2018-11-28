#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

int a[20];
int main()
{
    int a[20];
    long long num, ans;
    freopen("/Users/zty/Downloads/B-large.in", "r", stdin);
    freopen("/Users/zty/Downloads/B-large.txt", "w", stdout);
    int N;
    scanf("%d", &N);
    for(int cas=1;cas<=N;cas++){
        memset(a, 0, sizeof(a));
        ans = 0;
        scanf("%lld", &num);
        long long m = num;
        int cnt = 0;
        while(m > 0){
            a[cnt++] = m % 10;
            m /= 10;
        }
        for(int j=cnt-1;j>=1;j--){
            if(a[j-1] < a[j]){
                a[j] -= 1;
                while(j < cnt-1){
                    if(a[j+1] > a[j]){
                        a[j+1] -= 1;
                        j++;
                    }
                    else
                        break;
                }
                while(j >= 1){
                    a[j-1] = 9;
                    j--;
                }
            }
        }
        long long l = 1;
        for(int j=0;j<cnt;j++){
            ans += a[j] * l;
            l *= 10;
        }
        printf("Case #%d: %lld\n",cas,ans);
    }
    return 0;
}