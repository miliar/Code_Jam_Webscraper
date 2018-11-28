#include <iostream>

using namespace std;

bool tidy(int x)
{
    string s = to_string(x);
    if (s.size() == 1) return true;

    for (int i = 1; i < s.size(); ++i)
        if (s[i] < s[i - 1])
            return false;

    return true;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int N;
        cin >> N;

        for (int i = N; i >= 0; --i)
        {
            if (tidy(i))
            {
                cout << "Case #" << t + 1 << ": " << i << endl;
                break;
            }
        }
    }
}
