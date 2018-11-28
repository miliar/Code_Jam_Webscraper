//P = 2     0   11
//P = 3     0   12   111   222
//P = 4     0   13   22    112    233    1111    3333
#include <cstdio>
#include <algorithm>
using namespace std;
int n, p;
int r[4];

int find(){
    int val = 0;
    if(p == 2){
        val += r[0];
        val += r[1] / 2;

        if(r[1] % 2 == 1){
            val += 1;
        }
    }
    else if(p == 3){
        val += r[0];

        int temp = min(r[1], r[2]);
        val += temp;
        r[1] -= temp;
        r[2] -= temp;

        val += r[1] / 3;
        val += r[2] / 3;

        if(r[1] % 3 != 0 || r[2] % 3 != 0){
            val += 1;
        }
    }
    else{
        val += r[0];

        val += r[2] / 2;
        r[2] %= 2;
        int temp = min(r[1], r[3]);
        val += temp;
        r[1] -= temp;
        r[3] -= temp;

        if(r[2] == 1){
            if(r[1] >= 2){
                val += 1;
                r[2] -= 1;
                r[1] -= 2;
            }
            else if(r[3] >= 2){
                val += 1;
                r[2] -= 1;
                r[3] -= 2;
            }
        }

        val += r[1] / 4;
        val += r[3] / 4;

        if(r[1] % 4 != 0 || r[3] % 4 != 0){
            val += 1;
        }
    }

    return val;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++){
        scanf("%d %d", &n, &p);
        for(int i = 0; i < p; i++){
            r[i] = 0;
        }
        int temp;
        for(int i = 0; i < n; i++){
            scanf("%d", &temp);
            r[temp % p] ++;
        }

        int ans = find();
        printf("Case #%d: %d\n", tt, ans);
    }
}
