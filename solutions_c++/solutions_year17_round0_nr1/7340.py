#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string realFlip(string S, int K) {
    if (string::npos == S.find('-')){
        return to_string(0);
    } else if (K>S.size()) {
        return "IMPOSSIBLE";
    } else if (K==1) {
        return to_string(count(S.begin(), S.end(), '-'));
    } else {
        int flips = 0;
        for (int i=0; i<S.length(); i++){
            if(S[i]=='-'){
                int newInd = 0;
                // one flip
                for(int j=0; j<K; j++){
                    newInd = j + i;
                    // cannot flip anymore with - left
                    if (newInd >= S.length()){
                        return "IMPOSSIBLE";
                    } else {
                        if(S[newInd]=='-') S[newInd]='+';
                        else S[newInd] = '-';
                    }
                }
                flips+=1;
            }
        }
        return to_string(flips);
    }
}

void flipFileReadHelper(ifstream* fileStream) {
    int inputNum = 0;
    (*fileStream) >> inputNum;
    for (int i = 0; i < inputNum ; i++) {
        string inputStr;
        (*fileStream) >> inputStr;
        int flipSize;
        (*fileStream) >> flipSize;
        cout << "Case #" << i+1 << ": " << realFlip(inputStr, flipSize) << endl;
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

