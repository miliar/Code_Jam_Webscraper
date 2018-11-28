#include <bits/stdc++.h>

using namespace std;

string s;

void decrease(int i){
    s[i]--;
    if(i > 0 && s[i] < s[i - 1]){
        decrease(i - 1);
        return;
    }
    for(int j = i + 1; j < s.size(); j++){
        s[j] = '9';
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long t;
    cin >> t;
    for(int z = 0; z < t; z++){
        cin >> s;
        cout << "Case #" << z + 1 << ": ";
        string c = "";
        for(int i = 0; i < s.size(); i++){
            c += '1';
        }
        if(s < c){
            for(int i = 1; i < s.size(); i++){
                cout << '9';
            }
            cout << endl;
            continue;
        }
        for(int i = 1; i < s.size(); i++){
            if(s[i] < s[i - 1]){
                decrease(i - 1);
                break;
            }
        }
        cout << s << endl;
    }
    return 0;
}
