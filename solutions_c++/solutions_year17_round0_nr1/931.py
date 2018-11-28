#include <iostream>
#include <string>
#include <fstream>
#include <inttypes.h>

using namespace std;

void multiplier (int array[], int index, int k, int &counter)
{
    if (array[index] == -1)
    {
        counter++;
        for (int i = 0; i < k; i++)
            array[index + i] *= (-1);
    }
}

int sum (int array[], int len)
{
    int sum = 0;
    for (int i = 0; i < len; i++)
        sum += array[i];
    return sum;
}

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int i, j, k, T, len, array [1000], counter;
    string S;
    filin >> T;
    for (i = 0; i < T; i++)
    {
        cout << i + 1 << endl;
        counter = 0;
        filin >> S >> k;
        filout << "Case #" << i + 1 << ": ";
        len = S.length ();
        for (j = 0; j < len; j++)
            if (S[j] == '+')
                array[j] = 1;
            else
                array[j] = -1;
        for (j = len; j < 1000; j++)
            array[j] = 0;
        for (j = 0; j < len - k + 1; j++)
            multiplier (array, j, k, counter);
        if (sum(array, len) != len)
            filout << "IMPOSSIBLE" << endl;
        else
            filout << counter << endl;
    }
    filin.close ();
    filout.close ();
    return 0;
}
