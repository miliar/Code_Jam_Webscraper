#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int T;
long long N,K;

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        long long y = 0, z = 0;
        cin >> N >> K;
        long long cnt = 0;
        long long small = N, big = N;
        long long smallCnt = 1, bigCnt = 1;
        
        while (true) {
            if (big % 2 == 0) y = big / 2, z = big / 2 - 1;
            else y = z = big / 2;
            cnt += bigCnt;
            if (cnt >= K) break;
            
            if (small < big) {
                if (small % 2 == 0) y = small / 2, z = small / 2 - 1;
                else y = z = small / 2;
                cnt += smallCnt;
                if (cnt >= K) break;
            }
            
            long long tSmall, tSC, tBig, tBC;
            
            if (small == big) {
                if (small % 2 != 0) small = small / 2, big = small, smallCnt = bigCnt = (bigCnt * 2);
                else {
                    big = small / 2, small = big - 1, smallCnt = bigCnt;
                }
            }
            else {
                if (small % 2 != 0) small = small / 2, big = small + 1, smallCnt += smallCnt + bigCnt;
                else small = small / 2 - 1, big = small + 1, bigCnt += smallCnt + bigCnt;
            }
        }
        
        printf("Case #%d: ", cas);
        cout << y << " " << z << endl;
        
    }
    return 0;
}