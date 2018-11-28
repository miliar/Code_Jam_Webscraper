#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<long long> d;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    long long t, i, j, k, n;
    cin >> t;
    for (i = 0; i < t; i++)
    {
        cin >> n;
        d.clear();
        long long cur = n;
        while (cur > 0)
        {
            d.push_back(cur%10);
            cur /= 10;
        }
        bool check = true;
        while (check)
        {
            check = false;
            for (j = (long long)d.size() - 2; j >= 0; j--)
                if (d[j] < d[j+1])
                {
                    check = true;
                    d[j+1]--;
                    for (k = 0; k <= j; k++)
                        d[k] = 9;
                    break;
                }
        }
        if (d.back() == 0)
            d.pop_back();
        cout << "Case #" << i+1 << ": ";
        for (j = d.size() - 1; j >= 0; j--)
            cout << d[j];
        cout << endl;
    }
    return 0;
}
