#include <iostream>
#include <map>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        size_t n, k;
        cin >> n >> k;
        std::map<size_t, size_t> p;

        p[n] = 1;

        for (size_t j = 1; j < k;)
        {
            size_t r = p.rbegin()->first;
            size_t c = p.rbegin()->second;
            if (j + c <= k)
            {
                p[r / 2] += c;
                p[(r - 1) / 2] += c;
                p.erase(r);
                j += c;
            }
            else
            {
                j = k;
            }
        }
        size_t r = p.rbegin()->first;
        cout << "Case #" << (i + 1) << ": " << r / 2 << " " << (r - 1) / 2 << endl;
    }
    return 0;
}
