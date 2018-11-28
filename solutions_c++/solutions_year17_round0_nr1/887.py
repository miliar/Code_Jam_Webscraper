#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

string solveTestCase(string &pancake, unsigned N);

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        string pancake;
        unsigned size;
        
        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> pancake >> size;
            fout << "Case #" << count << ": ";
            fout << solveTestCase(pancake, size) << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}

string solveTestCase(string &pancake, unsigned K) {
    
    unsigned index = 0;
    unsigned end = pancake.size();
    unsigned moveCount = 0;
    for (string::iterator it = pancake.begin(), ie = pancake.end(); it != ie; ++it, ++index) {
        if (*it == '-') {
            //cout << index << " " << K << " " << end << endl; 
            if (index + K > end) return "IMPOSSIBLE";
            moveCount++;
            for (string::iterator sit = it, sie = it + K; sit != sie; ++sit) {
                if (*sit == '-') *sit = '+';
                else             *sit = '-';
            }
            //cout << pancake << endl;
        }
    }

    return to_string(moveCount);
}