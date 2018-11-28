#include <iostream>
#include <queue>
#include <map>

using namespace std;

typedef unsigned long long ULL;

int T;

ULL N, K;


int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> N >> K;
        map<ULL, ULL> m;
        priority_queue<ULL> pq;
        m[N] = 1;
        pq.push(N);
        while(K > m[pq.top()])
        {
            ULL len = pq.top();
            ULL num = m[len];
            ULL x = len / 2;
            ULL y = (len - 1) / 2;

            pq.pop();
            m.erase(len);
            if (m.find(x) == m.end()) pq.push(x);
            if (m.find(y) == m.end()) pq.push(y);
            m[x] += num;
            m[y] += num;
            K -= num;
        }
        cout << "Case #" << t << ": " << pq.top() / 2 << " " << (pq.top() - 1) / 2 << endl;
    }
    return 0;
}