#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <queue>
#include <map>

using namespace std;


int main() {
    freopen("input_c_2.txt", "r", stdin);
    freopen("output_c_2.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
                
        long long n, k;
        cin >> n >> k;
        priority_queue<pair<long long, long long> > Q;
        map<pair<long long, long long>, long long> Mp;
        Q.push(make_pair(n - (n + 1) / 2, (n + 1) / 2 - 1));
        Mp[make_pair(n - (n + 1) / 2, (n + 1) / 2 - 1)] = 1;
        k--;
        while (k > 0) {
            long long a = Q.top().first;
            long long b = Q.top().second;                    
            long long c = Mp[make_pair(a, b)];
            //cout << a << " " << b << " " << c << endl;
            if (c > k) {
                k = 0;
                break;
            } else {
                Q.pop();
                k -= c;
                if (a != 0) {
                    if (Mp[make_pair(a - (a + 1) / 2, (a + 1) / 2 - 1)] == 0) {
                        Q.push(make_pair(a - (a + 1) / 2, (a + 1) / 2 - 1));
                    }
                    Mp[make_pair(a - (a + 1) / 2, (a + 1) / 2 - 1)] += c;
                }

                if (b != 0) {
                    if (Mp[make_pair(b - (b + 1) / 2, (b + 1) / 2 - 1)] == 0) {
                        Q.push(make_pair(b - (b + 1) / 2, (b + 1) / 2 - 1));
                    }
                    Mp[make_pair(b - (b + 1) / 2, (b + 1) / 2 - 1)] += c;
                }
            }
        }
        cout << Q.top().first << " " << Q.top().second << endl;
    } 
    return 0;
}