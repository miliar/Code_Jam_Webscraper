#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
int TC, N, P;
int o, o1, o2, o3;
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d %d", &N, &P);
        o = o1 = o2 = o3 = 0;
        if(P == 2){
            for(int i = 0, t; i < N; ++i){
                scanf("%d", &t);
                if(t&1) ++o1;
                else ++ o;
            }
            printf("Case #%d: %d\n", tc, o + o1/2 + o1%2);
        }
        else if(P == 3){
            for(int i = 0, t; i < N; ++i){
                scanf("%d", &t);
                if(t%3 == 0) ++o;
                else if(t%3 == 1) ++ o1;
                else ++o2;
            }
            int ans = o;
            if(o1 == o2) ans += o1;
            else if(o1 < o2) ans += o1 + (o2 - o1)/3 + ((o2 - o1) % 3 > 0);
            else ans += o2 + (o1 - o2)/3 + ((o1 - o2)% 3 > 0);
            printf("Case #%d: %d\n", tc, ans);
        }
    }
}
                
