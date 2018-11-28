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

int p[1010], b[1010];
int coun[1010];

vector<set<int>> s;

int main()
{
    freopen("/Users/lujcmss/Downloads/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/b.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int n, c, m;
        cin >> n >> c >> m;
        
        memset(coun, 0, sizeof(coun));
        int ride = 0;
        
        for (int i = 0; i < m; i++) {
            cin >> p[i] >> b[i];
            if (p[i] == 1) {
                ride++;
                coun[b[i]]++;
            }
        }
        
        int promo = 0;
        int rem = 0;
        
        for (int row = 2; row <= n; row++) {
            int taken = 0;
            int org_ride = ride;
            for (int i = 0; i < m; i++) {
                if (p[i] == row) {
                    if (taken < ride && coun[b[i]] < ride) {
                        coun[b[i]]++;
                        taken++;
                    } else if (coun[b[i]] < ride) {
                        coun[b[i]]++;
                        rem--;
                        promo++;
                    } else {
                        ride++;
                        taken++;
                        coun[b[i]]++;
                    }
                }
            }
            
            rem += ride - taken + (ride - org_ride) * (row - 1);
        }
        
        cout << "Case #" << kase + 1 << ": " << ride << " " << promo << endl;
    }
    
    return 0;
}
