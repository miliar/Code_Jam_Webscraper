#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <array>
#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>
#include <time.h>
#include <errno.h>
#include <semaphore.h>

using namespace std;

int fun(int hk, int hd, int ak, int d, int c_attack, int c_debuff) {
    int hd_max = hd;
    int step = 0;
    
    while (step < 10000) {
        if (hd > ak || (c_debuff > 0 && hd > (ak - d)) || (c_debuff == 0 && c_attack == 1)) {
            if (c_debuff > 0) {
                ak -= d;
                c_debuff--;
                if (ak < 0) {
                    ak = 0;
                }
            } else {
                c_attack--;
            }
            hd -= ak;
        } else {
            hd = hd_max - ak;
        }
        step++;
        if (c_attack == 0) {
            break;
        }
    }
    
    return step;
}

int main()
{
    freopen("/Users/lujcmss/Downloads/C-small-attempt1.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/c.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        
        int c_attack = (hk - 1) / ad + 1;
        for (int i = 1; i < 101; i++) {
            c_attack = min((hk - 1) / (ad + i * b) + 1 + i, c_attack);
        }
        
        int ans = 10000;
        for (int c_debuff = 0; c_debuff < 101; c_debuff++) {
            ans = min(fun(hk, hd, ak, d, c_attack, c_debuff), ans);
        }
        
        cout << "Case #" << kase + 1 << ": ";
        if (ans == 10000) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
