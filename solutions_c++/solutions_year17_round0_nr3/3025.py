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


int main()
{
    freopen("/Users/lujcmss/Downloads/C-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/C3.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        uint64_t n, k, y, z, cy, cz;
        cin >> n >> k;
        
        y = n;
        z = n - 1;
        cy = 1;
        cz = 0;
        
        while (k) {
            if (k > cy + cz) {
                k -= cy + cz;
                if (y & 1) {
                    cy = cy * 2 + cz;
                    y >>= 1;
                    z = y - 1;
                } else {
                    cz = cz * 2 + cy;
                    z >>= 1;
                    y = z + 1;
                }
                continue;
            }
            if (k <= cy) {
                z = (y - 1) / 2;
                y = (y - 1) / 2 + (y - 1) % 2;
            } else {
                y = (z - 1) / 2 + (z - 1) % 2;
                z = (z - 1) / 2;
            }
            k = 0;
        }
        
        cout << "Case #" << kase + 1 << ": " << y << " " << z << endl;
    }
    return 0;
}
