#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <iomanip>
#include <cstdio>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int rnd = 1; rnd <= T; rnd++) {
        long long K, N;
        cin >> K >> N;
        
        vector<char> v(K + 2, '.');
        v[0] = 'o';
        v[K + 1] = 'o';
        
        long long min_dis;
        vector<long long> v_min;
        
        long long max_dis;
        vector<long long> v_max;
        
        map<long long, long long> m_max;
        
        for (long long i = 0; i < N; i++) {
            min_dis = INT64_MIN;
            
            for (long long j = 1; j <= K; j++) {
                if (v[j] == 'o') {
                    continue;
                }
                long long p = j - 1;
                for (; p >= 0; p--) {
                    if (v[p] == 'o') {
                        break;
                    }
                }
                long long q = j + 1;
                for (; q <= K + 1; q++) {
                    if (v[q] == 'o') {
                        break;
                    }
                }
                
                if (min(j - p, q - j) > min_dis) {
                    min_dis = min(j - p, q - j);
                    v_min.clear();
                    v_min.push_back(j);
                    m_max[j] = max(j - p, q - j);
                } else if(min(j - p, q - j) == min_dis) {
                    v_min.push_back(j);
                    m_max[j] = max(j - p, q - j);
                }
            }
            
            if(v_min.size() == 1) {
                v[v_min[0]] = 'o';
                max_dis = m_max[v_min[0]];
            } else {
                max_dis = INT64_MIN;
                for (int m = 0; m < v_min.size(); m++) {
                    if (m_max[v_min[m]] > max_dis) {
                        max_dis = m_max[v_min[m]];
                        v_max.clear();
                        v_max.push_back(v_min[m]);
                    } else if(m_max[v_min[m]] == max_dis) {
                        v_max.push_back(v_min[m]);
                    }
                }
                v[v_max[0]] = 'o';
            }
            
            if (i == N - 1) {
                cout << "Case #" << rnd << ": " << max_dis - 1 << " " << min_dis - 1 << endl;
            }
        }
    }
    
    return 0;
}
