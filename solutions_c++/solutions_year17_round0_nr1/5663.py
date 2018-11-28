#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main() {
    int n;
    cin >> n;
    cin.ignore();
    string input;
    int length;
    int flipper;
    bool cakes[1002];
    for (int ca = 1; ca <= n; ++ca) {
        getline(cin, input);
        length = input.find(' ');
        for (int i = 0; i < length; ++i)
            if (input[i] == '+') cakes[i] = true; else cakes[i] = false;
        flipper = 0;
        int i = length + 1;
        while (i < input.length()) {
            flipper *= 10;
            flipper += (input[i] - '0');
            i++;
        }
        int result = 0;
        for (int i = 0; i <= length - flipper; ++i)
            if (!cakes[i]) {
                result++;
                for (int j = i; j < i + flipper; ++j)
                    cakes[j] = !cakes[j];
            }
        for (int i = 0; i < length; ++i)
            if (!cakes[i]) {
                result = -1;
                break;
            }
        cout << "Case #" << ca << ": ";
        if (result != -1) cout << result << endl; else cout << "IMPOSSIBLE" << endl;
    }
}