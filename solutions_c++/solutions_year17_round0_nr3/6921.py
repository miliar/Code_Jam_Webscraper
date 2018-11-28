#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    int t = 0;
    cin >> t;
    for (int i=1; i<=t; i++) {
        std::priority_queue<int> q;
        unsigned long long N;
        unsigned long long K;
        unsigned long long min;
        unsigned long long max;
        cin >> N >> K;
        q.push(N);
        while (K > 0) {
            unsigned long long temp = q.top();
            q.pop();
            if (temp % 2 == 1) {
                max = temp / 2;
                min = max;
            } else {
                max = temp / 2;
                min = max - 1;
            }
            if (min > 0) q.push(min);
            if (max > 0) q.push(max);
            K--;
        }
        cout << "Case #" << i << ": " << max << " " << min << endl;
    }
    return 0;
}
