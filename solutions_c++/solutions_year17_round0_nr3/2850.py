
#include <bits/stdc++.h>

using namespace std;

long long getLeftSpan(long long span) {
    return (span - 1) / 2;
}

long long getRightSpan(long long span) {
    return span / 2;
}

int main() {

    int T;
    cin >> T;

    for(int t = 1; t <= T; t++) {
        long long n, k;
        cin >> n >> k;

        priority_queue<long long> areas; // Store available areas in descending order
        map<long long, long long> quantity; // Store quantities available of each area type in 'areas' pq
        long long toLeft, toRight;

        areas.push(n);
        quantity[n] = 1;

        while(k > 0) {
            long long area = areas.top();
            areas.pop();
            long long amount = quantity[area];
            quantity.erase(area);

            k -= amount;

            toLeft = getLeftSpan(area);
            toRight = getRightSpan(area);

            if(quantity.find(toLeft) != quantity.end()) {
                quantity[toLeft] += amount;
            } else {
                quantity[toLeft] = amount;
                areas.push(toLeft);
            }

            if(quantity.find(toRight) != quantity.end()) {
                quantity[toRight] += amount;
            } else {
                quantity[toRight] = amount;
                areas.push(toRight);
            }
        }
        cout << "Case #" << t << ": " << max(toLeft, toRight) << " " << min(toLeft, toRight) << endl;
    }

    return 0;
}