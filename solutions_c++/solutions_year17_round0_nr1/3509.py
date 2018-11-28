#include <iostream>
using namespace std;
int lol(string lolz, int k) {
    int counter = 0;
    for (int i = 0; i < lolz.length()-k+1; ++i) {
        if (lolz[i] == '-') {
            // cout << temp << endl;
            for (int i2 = 0; i2 < k; ++i2)
            {
                if (lolz[i2+i] == '+') {
                    lolz[i2+i] = '-';
                } else {
                    lolz[i2+i] = '+';
                }
            }

            counter++;
        }
    }
    bool good = true;
    for (int i = 0; i < lolz.length(); ++i)
    {
        if (lolz[i] == '-') {
            good=false;
            break;
        }
    }
    if (good) {
        return counter;
    } else {
        return 999999;
    }
}
int main(int argc, char const *argv[]) {

    int num;
    cin >> num;
    for (int numruns = 0; numruns < num; ++numruns) {
        string p;
        int k;
        cin >> p >> k;
        int l = lol(p,k);
        if (l == 999999) {
            cout << "Case #" << numruns+1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << numruns+1 << ": " << l << endl;
        }

    }
    return 0;
}