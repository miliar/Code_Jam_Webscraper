#include <iostream>
#include <fstream>
#ifdef WINDOWS
    #include <direct.h>
    #define GetCurrentDir _getcwd
#else
    #include <unistd.h>
#include <vector>

#define GetCurrentDir getcwd
#endif


using namespace std;

string pwd() {
    char buff[1024];
    GetCurrentDir(buff, 1024);
    string dir(buff);
    return dir;
}
string find_tidy(string number, int index);

int main(int argc, char* argv[]) {
    if (argc != 3 ) {
        cout << "usage: " << endl;
    }

    string inFileName = argv[1];
    string outFileName = argv[2];
    ifstream inFile(inFileName);
    ofstream outFile(outFileName);

    int count = 0;
    if ( !inFile.is_open()) {
        cout << "open" << endl;
        return -1;
    } else {
        string countStr;
        if (!inFile.eof()) getline(inFile, countStr);
        count = atoi(countStr.c_str());
    }
    vector<string> input_cases;
    while (count--) {
        string inputcase;
        getline(inFile, inputcase);
        input_cases.push_back(inputcase);
    }
    inFile.close();
    for (int i = 0; i < input_cases.size(); i++) {
        string number = input_cases[i];
        string newNum = find_tidy(number, i);
        if (newNum[0] == '0') {
            outFile << "Case #" << i + 1 << ": ";
            outFile << newNum.substr(1, newNum.size()) << endl;
        } else {
            outFile << "Case #" << i+1 << ": ";
            outFile << newNum << endl;
        }
    }
    outFile.close();
    return 0;
}
bool check (string number ) {
    if (number.size() == 1) return true;
    for (int i = 0; i < number.size() -1; i++) {
        if (number[i] <= number[i+1]) continue;
        else return false;
    }
}

string find_tidy(string number, int index) {
    if (check(number)) {
      return number;
    }
    int L =  number.size();
    string newSub =  find_tidy(number.substr(1, L), index);
//    cout << newSub << endl;
    if (number[0] > newSub[0]) {
//        cout << "comparision"<< L << endl;
        string temp(L-1,'9');
        char newHead = static_cast<char> (number[0] -1);
        return newHead + temp;
    } else {
        return number[0] + newSub;
    }
}