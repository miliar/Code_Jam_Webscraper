#include <iostream>
using namespace std;

bool check_order(string &N)
{
    if (N.length() == 1) {
        return true;
    }
    for (int i = 0; i < N.length()-1; i++) {
        if (N[i] > N[i+1]) {
            return false;
        }
    }
    return true;
}

string remove_left_zeros(string &N) 
{
    int i = 0;
    for (i = 0; i < N.length(); i++) {
        if (N[i] != '0')
            break;
    }
    if (i == N.length()) {
        return "0";    
    }
    return N.substr(i); 
}

string decre(string num, int pos)
{
    for (int i = pos; i >= 0; i--) {
        if (num[pos] > '0') {
            num[pos]--;
            break;
        }
        else {
            num[pos] = '9';
        }
    }
    for (int i = pos+1; i < num.length(); i++) {
        num[i] = '9';
    }
    string nnum = remove_left_zeros(num);
    return nnum;
}

int main()
{
    int T;
    cin >> T;
    int counter = 0;
    while (T--) {
        string N;
        cin >> N;
        string last_num = N;
        while (!check_order(last_num)) {
            int l = last_num.length();
            for (int i = l-1; i > 0; i--) {
                if (last_num[i-1] > last_num[i]) {
                    last_num = decre(last_num, i-1);
                    break;
                }
            }
        }
        cout << "Case #" << ++counter << ": " << last_num << "\n";
    }
    return 0;
}