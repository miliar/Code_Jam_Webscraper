#include <iostream>
#include <string>

using namespace std;

void swap(char *a) 
{
    if (*a == '+') {
        *a = '-';
    }
    else {
        *a = '+';
    }
}

bool final_check(string &S) 
{
    for (int i = 0; i < S.length(); i++) {
        if (S[i] == '-') 
            return false;
    }
    return true;
}

int main()
{
    int T, K;
    string S;
    cin >> T;
    int counter = 0;
    while (T--) {
        cin >> S >> K;
        int cur = 0;
        int time = 0;
        while (cur < S.length()) {
            if (S[cur] == '+') {
                cur++;
            }
            else if (S.length() - cur >= K) {
                int end = cur + K;
                for (int i = cur; i < end; i++) {
                    swap(&(S[i]));
                }
                int i = cur;
                for (;i < end; i++) {
                    if (S[i] == '-') {
                        cur = i;
                        break;
                    }
                }
                if (cur != i) {
                    cur += K;
                }
                time++;
            }
            else {
                break;
            }
        }
        bool success = final_check(S);
        if (success) {
            cout << "Case #" << ++counter << ": " << time << "\n";
        }
        else {
            cout << "Case #" << ++counter << ": " << "IMPOSSIBLE\n";
        }
    }
    return 0;
}