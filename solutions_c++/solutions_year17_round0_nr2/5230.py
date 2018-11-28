#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>


using namespace std;

char s[100];

string solve() {
    string res = "";
    const int n = strlen(s);
    bool anticarry = false;

    int i = 0;
    for (; i < n - 1; ++i) {
        if (s[i] > s[i+1])
            break;
    }

    if (i == n - 1)
        return string(s);

    for (int j = i + 1; j < n; ++j)
        res += '9';

    anticarry = true;
    for (; i > 0; --i) {
        if (anticarry) {
            --s[i];
            anticarry = false;
        }

        if (s[i] < s[i - 1]) {
            res += '9';
            anticarry = true;
        } else {
            res += s[i];
        }
    }


    if (anticarry && s[0] != '0')
        --s[0];

    if (s[0] != '0')
        res += s[0];

    reverse(res.begin(), res.end());

    return res;
}

int main(int argc, char const *argv[]) {
    FILE *fin = fopen("problemB.in", "r");
    FILE *fout = fopen("problemB.txt", "w");

    int t = 0;
    fscanf(fin, "%d", &t);

    long long int n = 0;
    for (int i = 0; i < t; ++i) {
        fscanf(fin, "%s", s);
        fprintf(fout, "Case #%d: %s\n", i + 1, solve().c_str());
    }

    return 0;
}