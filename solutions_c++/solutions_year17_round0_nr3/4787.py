#include <iostream>
#include <map>
#include <stdint.h>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int64_t N, K;
        cin >> N >> K;

        map<int64_t, int64_t> m;
        m[N] = 1;
        while(true)
        {
            map<int64_t, int64_t>::iterator it = --m.end();
            int64_t sz = it->first;
            int64_t freq = it->second;

            if (freq >= K)
            {
                cout << "Case #" << t + 1 << ": " << (sz / 2) << " " << ((sz - 1) / 2) << endl;
                break;
            }

            K -= freq;
            m.erase(it);
            m[sz / 2] += freq;
            m[(sz - 1) / 2] += freq;
        }
    }
}
