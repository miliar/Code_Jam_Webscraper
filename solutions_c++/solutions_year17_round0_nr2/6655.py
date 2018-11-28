#include <iostream>

using namespace std;

long long reduce(long long q)
{
        int d[20];
        long long qq = q;
        int n = 0;
        while (q)
        {
            d[n++] = q % 10;
            q /= 10;
        }
        int s = -1;
        for (int i = n-1; i>0; i--)
        {
            if (d[i] > d[i-1])
            {
                s = i-1;
                break;
            }
        }
        if (s == -1)
        {
            return qq;
        }
        else
        {
            long long v = 0;
            for (int i = s; i>=0; i--)
                v = v*10 + d[i];
            return reduce(qq - v - 1);
        }
}

int main()
{
    int N;
    cin >> N;

    for (int t = 1; t<=N; t++)
    {
        long long q;
        cin >> q;
        cout << "Case #" << t << ": " << reduce(q) << endl;
    }
}
