#include <fstream>
#include <math.h>
#include <algorithm>
#include <map>
using namespace std;
int main() {
    ifstream fi("codejam.in");
    ofstream fo("codejam.out");
    int q;
    fi >> q;
    for (int i = 1; i <= q; i++) {
        string s;
        fi >> s;
        int gold = -1;
        for (int j = 0; j < s.size()-1; j++)
            if (s[j] > s[j+1]) {
                gold = j;
                break;
            }
        int fin = gold;
        for (int j = gold; j >= 1; j--)
            if (s[j-1] >= s[j]) fin = j-1;
            else break;
        fo << "Case #" << i << ": ";
        for (int j = 0; j < fin; j++) fo << s[j];
        if (fin == -1) fo << s;
        else
            if (s[fin] > '1') fo << (char)(s[fin]-1);
        if (fin != -1)
            for (int j = fin+1; j < s.size(); j++) fo << 9;
        fo << '\n';
    }
    return 0;
}
