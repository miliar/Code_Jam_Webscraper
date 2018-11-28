//
// Created by adeladham on 4/8/17.
//

#include <bits/stdc++.h>

using namespace std;

#define oo (double)1e10
#define moo -((double)1e12)
#define zer (float)1e-6
#define ll long long
#define lli long long int

char flip(char c) {
    if (c == '+')return '-';
    else return '+';
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
#endif


    int t;
    cin >> t;
    for (int itr = 1; itr <= t; itr++) {

        string str;
        int k, cnt = 0;
        cin >> str >> k;

        for (int i = 0; i <= str.size() - k; i++) {

            if (str[i] == '-') {

                for (int j = i; j < i + k; j++)
                    str[j] = flip(str[j]);

                cnt++;
            }


        }


        if( count(str.begin(),str.end(),'-') )
            cout << "Case #" << itr << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << itr << ": " << cnt << endl;

//        cout<<"result"<<str<<endl;

    }

}