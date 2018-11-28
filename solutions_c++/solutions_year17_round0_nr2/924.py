#include <iostream>
#include <string>
#include <fstream>
#include <inttypes.h>

using namespace std;

int checker (int array[], int len)
{
    int i;
    for (i = 0; i < len - 1; i++)
        if (array[i] > array[i + 1])
            return i;
    return i + 1;
}

void changer (int array[], int len, int i)
{
    int j;
    for (j = i + 1; j < len; j++)
        array[j] = 9;
    array[i] = (array[i] + 9) % 10;
}

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int i, j, k, T, len, array[19];
    string S;
    filin >> T;
    for (i = 0; i < T; i++)
    {
        filin >> S;
        len = S.length ();
        filout << "Case #" << i + 1 << ": ";
        for (j = 0; j < len; j++)
            array[j] = S[j] - 48;
        while (checker (array, len) != len)
            changer (array, len, checker (array, len));
        for (j = len - 1; j >= 0; j--)
            if (array[j])
                k = j;
        for (j = k; j < len; j++)
            filout << array[j];
        filout << endl;
    }
    filin.close ();
    filout.close ();
    return 0;
}
