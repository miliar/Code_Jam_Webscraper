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

char m[26][26];

int main()
{
    freopen("/Users/lujcmss/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/aa.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int r, c;
        cin >> r >> c;
        
        for (int i = 0; i < r; i++) {
            string s;
            cin >> s;
            for (int j = 0; j < c; j++) {
                m[i][j] = s[j];
            }
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (m[i][j] == '?') {
                    int k = j;
                    while (k < c && m[i][k] == '?') {
                        k++;
                    }
                    if (k < c) {
                        m[i][j] = m[i][k];
                    }
                }
            }
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (m[i][j] == '?') {
                    int k = j;
                    while (k >= 0 && m[i][k] == '?') {
                        k--;
                    }
                    if (k >= 0) {
                        m[i][j] = m[i][k];
                    }
                }
            }
        }
        
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
                if (m[i][j] == '?') {
                    int k = i;
                    while (k < r && m[k][j] == '?') {
                        k++;
                    }
                    if (k < r) {
                        m[i][j] = m[k][j];
                    }
                }
            }
        }
        
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
                if (m[i][j] == '?') {
                    int k = i;
                    while (k >= 0 && m[k][j] == '?') {
                        k--;
                    }
                    if (k >= 0) {
                        m[i][j] = m[k][j];
                    }
                }
            }
        }
        
        cout << "Case #" << kase + 1 << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << m[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
