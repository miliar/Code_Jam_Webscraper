#include <iostream>
using namespace std;
bool is_tidy(int n)
{
    bool result = true;

    while (n >= 10)
    {
        int last = n % 10;
        int next_n = n / 10;
        int second_last = next_n % 10;
        if (last >= second_last)
        {
            n = next_n;
            continue;
        }
        else
        {
            result = false;
            break;
        }
    }

    return result;
}

int main()
{
    int T(0);
    cin >> T;
    int max_tidy[100] = {};
    int max_tidy_count(0);
    for (int i = 0; i < T; i++)
    {
        int N(0);
        cin >> N;
        for (int j = N; j > 0; j--)
        {
            if (is_tidy(j))
            {
                max_tidy[max_tidy_count++] = j;
                break;
            }
        }
    }

    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": " << max_tidy[i] << endl;
    }

    return 0;
}
