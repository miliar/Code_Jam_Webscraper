#include <cassert>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

bool isFlat(int flip, string& s, int index) {
    return (s[index] == '-') ^ (flip%2 == 1);
}

string testcase() {
    string s;
    int k;
    cin>>s>>k;
    int flip = 0, counter=0;
    vector<int> flips(1001, 0);
    int i;
    for (i = 0; i<s.size()-k+1; i++) {
        flip += flips[i];
        if (isFlat(flip, s, i)) {
            counter ++;
            flips[i+k]++;
            flip++;
        }
    }
    bool impossible = false;
    for (; i<s.size(); i++) {
        flip += flips[i];
        if (isFlat(flip, s, i)) {
            impossible = true;
        }
    }
    flip += flips[i];
    assert(flip%2 == 0);

    if (impossible) {
        return "IMPOSSIBLE";
    } else {
        return to_string(counter);
    }
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

