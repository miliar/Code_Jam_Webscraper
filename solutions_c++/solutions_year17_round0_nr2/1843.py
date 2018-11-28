// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 2005

ll n, m, t;

char flip(char c){
    return c == '+' ? '-' : '+';
}


int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        string s;
        cin >> s;
        ll l = 0, r = 0;
        while (r < s.size()){
            if (s[r] > s[l]) l = r;
            else if (s[r] < s[l]){
                break;
            }
            r++;
        }
        cout << "Case #" << cse << ": ";
        if (r == s.size()){
            cout << s << endl;
        }
        else if (l == 0 && s[0] == '1'){
            for (int i = 1; i < s.size(); i++) cout << '9';
            cout << endl;
        }
        else {
            for (int i = 0; i < l; i++){
                cout << s[i];
            }
            cout << char(s[l]-1);
            for (int i = l+1; i < s.size(); i++){
                cout << '9';
            }
            cout << endl;
        }
    }
    return 0;
}

