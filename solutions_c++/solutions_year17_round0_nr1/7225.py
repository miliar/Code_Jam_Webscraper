#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>

using namespace std;

vector<bool> pancakes;
vector<bool> flipped;

int initialize_pancakes(string S) {
    pancakes.clear();
    flipped.clear();
    int i = 0;
    while (S[i] != ' ') {
        pancakes.push_back((S[i] == '+'));
        flipped.push_back(false);
        i++;
    }
    string K_str = S.substr(i+1, 4);
    return strtol(K_str.c_str(), NULL, 10);       // K
}


bool complete() {
    for (auto it = pancakes.begin(); it != pancakes.end(); ++it)
        if (! *it)
            return false;
    return true;
}

/*
void print_pancakes() {
    for (auto it = pancakes.begin(); it != pancakes.end(); ++it)
        if (*it) cout << '+';
        else cout << '-';
    cout << endl;
}
*/

int flip(int pos, int a) {
    if (pos + a > pancakes.size())
        return -1;      // impossible
    for (int i = pos; i < pos + a; ++i)
        pancakes[i] = !pancakes[i];
    flipped[pos] = true;
    return 0;
}

int find_flip_pos() {
    int pos = 0;
    while (pos < pancakes.size() && pancakes[pos])
        pos++;
    return pos;
}

int main() {
    ifstream input("A-large.in");
    if (!input) {
        cerr << "Could not open file!" << endl;
        return 1;
    }
    ofstream output("A-large.out");
    int T;
    input >> T;
    string trash;
    getline(input, trash);      // ignores '\n'
    for (int x = 1; x <= T; x++) {
        string S;
        getline(input, S);
        output << "Case #" << x << ": ";
        int K = initialize_pancakes(S);
        int y = 0;
        bool impossible = false;
        while (!complete() && !impossible) {
            int position = find_flip_pos();
            if (flipped[position])
                impossible = true;
            if (flip(position, K) != 0)
                impossible = true;
            y++;
        }
        if (impossible)
            output << "IMPOSSIBLE" << endl;
        else
            output << y << endl;

    }
    input.close();
    output.close();

    return 0;
}
