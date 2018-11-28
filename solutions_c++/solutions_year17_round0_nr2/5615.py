#include <iostream>
#include <string>
using namespace std;

long long tidilize(long long n) {
    string str_n = std::to_string(n);
    for (int j = 0; j < str_n.length(); j++)
    {
        bool flag = 0;
        for (int i = 0; i < str_n.length() - 1; i++)
        {
            if (flag) {
                str_n[i] = '9';
            }
            if (str_n[i] > str_n[i + 1] && !flag) {
                flag = 1;
                str_n[i] = str_n[i] - 1;
            }
            if (flag) {
                str_n[i + 1] = '9';
            }
        }
        if (str_n[0] == '/')
        {
            str_n.erase(str_n.begin());
        }
    }
    return stoll(str_n);
}

void main() {
    int t;
    long long n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        //scanf("%d", &n);
        cin >> n;
        long long tidyn = tidilize(n);
        cout << "Case #" << (i + 1) << ": " << tidyn << endl;
    }
}