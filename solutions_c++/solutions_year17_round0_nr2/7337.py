#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string findTidy(string numStr) {
    if(numStr.length() <= 1){
        return numStr;
    }

    // get return value in array
    int prevI = numStr.length() - 1;
    for(int i = numStr.length() - 2; i>=0; i--){
        if(numStr[prevI] < numStr[i]){
            numStr[prevI] = '9';
            if(numStr[i]=='0'){
                numStr[i] = '9';
            } else {
                numStr[i] = numStr[i]-1;
            }
        }
        prevI--;
    }

    // go through array and return a value
    if(numStr[0]=='0') numStr.erase(numStr.begin());
    bool turn9 = false;
    for(int i = 0; i<numStr.length(); i++){
        if(turn9){
            numStr[i] = '9';
        }
        if(numStr[i] == '9') {
            turn9 = true;
        }
    }
    return numStr;
}

void flipFileReadHelper(ifstream* fileStream) {
    int inputNum = 0;
    (*fileStream) >> inputNum;
    for (int i = 0; i < inputNum ; i++) {
        string numStr;
        (*fileStream) >> numStr;
        cout << "Case #" << i+1 << ": " << findTidy(numStr) << endl;
    }
    return;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "stupid you, argument size wrong" << endl;
        return 0;
    } else {
        string filename = argv[1];
        string line;
        ifstream myfile(filename);
        if(myfile.is_open()){
            flipFileReadHelper(&myfile);
        } else {
            cout << "file open failed" << endl;
        }
        return 0;
    }
}

