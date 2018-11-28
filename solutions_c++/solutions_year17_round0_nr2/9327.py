#include <iostream>
#include <functional>
#include "vector"
//#include "map"
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include "list"
using namespace std;

#define MAX 105
const int INF = 1e9;

vector<string> v;
bool checkTidy(string s) {
    int length = s.size();
    for(int i=length-1; i>=1; i--) {
        if (s[i]< s[i-1]) {
            return false;
        }
    }
    return true;
}
string subint(string s) {
    int length = s.size();
    int i=length-1;
    bool borrow = false;
    if (checkTidy(s)) {
        return s;
    }
    while (i>=0) {
        if (borrow) {
            if (s[i] == '0') {
                s[i] = '9';
                borrow = true;
            } else {
                s[i] = s[i] - 1;
                borrow = false;
                if (checkTidy(s)) {
                    break;
                }
                s[i] = '9';
                borrow = true;

            }
        } else {
            s[i] = '9';
            borrow = true;

        }
        i--;

    }
    return s;
}

int main() {
//    freopen("/Users/macos/Documents/projects/my/big-o/input.in", "rt", stdin);
    int n;
    string temp;
    cin>> n;
    for (int i=0; i<n; i++) {
        cin>> temp;
        v.push_back(temp);

    }
    for (int i=0; i<n; i++) {
        string s = v[i];
        s = subint(s);
        cout<<"Case #" << i+1 <<": " << atoll(s.c_str()) << endl;

    }


    return 0;


}