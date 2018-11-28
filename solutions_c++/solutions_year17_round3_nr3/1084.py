#include <iostream>
#include <math.h>
#include <fstream>
#include <string>
#include <inttypes.h>
#include <iomanip>

using namespace std;

void inserter (double P[], double &U)
{
    int64_t i, number;
    if (U < 0.0000001)
        U = 0;
    cout << U << " " << P[49] << " " << P[50] << endl;
    for (i = 0; i < 52; i++)
    {
        if (P[i] != P[i + 1])
            break;
    }
    number = i + 1;
    //cout << number << endl;
    if (U >= ((P[number] - P[number - 1]) * number))
    {
        U -= (P[number] - P[number - 1]) * number;
        for (i = 0; i < number; i++)
        {
            P[i] = P[number];
        }
    }
    else
    {
        for (i = 0; i < number; i++)
        {
            P[i] += (U / number);
        }
        U = 0;
    }
}

void sortByScore(double array[])
{
    int64_t i, j, index;                                 //Variables declaration
    double temp, maxi;

    for (i = 0; i < 50; i++)
    {
        index = i;
        maxi = array[i];
        for (j = i; j < 51; j++)                          //Running loop to find the largest element
            if (maxi > array[j])
            {
                maxi = array[j];
                index = j;
            }

        temp = array[index];                                     //Exchanging max element with i'th element
        array[index] = array[i];
        array[i] = temp;
    }
}

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int64_t i, j, N, K, T;
    double P[52], U, prob;
    filin >> T;
    for (i = 0; i < T; i++)
    {
        prob = 1;
        filout << "Case #" << i + 1 << ": ";
        filin >> N >> K;
        for (j = 0; j < 51; j++)
        {
            P[j] = 1.0;
        }
        P[51] = 2.0;
        filin >> U;
        for (j = 0; j < N; j++)
        {
            filin >> P[j];
        }
        sortByScore (P);
        while (U > 0.0)
        {
            inserter (P, U);
        }
        for (j = 0; j < N; j++)
        {
            prob *= P[j];
        }
        cout << i + 1;
        filout << std::fixed;
        filout << std::setprecision (6) << prob;
        filout << endl;
    }
    filin.close ();
    filout.close ();
}
