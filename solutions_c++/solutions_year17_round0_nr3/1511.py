
#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <time.h>
#include <vector>
using namespace std;
#define LL long long
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:1024000000")
const int mod=1e9+7;
const int INF=0x3f3f3f3f;
const double eqs=1e-9;
const int MAXN=200000+10;
void func(LL x){
    if(x%2){
        printf("%lld %lld\n",x/2+1,x/2);
    }
    else{
        printf("%lld %lld\n",x/2,x/2);
    }
}
int main()
{
    int t, i, icase=0;
    LL min_num_1, max_num_1, min_cnt_1, max_cnt_1, n, k, tmp, min_num_2, max_num_2, min_cnt_2, max_cnt_2;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",++icase);
        n--;
        if(n%2){
            min_num_1=n/2;
            max_num_1=n/2+1;
            min_cnt_1=max_cnt_1=1;
        }
        else{
            min_num_1=n/2;
            max_num_1=n/2;
            min_cnt_1=max_cnt_1=1;
        }
        k--;
        if(k<=0){
            printf("%lld %lld\n", max_num_1, min_num_1);
            continue;
        }
        min_num_1--;
        max_num_1--;
        while(1){
            if(min_num_1==max_num_1){
                if(min_num_1%2){
                    min_num_2=min_num_1/2;
                    max_num_2=max_num_1/2+1;
                    min_cnt_2=min_cnt_1*2;
                    max_cnt_2=max_cnt_1*2;
                }
                else{
                    min_num_2=max_num_2=min_num_1/2;
                    min_cnt_2=min_cnt_1*2;
                    max_cnt_2=max_cnt_1*2;
                }
            }
            else{
                if(min_num_1%2){
                    min_num_2=min_num_1/2;
                    max_num_2=max_num_1/2;
                    min_cnt_2=min_cnt_1;
                    max_cnt_2=min_cnt_1+max_cnt_1*2;
                }
                else{
                    min_num_2=min_num_1/2;
                    max_num_2=max_num_1/2+1;
                    min_cnt_2=min_cnt_1*2+max_cnt_1;
                    max_cnt_2=max_cnt_1;
                }
            }
            k-=max_cnt_1;
            if(k<=0){
                func(max_num_1);
                break;
            }
            k-=min_cnt_1;
            if(k<=0){
                func(min_num_1);
                break;
            }
            min_num_1=min_num_2-1;
            max_num_1=max_num_2-1;
            min_cnt_1=min_cnt_2;
            max_cnt_1=max_cnt_2;
        }
    }
    return 0;
}
