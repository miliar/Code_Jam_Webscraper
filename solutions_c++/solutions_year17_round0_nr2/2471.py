#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

long long solve(long long N) {
    vector<int> digits;
    while (N > 0) {
        int last = N % 10;
        digits.push_back(last);
        N /= 10;
    }
    reverse(digits.begin(), digits.end());

    for (int i = digits.size() - 2; i >= 0; i--) {
        if (digits[i] > digits[i + 1]) {
            digits[i]--;
            for (int j = i + 1; j < digits.size(); j++)
                digits[j] = 9;
        }
    }

    long long ret = 0;
    for (int i = 0; i < digits.size(); i++) {
        ret = 10*ret + digits[i];
    }
    return ret;
    //132
    //1000
    //1099
    //7
    //111111111111110999
    //99999999999999999
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for (int test = 0; test < T; test++)
    {
        long long N;
        fin >> N;
        long long ret = solve(N);

        fout << "Case #" << test + 1 << ": ";
        fout << ret << endl;
    }
    return 0;
}

