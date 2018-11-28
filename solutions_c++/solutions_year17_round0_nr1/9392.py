#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

bool detectChange(char *arr, int flipperSize, int arrayStackSize) {
    bool blankSide = 0;
    for (int i = 0; i < flipperSize; i++){
        if (*(arr+i) == '-'){
            blankSide = 1;
            i = flipperSize;
        }
    }
    return blankSide;
}

int flip (char *arr, int flipperSize, int numOfFlips){
    if (*arr == '-'){
        for (int i = 0; i < flipperSize; i++){
            if (*(arr+i) == '-'){
                *(arr+i) = '+';
            }
            else {
                *(arr+i) = '-';
            }
        }
        numOfFlips++;
    }
return numOfFlips;
}

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-large.in", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file 'A-sample'" << endl;
        exit(10);
    }

    fout.open("A-large-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file 'A-sample-answer'" << endl;
        exit(10);
    }

    int T, numOfFlips, flipperSize, arrayStackSize, arrayStackIndex, *ptr;
    bool blankSide;
    string stack;
    string::iterator iterStack;

    fin >> T;

    for (int i = 0; i < T; i++){
        fin >> stack;
        fin >> flipperSize;
        arrayStackSize = stack.length();

        char arrayStack[arrayStackSize];
        iterStack = stack.begin();
        int arrayStackIndex = 0;
        bool blankSide = 0;

        for (iterStack; iterStack != stack.end(); iterStack++){
            arrayStack [arrayStackIndex] = *iterStack;
            arrayStackIndex++;
        }

        numOfFlips = 0;
        arrayStackIndex = 0;

        if (arrayStackSize == flipperSize){
            numOfFlips = flip (&arrayStack[arrayStackIndex], flipperSize, numOfFlips);
            for (int i = 0; i < flipperSize; i++){
            }
            blankSide = detectChange(&arrayStack[0], flipperSize, arrayStackSize);
            if (blankSide){
                numOfFlips = -1;
            }
        }
        else {
            for (int i = 0; i < arrayStackSize-flipperSize+1; i++){
                numOfFlips = flip (&arrayStack[arrayStackIndex], flipperSize, numOfFlips);
                arrayStackIndex++;
            }
            blankSide = detectChange(&arrayStack[arrayStackIndex-1], flipperSize, arrayStackSize);
            if (blankSide){
                numOfFlips = -1;
            }
            for (int i = 0; i < arrayStackSize; i++){
            }
        }

        if (numOfFlips == -1){
            for (int i = 0; i < arrayStackSize; i++){
                //cout << arrayStack[i];
            }
            //cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
            fout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
        else {
            for (int i = 0; i < arrayStackSize; i++){
            //cout << arrayStack[i];
            }
            //cout << "Case #" << i+1 << ": " << numOfFlips << endl;
            fout << "Case #" << i+1 << ": " << numOfFlips << endl;
        }
    }

    fin.close();
    fout.close();

    return 0;
}
