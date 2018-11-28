#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using namespace std;

long long calculate(long long N) {
    string str = to_string(N);
    if (str.length() == 1) {
        return N;
    }
    
    bool zeroFlag = false;
    int i = 0;
    while (i < str.length() - 1) {
        if (str[i] > str[i + 1]) {
            while (i > 0 && str[i] == str[i - 1]) {
                i--;
            }
            
            str[i] = str[i] - 1;
            if (str[i] == '0') {
                zeroFlag = true;
            }
            break;
        }
        i++;
    }
    
    i++;
    if (!zeroFlag) {
        while (i < str.length()) {
            str[i] = '9';
            i++;
        }
    } else {
        if (i == 1 ||i == str.length() - 1) {
            string temp(str.length() - 1, '9');
            str = temp;
        }
    }
    
    
    
    return stol(str);
}

int main(int argc, const char * argv[]) {
    ifstream ifile;
    ifile.open("/Users/Zhen/Desktop/FB/FB/02_input.txt");
    int t;
    ifile >> t;
    
    ofstream ofile;
    ofile.open("/Users/Zhen/Desktop/FB/FB/02_output.txt");
    
    for (int i = 0; i < t; i++) {
        long long N;
        ifile >> N;

        long long result = calculate(N);

        ofile << "Case #" << (i + 1) << ": "<< result << endl;
    }
    
    ifile.close();
    ofile.close();
    
    return 0;
}
