#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int N, K;
        cin >> N >> K;
        ld u;
        cin >> u;
        map<ld, int> M;
        for (int i = 0; i < N; i++)
        {
            long double x;
            cin >> x;
            M[x]++;
        }
        while(u > 0)
        {
            ld m = M.begin()->first;
            int c = M.begin()->second;
            M.erase(M.begin());
            if (c != N)
            {
                ld ne = M.begin()->first;
                ld req = c*(ne-m);
                if (u >= req)
                {
                    u -= req;
                    M[ne] += c;
                }
                else
                {
                    ne = m + u/c;
                    u = 0;

                    M[ne] += c;
                }
            }
            else
            {
                //cerr << c << " at " << m << ", " << u << " remaining" << endl;
                ld ne = m + u/c;
                u = 0;


                M[ne] += c;
            }
        }
        ld P = 1;
        for (auto pa : M)
        {
            //cerr << "res: " << pa.second << " x " << pa.first << endl;
            for (int i = 0; i < pa.second; i++)
                P *= pa.first;
        }
        cout << "Case #" << t+1 << ": " << setprecision(10) << P <<  endl;
    }
}
