#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream cin("t.in");
    ofstream cout("output.txt");
    int t;
    cin >> t;
    for (int tk = 0; tk < t; ++tk)
    {
        int n, p;
        cin >> n >> p;
        vector <int> A(n);
        vector <int> B(p);
        cout << "Case #" << tk + 1 << ": ";
        for (int i = 0; i < n; ++i)
        {
            cin >> A[i];
            ++B[A[i] % p];
        }
        if (p == 2)
        {
            cout << B[0] + (B[1] - 1) / 2 + min(B[1], 1) << endl;
        }
        else if (p == 3)
        {
            cout << B[0] + min(B[1], B[2]) + (max(B[1], B[2]) - min(B[1], B[2]) - 1) / 3 + min(1, max(B[1], B[2]) - min(B[1], B[2])) << endl;
        }
    }
    return 0;
}
