#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for(int ca = 1; ca <= t; ++ca) {
        unsigned long long num;
        cin >> num;
        string tmp;
        REDO:
        while(num) {
            ostringstream oss;
            oss << num;
            const string &str_num = oss.str();
            for(int i = str_num.size() - 1; i > 0; --i) {
                if(str_num[i] == '9') {
                    tmp += '9';
                    num /= 10;
                    goto REDO;
                }
                if(str_num[i] < str_num[i - 1]) {
                    tmp += '9';
                    num = num / 10 - 1;
                    goto REDO;
                }
            }
            break;
        }
        reverse(tmp.begin(), tmp.end());
        stringstream ss;
        ss << num << tmp;
        long long ans;
        ss >> ans;
        cout << "Case #" << ca << ": " << ans << endl;
    }
    return 0;
}

