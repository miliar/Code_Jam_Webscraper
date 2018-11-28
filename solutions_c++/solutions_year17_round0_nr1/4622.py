#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using namespace std;

int calculate(string str, int k) {
    int cnt = 0;
    bool hasNeg = false;
    int i = 0;
    while (i <= str.length() - k) {
        if (str[i] == '-') {
            hasNeg = true;
            cnt++;
            for (int j = 0; j < k; j++) {
                if (str[i + j] == '+') {
                    str[i + j] = '-';
                } else {
                    str[i + j] = '+';
                    
                }
            }
        }
        i++;
    }
    
    while (i < str.length()) {
        if (str[i] == '-') {
            hasNeg = true;
            cnt = -1;
            break;
        }
        i++;
    }
    
    if (hasNeg == false) {
        cnt = 0;
    }
    
    return cnt;
}

int main(int argc, const char * argv[]) {
    ifstream ifile;
    ifile.open("/Users/Zhen/Desktop/FB/FB/01_input.txt");
    int t;
    ifile >> t;
    
    ofstream ofile;
    ofile.open("/Users/Zhen/Desktop/FB/FB/01_output.txt");
    
    for (int i = 0; i < t; i++) {
        string str;
        ifile >> str;
        int k;
        ifile >> k;

        int result = calculate(str, k);
        cout << t << "\t" << result;
        if (result == -1) {
            ofile << "Case #" << (i + 1) << ": "<< "IMPOSSIBLE" << endl;
        }
        else {
            ofile << "Case #" << (i + 1) << ": "<< result << endl;
        }
    }
    
    ifile.close();
    ofile.close();
    
    return 0;
}
