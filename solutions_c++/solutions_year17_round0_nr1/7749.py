#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin >> t;
    for (int te = 0; te < t; ++te)
    {
        string s;
        int k;
        cin >> s >> k;
        int ind = -k;
        int cnt = 0;
        vector <int> A(s.size());
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '+')
            {
                A[i] = 1;
            }
            else
            {
                A[i] = -1;
            }
        }
        for (int i = 0; i + k <= s.size(); ++i)
        {
            if (A[i] == -1)
            {
                ++cnt;
                for (int j = i; j < i + k; ++j)
                {
                    A[j] *= -1;
                }
            }
        }
        cout << "Case #" << te + 1 << ": ";
        if (*min_element(A.begin(), A.end()) == -1)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << cnt << endl;
        }
    }
    return 0;
}
