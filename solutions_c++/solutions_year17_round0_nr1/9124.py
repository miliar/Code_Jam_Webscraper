#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define MAX_LENGTH 1003

/**
 * Finish when
 * meet empty character
 * */


int flippable(char * c) {
    return *c != 0;
}

void flip(char *i) {
    if(*i == '-') {
        *i = '+';
    }
    else if(*i == '+'){
        *i = '-';
    }
}

int fliprec(char* cur, int flipper_len, int acc) {
    if ((*cur) == 0)
        return acc; // Success
    else if (*cur == '-') {
        for(int i =0; i < flipper_len; i ++) {
            if(flippable(cur+i)) {
                flip(cur + i);
            }
            else return -1;
        }
        return fliprec(cur + 1, flipper_len, acc + 1);
    } else {
        return fliprec(cur + 1, flipper_len, acc);
    }
}

int main() {
    int t;
    int flipper_len;
    int answer;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        char in[MAX_LENGTH] = "";
        cin >> in >> flipper_len;
        //algorithm here
        answer = fliprec(in, flipper_len, 0);
        if(answer >= 0)
            cout << "Case #" << i << ": " << answer << endl;
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
    return 0;
}

