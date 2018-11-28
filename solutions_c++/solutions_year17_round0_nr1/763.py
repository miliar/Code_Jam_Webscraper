#include <iostream>
#include <string>

using namespace std;

int sol(string str, int K, int index) {
    if (str.length() - index < K) {
        for (int i=index; i<str.length(); ++i) {
            if (str[i] != '+')
                return -1;
        }
        return 0;
    }

    if (str[index] == '+')
        return sol(str, K, index + 1);
    else {
        for (int i=0; i<K; ++i) {
            str[i+index] = ((str[i+index] == '-') ? '+' : '-');
        }
        int res = sol(str, K, index+1);
        if (res == -1)
            return -1;
        else
            return 1 + res;
    }
}

int main() {
    int N;
    cin >> N;
    for (int i=0; i<N; ++i) {
        string str;
        int K;
        cin >> str >> K;

        int s = sol(str, K, 0);
        cout << "Case #" << i+1 << ": ";
        if (s == -1)
            cout << "IMPOSSIBLE";
        else 
            cout << s;
        cout << endl;
    }
    return 0;
}
