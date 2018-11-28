#include<iostream>
#include<string>
#include<sstream>
#include<iterator>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    cin.ignore();
    for(int t = 1; t <= T; t++){
        string line;
        getline(cin, line);
        istringstream iss(line);
        vector<string> tokens;
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter(tokens));
        string s = tokens[0];
        int k = stoi(tokens[1]);
        int cnt = 0;
        for (int i = 0; i <= s.size()-k; i++) {
            if (s[i] == '-') {
                cnt++;
                for (int j = 0; j < k; j++) {
                    if (s[i+j] == '-') {
                        s[i+j] = '+';
                    }else{
                        s[i+j] = '-';
                    }
                }
            }
        }
        bool flag = false;
        cout << "Case #" << t << ": ";
        for (int i = s.size()-k+1; i < s.size(); i++) {
            if (s[i] == '-') {
                cout << "IMPOSSIBLE" << endl;
                flag = true;
                break;
            }
        }
        if (!flag) {
            cout << cnt << endl;
        }
    }
    return 0;
}