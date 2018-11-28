#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
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
        int N, C, M;
        cin >> N >> C >> M;
        map<int,int> C1;
        map<int,int> C2;
        int m1 = 0;
        int m1i = 0;
        int m2i = 0;
        int m2 = 0;
        int t1 = 0;
        int t2 = 0;
        for (int i = 0; i < M; i++)
        {
            int p, b;
            cin >> p >> b;
            if (b == 1)
            {
                C1[p]++;
                t1++;
                if (C1[p] > m1)
                {
                    m1 = C1[p];
                    m1i = p;
                }
            }
            if (b == 2)
            {
                C2[p]++;
                t2++;
                if (C2[p] > m2)
                {
                    m2 = C2[p];
                    m2i = p;
                }
            }
        }
        int r = max(t1, t2);
        r = max(r, C1[1]+C2[1]);
        int p = 0;
        for (int i = 1; i <= N; i++)
            p = max(p, C1[i]+C2[i]-r);
        //if (m1i == m2i)
        //    p = m1 + m2 - r;
        cout << "Case #" << t+1 << ": " << r << " " << p << endl;
    }
}
