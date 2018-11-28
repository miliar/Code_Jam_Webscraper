#include <iostream>
#include <fstream>
#include <stack>
using namespace std;

#define PLUS 1
#define MINUS 0

int main() {
    ifstream fin;
    fin.open("input.txt");

    ofstream fout;
    fout.open("output.txt");


    int testCase=0;
    fin >> testCase;
    for(int t=0;t<testCase;t++) {
        string str;
        int k;

        fin >> str;
        //cout << "STR: " << str;
        fin >> k;
        stack<int> s;
        int count = 0;
        bool isFound = true;
        for(int i=0;i<str.length();i++) {
            if(str[i] == '+') {
                s.push(PLUS);
            }else {
                s.push(PLUS);
                if(i+k > str.length()) {
                    isFound = false;
                    fout << "Case #"<< t+1 << ": " << "IMPOSSIBLE" << endl;
                    break;
                }else {
                    count++;
                    for(int z=1;z<k;z++) {
                        str[i+z] = (str[i+z] == '+')?'-':'+';
                    }
                }
            }
        }
        if(isFound)
            fout << "Case #" << t+1 << ": " << count << endl;


    }



    fin.close();
    fout.close();
    return 0;
}