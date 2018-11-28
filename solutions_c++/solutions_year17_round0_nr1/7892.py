#include <iostream>
#include <string>

// Operation is commutative. Left-to-right greedy solution is optimal.

using namespace std;

int main()
{
    unsigned int T; // Number of test cases
    cin >> T;
    for(unsigned int i = 1; i <= T; ++i)
    {
        string S; // pancake state
        unsigned int K, flips = 0; // size of spatula in consecutive pancakes, number of flips
        bool impossible = false;
        cin >> S >> K;
        for(unsigned int j = 0; j + K <= S.length(); ++j)
        {
            if(S[j] != '+')
            {
                ++flips;
                for(unsigned int k = j; k < j + K; ++k) // don't get k and K confused; k?
                    if(S[k] == '+')
                        S[k] = '-';
                    else
                        S[k] = '+';
            }
        }
        for(unsigned int j = S.length() + 1 - K; j < S.length() && !impossible; ++j)
            if(S[j] != '+')
                impossible = true;
        cout << "Case #" << i << ": ";
        if(impossible)
            cout << "IMPOSSIBLE";
        else
            cout << flips;
        cout << '\n';
    }
    return 0;
}
