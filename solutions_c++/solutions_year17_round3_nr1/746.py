#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("a.in");
    ofstream cout("output.txt");
    int T;
    cin >> T;
    for (int Tk = 0; Tk < T; ++Tk)
    {
        int n, k;
        cin >> n >> k;
        vector <double> R(n), H(n);
        vector <pair <double, double> > A(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> A[i].first >> A[i].second;
        }
        sort(A.rbegin(), A.rend());
        double sq = 0;
        for (int i = 0; i < n - k + 1; ++i)
        {
            vector <double> S;
            for (int j = 1; i + j < n; ++j)
            {
                S.push_back(A[i + j].first * A[i + j].second);
            }
            sort(S.rbegin(), S.rend());
            double sum = 0;
            for (int j = 0; j < k - 1; ++j)
            {
                sum += S[j];
            }
            sum += A[i].first * A[i].second;
            sq = max(sq, sum * 2 * M_PI + M_PI * A[i].first * A[i].first);
        }
        cout.precision(26);
        cout << "Case #" << Tk + 1 << ": ";
        cout << sq << endl;
    }
    return 0;
}
