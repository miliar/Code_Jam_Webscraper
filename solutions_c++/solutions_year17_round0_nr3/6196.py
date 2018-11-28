#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("C-large.in");
    ofstream out("output.txt");

    int T;
    __int64 K, N;

    in >> T;

    for (int i = 1; i <= T; i++)
    {
        out << "Case #" << i << ": ";
        in >> N >> K;
        __int64 tmp = 1, SS, MM;
        while (tmp - 1 < K) tmp *= 2;
        tmp--;

        if (tmp >= N) out << 0 << " " << 0 << endl;
        else
        {
            N -= tmp;
            K -= tmp / 2;
            tmp++;

            SS = N / tmp, MM = N % tmp;
            if (MM < K) out << SS << " " << SS << endl;
            else if (MM > tmp / 2 && MM - tmp / 2 >= K) out << SS + 1 << " " << SS + 1 << endl;
            else out << SS + 1 << " " << SS << endl;
        }
    }

    return 0;
}
