#include <cstdio>
#include <iostream>

using namespace std;

char a[1111];

int main()
{
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; tt++)
    {
        for (int i = 0; i < 1111; i++) a[i] = 'x';
        int N;
        cin >> N;
        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V;
        printf("Case #%d: ", tt);
        if (R > N / 2 || Y > N / 2 || B > N / 2)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        char c = 'x';
        int MAX = 0;
        if (MAX < R)
        {
            MAX = R;
            c = 'R';
        }

        if (MAX < Y)
        {
            MAX = Y;
            c = 'Y';
        }

        if (MAX < B)
        {
            MAX = B;
            c = 'B';
        }

        for (int i = 0; i < MAX; i ++)
        {
            a[i * 2] = c;
        }


        if (c == 'R')
        {
            R = 0;
        }

        if (c == 'Y')
        {
            Y = 0;
        }

        if (c == 'B')
        {
            B = 0;
        }

        //cout << R << ' ' << Y << ' ' << B << endl;

        for (int i = 0; i < N; i++)
        {
            if (a[i] != 'x')
            {
                continue;
            }

            char c = 'x';
            int MAX = 0;
            if (MAX < R && a[i-1] != 'R')
            {
                MAX = R;
                c = 'R';
            }

            if (MAX < Y && a[i-1] != 'Y')
            {
                MAX = Y;
                c = 'Y';
            }

            if (MAX < B && a[i-1] != 'B')
            {
                MAX = B;
                c = 'B';
            }

            if (c == 'R')
            {
                R--;
            }

            if (c == 'Y')
            {
                Y--;
            }

            if (c == 'B')
            {
                B--;
            }
            a[i] = c;
        }

        for (int i = 0; i < N; i++) {
            printf("%c", a[i]);
        }

        cout << endl;
    }

    return 0;
}
