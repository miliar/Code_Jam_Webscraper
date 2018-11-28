#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

tuple<long long, long long> solve(long long n,long long k) {
    long long counter = 0;
    queue<long long> que;
    que.push(n);
    for (;;) {
        long long x = que.front();
        long long counter2 = 0;
        for (; x == que.front();)
        {
            counter2++;
            counter++;
            que.pop();
                if (que.empty())
                {
                    break;
                }
        }
        if (counter >= k)
        {
            if ((x-1)%2 == 0)
            {
                return forward_as_tuple((x - 1) / 2, (x - 1) / 2);
            }
            else
            {
                return forward_as_tuple((x - 1) / 2 + 1, (x - 1) / 2);
            }
        }
       
        if ((x - 1) % 2 == 0)
        {
            for (long long j = 0; j < counter2; j++)
            {
                que.push((x - 1) / 2);
                que.push((x - 1) / 2);
            }
        }
        else
        {
            for (long long j = 0; j < counter2; j++)
            {
                que.push((x - 1) / 2 + 1);
            }
            for (long long j = 0; j < counter2; j++)
            {
                que.push((x - 1) / 2);
            }
        }
        

    }
}

void main() {
    int t;
    long long n, k;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> k;
        long long maxx, minx;
        tie(maxx,minx) = solve(n,k);
        cout << "Case #" << (i + 1) << ": " << maxx << " " << minx << endl;
    }
}