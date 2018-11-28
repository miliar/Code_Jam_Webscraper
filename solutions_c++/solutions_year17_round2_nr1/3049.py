#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    ifstream file_input("A-large.in", ios::in);
    ofstream file_output("A-large.out", ios::trunc | ios::out);

    if(file_input && file_output)
    {
        streambuf *cinbuf = std::cin.rdbuf();
        cin.rdbuf(file_input.rdbuf());
        streambuf *coutbuf = std::cout.rdbuf();
        cout.rdbuf(file_output.rdbuf());

        unsigned short T, t, N, n, S;
        unsigned long long K;
        double D, M, res;

        cin >> T;
        for(t = 1; t <= T; ++t)
        {
            cin >> D >> N;
            for(n = 0; n < N; ++n)
            {
                cin >> K >> S;
                if(n == 0) M = (D - K) / S;
                else M = max(M, (D - K) / S);
            }
            res = D / M;

            cout << "Case #" << t << ": " << fixed << setprecision(6) << res << endl;
        }
        cin.rdbuf(cinbuf);
        cout.rdbuf(coutbuf);

        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file(s) !" << endl;
    return 0;
}
