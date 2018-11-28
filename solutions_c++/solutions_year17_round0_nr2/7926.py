#include <iostream>
#include <string>
#include <vector>

#define ll long long

using namespace std;

ll t, n, test, out;
string s;
vector<string> opt;

bool check(string& x){
    char last = '0';
    for(int i = 0;i<x.size();i++) {
        if(x[i] < last) return false;
        last = x[i];
    }
    return true;
}

int main() {
    cin >> t;
    while(t--){
        opt.clear();
        test++;
        out = 0;
        cin >> s;
        if(s.size() == 1){
            cout << "Case #" << test << ": ";
            cout << s[0];
            cout << endl;
            continue;
        }
        opt.push_back(s);
        string emp = "";
        for(int i = 0;i<s.size()-1;i++){
            emp += "9";
        }
        opt.push_back(emp);
        for(int i = 0;i<s.size();i++){
            string tmp = s;
            tmp[i]--;
            for(int j = i+1;j<s.size();j++) {
                tmp[j] = '9';
            }
            opt.push_back(tmp);
        }
        for(int i = 0;i<opt.size();i++){
            if(check(opt[i])){
//                cout << "ddd " << opt[i] << endl;
                out = max(out, stoll(opt[i]));
            }
        }
        cout << "Case #" << test << ": ";
        cout << out;
        cout << endl;
    }
    return 0;
}