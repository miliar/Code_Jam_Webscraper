#include <iostream>
#include <math.h>
#include <fstream>
#include <string>
#include <inttypes.h>

using namespace std;

int main()
{
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    int64_t i, j, k, T, N, R, O, Y, G, B, V, counter = 0;
    char temp, cannot = 'P', order[3], blood = 'P', array[1000];
    filin >> T;
    for (i = 0; i < T; i++)
    {
            cout << i + 1 << endl;
            cannot = 'P';
            blood = 'P';
            filout << "Case #" << i + 1 << ": ";
            filin >> N >> R >> O >> Y >> G >> B >> V;
            //Small Input
            counter = N;
            if (R > N / 2 || Y > N / 2 || B > N / 2)
                filout << "IMPOSSIBLE";
            else
            {
                for (j = 0; j < R; j++)
                {
                    array[j] = 'R';
                }
                for (; j < B + R; j++)
                {
                    array[j] = 'B';
                }
                for (; j < N; j++)
                {
                    array[j] = 'Y';
                }
                for (j = 0; j < 1000000; j++)
                {
                    if (array[j % N] == array[(j + 1) % N])
                    {
                        temp = array [(j + 1) % N];
                        array[(j + 1) % N] = array[(j + 2) % N];
                        array[(j + 2) % N] = temp;
                    }
                }
                for (j = 0; j < N; j++)
                {
                    filout << array[j];
                }
            }
            /*
            else
            {
                while (R + B + Y > 2)
                {
                if (cannot == 'R')
                {
                    if (B >= Y)
                    {
                        filout << 'B';
                        B--;
                        cannot = 'B';
                    }
                    else
                    {
                        filout << 'Y';
                        Y--;
                        cannot = 'Y';
                    }
                }
                else if (cannot == 'B')
                {
                    if (R >= Y)
                    {
                        filout << 'R';
                        R--;
                        cannot = 'R';
                    }
                    else
                    {
                        filout << 'Y';
                        Y--;
                        cannot = 'Y';
                    }
                }
                else if (cannot == 'Y')
                {
                    if (R >= B)
                    {
                        filout << 'R';
                        R--;
                        cannot = 'R';
                    }
                    else
                    {
                        filout << 'B';
                        B--;
                        cannot = 'B';
                    }
                }
                else
                {
                    if (R >= B)
                    {
                        if (R >= Y)
                        {
                            filout << 'R';
                            R--;
                            cannot = 'R';
                            blood = 'R';
                        }
                        else
                        {
                            filout << 'Y';
                            Y--;
                            cannot = 'Y';
                            blood = 'Y';
                        }
                    }
                    else
                    {
                        if (B >= Y)
                        {
                            filout << 'B';
                            B--;
                            cannot = 'B';
                            blood = 'B'
                        }
                        else
                        {
                            filout << 'Y';
                            Y--;
                            cannot = 'Y';
                            blood = 'Y';
                        }
                    }
                }
                }
                if (blood == 'P')
                {
                    if (R + B == 2)
                    {
                        if (cannot == 'R')
                        {
                            filout << "BR";
                        }
                        else
                        {
                            filout << "RB";
                        }
                    }
                }
            }
            */
            filout << endl;
    }
    filin.close ();
    filout.close ();
}
