#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T;
    ifstream cin("in.in");
    ofstream cout("out.txt");
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int N, P;
        cin >> N >> P;
        int C[P];
        for (int i = 0; i < P; i++)
            C[i] = 0;
        for (int i = 0; i < N; i++)
        {
            int s;
            cin >> s;
            C[s%P]++;
        }
        int res = 0;
        if (P == 2)
        {
            res = C[0] + C[1]/2 + C[1]%2;
        }
        else if (P == 3)
        {
            res = C[0];
            int m = min(C[1], C[2]);
            res += m;
            C[1] -= m;
            C[2] -= m;
            res += C[1]/3;
            res += C[2]/3;
            if (C[1]%3 || C[2]%3)
                res++;
        }
        cout << "Case #" << t+1 << ": " << res << endl;
    }
}
