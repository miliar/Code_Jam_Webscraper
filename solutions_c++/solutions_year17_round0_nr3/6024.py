#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::endl;

int main()
{
    int64_t T;
    int64_t N, k;
    int64_t max, min;
    std::string pattern = "Case #";
    std::string tmp;
    cin >> T;
    std::priority_queue<int64_t> pq;
    for (int64_t i = 0; i < T; ++i)
    {
        {
            std::priority_queue<int64_t> tmp;
            pq.swap(tmp);
        }
        tmp = pattern;
        cin >> N >> k;
        pq.push(N);
        for (int64_t j = 0; j < k - 1; ++j)
        {
            int64_t tmp = pq.top();
            pq.pop();
            pq.push(tmp / 2);
            if (tmp % 2)
                pq.push(tmp / 2);
            else
                pq.push(tmp / 2 - 1);
        }
        int64_t end = pq.top();
        max = end / 2;
        min = (end % 2) ? end / 2 : end / 2 - 1;
        tmp += std::to_string(i + 1);
        tmp += ": ";
        tmp += std::to_string(max);
        tmp += " ";
        tmp += std::to_string(min);
        cout << tmp << endl;
    }
}
