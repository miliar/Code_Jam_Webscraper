#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
struct stall{
    int num;
    int cnt;
    bool operator<(const stall &b) const{
        return this->num > b.num;
    }
};

int main() {
    struct stall div[3];
    bool bflag;
    int i, j, T, cnt, N, K, minV, maxV, dcnt;
    int tmp1, tmp2;
    cnt = 0;
    cin>> T;
    while(T--) {
        cin >> N >> K;
        memset(div, 0, sizeof(div));
        div[0].num = N;
        div[0].cnt = 1;
        for (i = 0; i < K; ) {
            
            bflag = false;
            tmp1 = tmp2 = 0;
            sort(div, div+3);
            // cout << i << ' ' << div[0].num<<' '<< div[0].cnt<<endl;
            if (div[0].num == 1)  {
                break;
            }
            
            if (div[0].num % 2 == 1) {
                i += div[0].cnt;
                tmp2 = tmp1 = div[0].num / 2;
                for (j = 0; j < 3; j++) {
                    if (div[j].num == tmp1) {
                        div[j].cnt += (2 * div[0].cnt);
                        break;
                    }
                }
                if (j == 3) {
                    div[0].num = tmp1;
                    div[0].cnt *= 2;
                } else {
                    div[0].num = 0;
                    div[0].cnt = 0;
                }
            } else {
                i += div[0].cnt;
                tmp1 = div[0].num / 2;
                tmp2 = tmp1 - 1;
                for (j = 0; j < 3; j++) {
                    if (div[j].num == tmp1) {
                        div[j].cnt += div[0].cnt;
                        break;
                    } 
                }
                if (j == 3) {
                    div[0].num = tmp1;
                    bflag = true;
                }
                for (j = 0; j < 3; j++) {
                    if (div[j].num == tmp2) {
                        div[j].cnt += div[0].cnt;
                        break;
                    } 
                }
                if (j == 3 && bflag) {
                    div[2].num = tmp2;
                    div[2].cnt += div[0].cnt;
                } else if (j == 3 && !bflag) {
                    div[0].num = tmp2;
                    //div[0].cnt = 1;
                } else if (j < 3 && !bflag) {
                    div[0].num = 0;
                    div[0].cnt = 0;
                }
                
            }
         
        }
           cout <<"Case #"<<++cnt<< ": "<< tmp1 <<' '<< tmp2<<endl;
    }
    return 0;
}
