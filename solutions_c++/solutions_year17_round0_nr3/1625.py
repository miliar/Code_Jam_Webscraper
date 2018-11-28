#include <iostream>
#include <map>
#include <queue>
using namespace std;

unsigned long long maxRest(unsigned long long n) {
    return (n / 2);
}

unsigned long long minRest(unsigned long long n) {
    return ((n - 1) / 2);
}

struct node {
    unsigned long long value;
    unsigned long long nums;
};

int main() {
    int t;
    unsigned long long n, k;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> k;
        
        priority_queue<unsigned long long> q;
        map<unsigned long long, unsigned long long> m;
        q.push(n);
        m.insert(pair<unsigned long long, unsigned long long>(n, 1));

        unsigned long long ansMax = 0;
        unsigned long long ansMin = 0;

        for (unsigned long long j = 0; j < k;) {
            unsigned long long value = q.top();
            unsigned long long nums = m[value];

            q.pop();
            m.erase(value);

            unsigned long long max = maxRest(value);
            unsigned long long min = minRest(value);

            if (j + nums >= k) {
                ansMax = max;
                ansMin = min;
                break;
            } else {
                map<unsigned long long, unsigned long long>::iterator maxIt = m.find(max);
                if (maxIt == m.end()) {
                    m.insert(pair<unsigned long long, unsigned long long>(max, nums));
                    q.push(max);
                } else {
                    maxIt->second = maxIt->second + nums;
                }

                map<unsigned long long, unsigned long long>::iterator minIt = m.find(min);
                if (minIt == m.end()) {
                    m.insert(pair<unsigned long long, unsigned long long>(min, nums));
                    q.push(min);
                } else {
                    minIt->second = minIt->second + nums;
                }
            }

            j += nums;
        }

        cout << "Case #" << i << ": " << ansMax << " " << ansMin << endl;
        /*
        for (unsigned long long j = 1; j < k; j++) {
            unsigned long long v = q.top();
            q.pop();
            q.push(maxRest(v));
            q.push(minRest(v));
        }

        unsigned long long last = q.top();
        unsigned long long max = maxRest(last);
        unsigned long long min = minRest(last);

        cout << "Case #" << i << ": " << max << " " << min << endl;
        */
    }
    return 1;
}
