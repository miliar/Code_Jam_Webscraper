#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

#define LOCAL 1

//Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/A-small-attempt0.in



int main()
{
#ifdef LOCAL
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/C-small-2-attempt0.in","r",stdin);
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/C-small-2-attempt0.out","w",stdout);
#endif
    long long T[65];
    T[0] = 0;
    for(int i = 1; i < 64; i++) T[i] = T[i-1] + (1ll << (i-1));
    int t;
    scanf("%d", &t);
    for(int _cas = 1; _cas <= t; ++_cas){
        printf("Case #%d: ", _cas);
        long long k, n;
        long long l_num, r_num, l, r;
        scanf("%lld%lld", &n, &k);
        if(n == k){
            printf("0 0\n");
            continue;
        }
        int id = 1;
        long long pre_l = n, pre_r = n;
        l = (n-1) >> 1, r = n >> 1;
        if(l == r) l_num = 0, r_num = 2;
        else l_num = 1, r_num = 1;
        k--;
        while(T[id] <= k){
            if(pre_r & 1) l_num = l_num, r_num = (1<<id) - l_num;
            else r_num = r_num, l_num = (1<<id) - r_num;
            pre_l = l, pre_r = r;
            l = (l - 1) >> 1;
            r = r - 1 - ((r - 1) >> 1);
            id++;
//            printf("pre_l = %lld pre_r = %lld l_num = %lld r_num = %lld num = %lld\n", pre_l, pre_r, l_num, r_num, T[id-1]);
        }
//        printf("pre_l = %lld pre_r = %lld l_num = %lld r_num = %lld num = %lld\n", pre_l, pre_r, l_num, r_num, T[id-1]);
        
//        long long i = 1;
//        while (k >= (1ll << i)) i++;
//        long long low1 = (n + 1 - (1 << (i - 1))) / (1 << (i - 1));
//        long long hig1 = n / (1 << (i - 1));
//        long long cnth1 = (n + 1 - (1 << (i - 1))) % (1 << (i - 1));
//        k -= (1 << (i - 1));
//        long long ans1 = (k < cnth1) ? (hig1 - 1) : (low1 - 1);
/*
 1000
 499 1 500 1
 249 3 250 1
 124 7 125 1
 61 7 62 9
 30 23 31 9
 14 23 15 41
 6 2
 */
        long long ans = ((k - T[id-1]) >= r_num) ? (pre_l-1) : (pre_r-1);
        printf("%lld %lld\n", (ans+1)>>1, ans>>1);
    }
    
    return 0;
}
