#include <bits/stdc++.h>
using namespace std;

bool isTidy(int N) {

    string str;
    stringstream stream;

    stream << N;
    str = stream.str();

    for (int i = 1; i < str.size(); i++) {
        if (str[i] < str[i - 1])
            return false;
    }

    return true;
}

int main() {

    int TC, N, sol;

    scanf("%d", &TC);
    for (int t = 1; t <= TC; t++) {
        scanf("%d", &N);
        sol = 1;
        for (int i = 2; i <= N; i++) {
            if (isTidy(i))
                sol = i;
        }
        printf("Case #%d: %d\n", t, sol);
    }
    return 0;
}