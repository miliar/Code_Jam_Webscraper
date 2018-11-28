#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("B-small-attempt1.in");
    ofstream out("output.txt");

    int T, N;
    char st[20] = {};

    in >> T;

    for (int i = 1; i <= T; i++)
    {
        in >> N;

        do
        {
             itoa(N, st, 10);

             if (strlen(st) == 1) goto en;

             for (int j = 0; j < strlen(st) - 1; j++)
             {
                 if (st[j] > st[j + 1]) break;
                 if (j == strlen(st) - 2) goto en;
             }
        } while (N--);

        en:;
        out << "Case #" << i << ": " << N << endl;
    }

    return 0;
}
