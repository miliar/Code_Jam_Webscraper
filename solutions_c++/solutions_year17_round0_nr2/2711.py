
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

uint64_t testcase() {
    uint64_t num, backup;
    cin>>num;
    backup = num;
    string output(""), input;
    input = to_string(num);
    output.push_back(input[0]);
    char digit = 0;
    int start9 = 20;
    for (int i =1; i<input.size(); i++) {
        if (input[i]>=input[i-1]) {
            output.push_back(input[i]);
        } else {
            start9 = i;
            digit = input[i-1]-1;
            break;
        }
    }

    if (digit == 0) {
        return backup;
    }
    output = "";
    for (int i = 0; i<input.size(); i++) {
        if (i >= start9) {
            output.push_back('9');
        } else {
            if (input[i] > digit) {
                output.push_back(digit);
                start9 = i+1;
            } else {
                output.push_back(input[i]);
            }
        }
    }
    return stoll(output);
}

int main() {
    //init();
    int t;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        auto result = testcase();
        cout<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}

