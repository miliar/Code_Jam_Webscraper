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

int a[110];

int main()
{
    freopen("/Users/lujcmss/Downloads/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/a.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int n, p;
        cin >> n >> p;
    
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        int ans = 0;
        
        int mod[4];
        mod[0] = mod[1] = mod[2] = mod[3] = 0;
        
        for (int i = 0; i < n; i ++) {
            mod[a[i] % p]++;
        }
        
        if (p == 2) {
            ans = mod[0] + (mod[1] + 1) / 2;
        } else if (p == 3) {
            ans = mod[0];
            
            int tmp = min(mod[1], mod[2]);
            ans += tmp;
            
            mod[1] -= tmp; mod[2] -= tmp;
            tmp = max(mod[1], mod[2]);
            
            ans += (tmp + 2) / 3;
        } else {
            ans = mod[0];
            
            int tmp = min(mod[1], mod[3]);
            ans += tmp;
            mod[1] -= tmp; mod[3] -= tmp;
            
            ans += mod[2] / 2;
            mod[2] %= 2;
            
            if (mod[1] != 0) {
                if (mod[2] != 0) {
                    ans += (mod[1] + 5) / 4;
                } else {
                    ans += (mod[1] + 3) / 4;
                }
            } else if (mod[3] != 0) {
                if (mod[2] != 0) {
                    ans += (mod[3] + 5) / 4;
                } else {
                    ans += (mod[3] + 3) / 4;
                }
            }
        }
        
        cout << "Case #" << kase + 1 << ": " << ans << endl;
    }
    
    return 0;
}
