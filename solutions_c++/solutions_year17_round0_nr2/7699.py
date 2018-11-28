#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <list>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int test_case = 0; test_case < T; test_case++) {
        cout<<"Case #"<<test_case+1<<": ";
        string s;
        cin>>s;
        // Iterate right -> left, as soon as we see a decreasing sequence, fix the string by
        // lowering the left # and making the rest 9's
        for(int i = s.size()-1; i > 0; i--) {
            if(s[i] < s[i-1]) {
                // Found a decreasing sequence
                s[i-1]--;
                for(int j = i; j < s.size(); j++) {
                    s[j] = '9';
                }
            }
        }
        if(s[0] == '0') {
            // Edge case: Don't print a leading zero
            for(int i = 1; i < s.size(); i++) {
                cout<<s[i];
            }
            cout<<"\n";
        } else {
            cout<<s<<"\n";
        }
    }
    return 0;
}