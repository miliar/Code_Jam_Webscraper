#include <iostream>
#include <stdio.h>

using namespace std;

string s;

void update() {
    for (int idx = s.length()-1; idx > 0; idx--) {
        if (s[idx] < '0') {
            s[idx] = '9';
            s[idx-1]--;
        }
    }
}
int main()
{
    //freopen("input.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;

    cin >> cases;

    for (int i = 1; i <= cases; i++) {

        cin >> s;
         //cout << s << " to ";

        for (int idx = s.length()-1; idx > 0; idx--) {

            // e.g. 91 => 89
            //      100 => 99
            if (s[idx-1] > s[idx]) {
                s[idx-1] --;
                for (int k = idx; k < s.length(); k++)
                    s[k] = '9';
                update();
            }

        }

        if (s[0] == '0' && s.length() > 1)
            cout << "Case #" << i << ": " << s.substr(1,s.length()-1) << endl;
        else
            cout << "Case #" << i << ": " << s << endl;


    }
}
