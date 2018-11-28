#include<cstdio>
#include<algorithm>
using namespace std;

int foo(int i, int d1, int d2){
    int ret = i;
    d1 -= i*2;
    d2 -= i;
    ret += d2/2;
    ret += d1/4;
    if (d2%2 || d1%4) ret++;
    return ret;
}

int main (){
    int T;
    scanf("%d", &T);
    for (int t=1;t<=T;t++){
        printf("Case #%d: ", t);

        int n, p, d[4]{};
        scanf("%d%d", &n,&p);
        for (int i=0;i<n;++i){
            int tmp;
            scanf("%d", &tmp);
            ++ d[tmp%p];
        }
        int ans = d[0];
        if (p == 2){
            ans += d[1]/2;
            if (d[1]%2) ans += 1;
        }
        else if (p == 3){
            int tmp = min(d[1], d[2]);
            d[1] -= tmp;
            d[2] -= tmp;
            ans += tmp + d[1]/3 + d[2]/3;
            if (d[1]%3 || d[2]%3) ans += 1;
        }
        else{
            ans += min(d[1], d[3]);
            d[1] = max(d[1], d[3]) - min(d[1], d[3]);
            int max_a = 0;
            for (int i=0;i<=d[2] && i*2 <= d[1];i++){
                int tmp = foo(i, d[1], d[2]);
                if (tmp > max_a)
                    max_a = tmp;
            }
            ans += max_a;
        }
        printf("%d\n", ans);
    }
}
