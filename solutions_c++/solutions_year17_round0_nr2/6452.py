#include<iostream>
#include<fstream>
using namespace std;

void check(string &s, int i , int n) {
        for (int j = i; j< n -1 ; j++) {
            if (s[j + 1] < s[j])
                s[j + 1] = s[j];
        }
}

void tidynumber(string &s) {
    int len = s.length();
    for(int i = len - 2; i >= 0 ; i--) {
        if (s[i] <= s[i + 1]) continue;
        s[i + 1] = '9';
        s[i] = s[i] - 1;
        check(s, i, len);
    }

    string tmp_sm; int j = 0;
    for (j =0; j< len; j++)
        if (s[j] !='0') break;
    s = s.substr (j,len);
}

int main() {

    int input;
    string s;

    ifstream file("input.txt");
    file >> input;
    for (int i =0; i< input ; i++) {
        file >> s;
        tidynumber(s);
        cout << "Case #" << i + 1 << ": "<< s <<endl;
    }
}
