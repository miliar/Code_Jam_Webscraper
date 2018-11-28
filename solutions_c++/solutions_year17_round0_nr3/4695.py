#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

void bathroomStalls(uint64_t n, uint64_t k, uint64_t& min, uint64_t& max)
{
    priority_queue<uint64_t> q;
    q.push(n);

    for(uint64_t i = 0; i < k; i++)
    {
        uint64_t a = q.top(); q.pop();
        if((a % 2) == 0)
        {
            max = a/2;
            min = a/2 - 1;
        }
        else
        {
            min = max = a/2;
        }

        if(max > 0)
            q.push(max);
        if(min > 0)
            q.push(min);
    }
}

int main()
{
    int t; cin >> t;

    for(int i = 0; i < t; i++)
    {
        uint64_t n, k; cin >> n >> k;

        uint64_t min, max;
        bathroomStalls(n, k, min, max);

        cout << "Case #" << (i + 1) << ": " << max << " " << min << endl;
    }
}