#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

fstream input("input.in");
ofstream output("output.out");
const string IMPOSSIBLE = "IMPOSSIBLE";

void solve(int index) {
    int steps = 0;
    int k;
    string sequence;
    input >> sequence >> k;
    
    for (int i = 0; i <= sequence.size() - k; i++) {
        if (sequence[i] == '-') {
            steps++;
            for (int j = i; j < i + k; j++) {
                if (sequence[j] == '-') {
                    sequence[j] = '+';
                } else {
                    sequence[j] = '-';
                }
            }
        }
    }
    
    bool valid = true;
    for (int i = 0; i < sequence.size(); i++) {
        if (sequence[i] == '-') {
            valid = false;
            break;
        }
    }
    output << "Case #" << index << ": ";
    if (!valid) {
        output << IMPOSSIBLE << "\n";
    } else {
        output << steps << "\n";
    }
}

int main()
{
    int T;
    input >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
