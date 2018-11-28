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
        long long a;
        cin >> a;
        vector <int> A;
        while (a > 0)
        {
            A.push_back(a % 10);
            a /= 10;
        }
        reverse(A.begin(), A.end());
    for (int tq = 0; tq < 20; ++tq)
    {
        for (int i = 1; i < A.size(); ++i)
        {
            if (A[i] < A[i - 1])
            {
                --A[i - 1];
                for (int j = i; j < A.size(); ++j)
                {
                    A[j] = 9;
                }
            }
        }
    }
        cout << "Case #" << te + 1 << ": ";
        int st = 0;
        if (A[0] == 0)
        {
            ++st;
        }
        for (; st < A.size(); ++st)
        {
            cout << A[st];
        }
        cout << endl;
    }
    return 0;
}
