#include <iostream>
#include <string>
using namespace std;
#include <vector>
#include <fstream>
int main()
{
    int flips=0;
    int testCases=0;
    string pancakes ="";

    int flipperSize=0;

    vector <string> input1;     //modify according to input
    vector <int> input2;

    cin >> testCases;

    for (int i=0; i<testCases; i++){
        cin >> pancakes;
        cin >> flipperSize;
        input1.push_back(pancakes);
        input2.push_back(flipperSize);
    }
    //actual code starts here!
    for (int k=0; k<testCases; k++){
    	flips = 0;
        pancakes = input1[k];
        flipperSize = input2[k];
        int i;
        for (i=0; i < pancakes.size() - flipperSize + 1; i++){
            if (pancakes[i] == '-'){
                pancakes[i] = '+';
                flips++;
                for (int j=1; j<flipperSize; j++){
                    if ( pancakes[i+j] == '-'){
                        pancakes[i+j] = '+';
                    }
                    else {
                        pancakes[i+j] = '-';
                    }
                }
            }
            //cout << pancakes << endl;
        }
        bool flag = false;
        for (; i<pancakes.size(); i++){
            if (pancakes[i] == '-' ){
                flag = true;
            }
        }
        if (flag){
            cout << "Case #" << k+1 << ": " << "IMPOSSIBLE" <<endl;
        }
        else {
        cout << "Case #" << k+1 << ": " << flips << endl;
        }
    }

    return 0;
}
