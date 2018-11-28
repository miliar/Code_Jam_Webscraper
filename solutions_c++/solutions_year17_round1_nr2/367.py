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

int64_t m[60][60];
int64_t need[60];

int main()
{
    freopen("/Users/lujcmss/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/b1.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int n, p;
        cin >> n >> p;

        for (int i = 0; i < n; i++) {
            cin >> need[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> m[i][j];
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int ii = 0; ii < p - 1; ii++) {
                for (int jj = ii + 1; jj < p; jj++) {
                    if (m[i][ii] > m[i][jj]) {
                        auto tmp = m[i][ii];
                        m[i][ii] = m[i][jj];
                        m[i][jj] = tmp;
                    }
                }
            }
        }
        
        int64_t ans = 0;
        
        for (int kit = 0; kit < p; kit++) {
            int64_t guess = m[0][kit] / need[0];
            
            for (int64_t k = guess - 400000; k < guess + 400000; k++) {
                if (k * need[0] * 0.9 <= m[0][kit] && k * need[0] * 1.1 >= m[0][kit]) {
                    bool valid = true;
                    for (int i = 1; i < n; i++) {
                        bool found = false;
                        for (int j = 0; j < p; j++) {
                            if (k * need[i] * 0.9 <= m[i][j] && k * need[i] * 1.1 >= m[i][j]) {
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            valid = false;
                            break;
                        }
                    }
                    
                    if (valid) {
                        ans++;
                        for (int i = 1; i < n; i++) {
                            for (int j = 0; j < p; j++) {
                                if (k * need[i] * 0.9 <= m[i][j] && k * need[i] * 1.1 >= m[i][j]) {
                                    m[i][j] = 0;
                                    break;
                                }
                            }
                        }
                        break;
                    }
                }
            }
        }
        
        
        cout << "Case #" << kase + 1 << ": " << ans << endl;
    }
    return 0;
}
