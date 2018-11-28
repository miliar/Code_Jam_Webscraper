#include <iostream>
#include <map>
using namespace std;

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas)
    {
        cout << "Case #" << cas << ": ";
        long long n, k;
        cin >> n >> k;
        map<long long, long long, std::greater<long long>> qtt;
        qtt[n] = 1;

        while (true)
        {
            auto it = qtt.begin();
            if (it->second >= k)
            {
                cout << it->first / 2 << " " << (it->first - 1) / 2 << endl;
                break;
            }
            else
            {
                k -= it->second;
                qtt[it->first / 2] += it->second;
                qtt[it->first % 2 == 1 ? it->first / 2 : (it->first / 2 - 1)] += it->second;
                qtt.erase(it);
            }
        }
    }
}
