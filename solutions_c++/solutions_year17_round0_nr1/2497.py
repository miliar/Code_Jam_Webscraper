#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for (int test = 0; test < T; test++)
    {
        int k;
        string p;
        fin >> p >> k;
        int rotations = 0;
        int ret = 0;
        for (int i = 0; i <= p.size()-k; i++) {
            if (p[i] == '-'){
                for (int j = i; j < i + k; j++) {
                    if (p[j] == '-') p[j] = '+';
                    else if (p[j] == '+') p[j] = '-';
                }
                ret++;
            }
        }
        bool imp = false;
        for (int i = 0; i < p.size(); i++) {
            if (p[i] == '-') imp = true;
        }
        fout << "Case #" << test + 1 << ": ";
        if (imp) {
            fout << "IMPOSSIBLE" << endl;
        }
        else {
            fout << ret << endl;
        }
    }
    return 0;
}

