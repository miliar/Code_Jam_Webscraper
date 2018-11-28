#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    string s;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> s;
        for (int i = 0; i < s.size() - 1; i++) {
            bool lessthan = true;
            int id = 0;
            while(true) {
                lessthan = false;
                for (int j = i + 1; j < s.size(); j++) {
                    if (s[j] < s[i]) {
                        lessthan = true;
                        id = j - 1;
                        break;
                    }
                }
                if (!lessthan) 
                    break;
                while(s[id] == '0' && id > 0) id--;
                s[id] -= 1;
                for (int i = id + 1; i < s.size(); i++) {
                    s[i] = '9';
                }
            }
        }
        cout << "Case #" << cs << ": ";
        int id = 0;
        while (s[id] == '0') id++;
        for (int i = id; i < s.size(); i++)
            cout << s[i];
        cout << endl;
    }
}