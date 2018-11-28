#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

#define LOCAL 1

char str[1005];

///Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/A-small-attempt0.in
int main()
{
#ifdef LOCAL
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/A-large.in","r",stdin);
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/A-large.out","w",stdout);
#endif
    int t;
    scanf("%d", &t);
    for(int _cas = 1; _cas <= t; ++_cas){
        printf("Case #%d: ", _cas);
        int k, filp_cnt = 0;
        bool check = true;
        scanf("%s%d", str, &k);
        int len = strlen(str);
        for(int i = 0; i < len && check; ++i){
            if(str[i] == '-'){
                if(i > len-k) {
                    check = false;
                    break;
                }
                for(int j = 0; j < k; ++j){
                    str[i+j] = (str[i+j] == '-') ? '+' : '-';
                }
                ++filp_cnt;
            }
        }
        if(check) printf("%d\n", filp_cnt);
        else printf("%s\n", "IMPOSSIBLE");
    }
    
    return 0;
}
