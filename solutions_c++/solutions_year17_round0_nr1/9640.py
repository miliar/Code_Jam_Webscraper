#include "main.h"
#include <iostream>

using namespace std;

// private funcs
int solveCase(string arrPancake, int arrSize, int K);
int checkIfStringOk(string arrPancake, int arrSize, int K);


//Functions impl
int main()
{
    int T, K;
    string S = "++---+-+";

    cin >> T;
    for(int i= 0; i<T; i++)
    {
        cin >> S >> K;
        int numofFlips = solveCase(S, S.length(),K);
        if(numofFlips == -1)
        {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": " << numofFlips << endl;
        }

    }




    return 0;
}

int solveCase(string arrPancake, int arrSize, int K)
{
    int numOfFlips = 0;

    for(int i = 0; i<=(arrSize-K); i++)
    {
        if (arrPancake[i] == '-')
        {
            for(int j =0; j<K; j++)
            {
                if(arrPancake[i+j] == '-')
                {
                    arrPancake[i+j] = '+';
                }
                else
                {
                    arrPancake[i+j] = '-';
                }
            }
            numOfFlips++;
        }
    }
    if(!checkIfStringOk(arrPancake, arrSize, K))
        numOfFlips = -1;

    return numOfFlips;
}

int checkIfStringOk(string arrPancake, int arrSize, int K)
{
    for(int i = arrSize-K; i<arrSize; i++)
    {
        if(arrPancake[i] == '-')
            return 0;
    }
    return 1;
}
main::main()
{
    //ctor
}

main::~main()
{
    //dtor
}
