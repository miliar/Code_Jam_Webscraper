//============================================================================
// Name        : TidyNumbers.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

typedef unsigned long long ll;

ll pot10[20];

void calcPots(){
    ll p = 1;
    for (int i = 1; i < 19; i++){
        p*=10;
        pot10[i]=p;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    calcPots();
    int TC;
    cin >> TC;
    string s;
    int c = 1;
    while (TC-- && (cin >> s)){
        cout << "Case #" << c++ << ": ";
        if (s.length() == 1) {
            cout << s << "\n";
            continue;
        }
        int i = 1;
        while (i < (int)s.length() && s[i-1] <= s[i])i++;
        if (i == (int)s.length()){
            cout << s << "\n";
            continue;
        }
        while (i >= 2 && s[i-2] == s[i-1]) i--;
        ll n = stoull(s);
        int toSubtract = s.length() - i;
        n-=n%pot10[toSubtract];
        cout << (n-1) << "\n";
    }
}
