#include <iostream>

using namespace std;

size_t solve(size_t n)
{
    size_t k = 1;
    while (n / k > 9)
    {
        k *= 10;
    }
    while (k > 1)
    {
        size_t k2 = k / 10;
        size_t a = n / k % 10;
        size_t b = n / k2 % 10;
        if (a > b)
        {
            return solve(n / k * k - 1);
        }

        k = k2;
    }
    return n;
}

int main()
{
    int T;

    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        size_t n;
        cin >> n;

        cout << "Case #" << (i + 1) << ": " << solve(n) << endl;
    }
    return 0;
}
