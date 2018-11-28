#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

long long int calcTidy (long long int *ptr, int numOfDigits){
    long long int tidy;
    int i = 0;
    tidy = *ptr * 10 + *(ptr+1);
    for (int i = 2; i < numOfDigits; i++){
        tidy = tidy * 10 +  *(ptr+i);
    }
    return tidy;
}

void calcArr (long long int number, long long int *ptr, int numOfDigits) {
    int i = numOfDigits;
    int mod;
    while (number != 0){
        mod = number % 10;
        number /= 10;
        *(ptr+numOfDigits-1) = mod;
        numOfDigits--;
    }
}

int calc (long long int number){
    int count = 0;
    while (number != 0){
        number /= 10;
        count++;
    }
    cout << count << endl;
return count;
}

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("B-small-attempt1.in", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file 'A-sample'" << endl;
        exit(10);
    }

    fout.open("B-small-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file 'A-sample-answer'" << endl;
        exit(10);
    }

    int T, numOfDigits;
    long long int number, refNumber, tidy;

    fin >> T;

    for (int i = 0; i < T; i++){
        fin >> refNumber;
        number = refNumber;
        tidy = refNumber;

        numOfDigits = calc (number);

        if (numOfDigits == 1){
            tidy = refNumber;
        }
        else{
            long long int arrNumber[numOfDigits] = {0};
            calcArr (number, &arrNumber[0], numOfDigits);

            long long int *ptr = &arrNumber[0];

            for (int i = 0; i < numOfDigits-1; i++){
                if (arrNumber[i] > arrNumber[i+1]){
                    arrNumber[i]--;
                    if (arrNumber[i] == 0){
                        for (int i = 0; i < numOfDigits-1; i++){
                            arrNumber[i] = 9;
                        }
                        tidy = calcTidy(&arrNumber[0], numOfDigits-1);
                    }
                    else{
                        if(arrNumber[i] < arrNumber[i-1]){
                            int j = 0;
                            int dummy = arrNumber[i];
                            for (int j = i; j > 0 & dummy < arrNumber[j-1]; j--){
                                arrNumber[j] = 9;
                            }
                            arrNumber[j] = dummy;
                        }
                        while (i < numOfDigits){
                            i++;
                            arrNumber[i] = 9;
                        }
                        tidy = calcTidy(&arrNumber[0], numOfDigits);
                    }
                    i = numOfDigits;
                }
            }
        }
    fout << "Case #" << i+1 << ": " << tidy << endl;
    }


    fin.close();
    fout.close();

    return 0;
}
