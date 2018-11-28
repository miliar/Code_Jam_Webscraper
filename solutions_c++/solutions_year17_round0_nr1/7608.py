#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        string S;
        int K;

        cin >> S;
        cin >> K;

        int flips = 0;
        bool impossible = false;
        for (size_t i = 0; i < S.size(); i++)
        {
            if (S[i] == '+')
                continue;
            if (i+K > S.size())
            {
                int count = 0;
                for (int k = i; k < S.size(); k++)
                    if (S[k] == '+')
                        count++;
                if (count != K)
                    impossible = true;
                break;
            }
            for (int k = i; k < i+K; k++)
            {
                if (k==i)
                    flips++;
                S[k] = (S[k] == '-') ? '+' : '-';
            }
        }

        if (impossible)
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << t+1 << ": " << flips << endl;
    }
}
