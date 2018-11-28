#include <iostream>

using namespace std;

int main() {

    int T;
    cin >> T;

    for(int t = 1; t <= T; t++) {

        string s;
        int K;

        cin >> s >> K;

        int len = s.length();
        bool * happy = new bool[len];

        for(int i = 0; i < len; i++)
            if(s[i] == '+')
                happy[i] = 1;
            else
                happy[i] = 0;

        int flips = 0;
        for(int i = 0; i < len - K + 1; i++) {
            if(!happy[i]) {
                for(int j = 0; j < K; j++)
                    happy[j + i] = !happy[j + i];

                flips ++;
            }
        }

        bool flag = 0;
        for(int i = 0; i < len; i++)
            if(!happy[i])
                flag = 1;

        cout << "Case #" << t << ": ";
        if(flag)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << flips << endl;

    }

    return 0;
}