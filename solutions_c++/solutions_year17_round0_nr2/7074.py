#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream Inputfile;
ofstream Outputfile;

#define cin Inputfile
#define cout Outputfile

#define FILENAME "B-large"
#define FILENAME_IN FILENAME ".in"
#define FILENAME_OUT FILENAME ".out"

#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
#define forba(i, a, b) for (int i = (int)(b); i >= (int)(a); --i)
#define for0n(i, n) forab (i, 0, n-1)
#define for1n(i, n) forab (i, 1, n)
#define forn0(i, n) forba (i, n-1, 0)
#define forn1(i, n) forba (i, n, 1)

int main() {
    Inputfile.open(FILENAME_IN);
    Outputfile.open(FILENAME_OUT);
    int T;
    cin >> T;

    string ipT = "11111111111111111111";
    bool flag = false;

    getline (cin, ipT);
    for1n (i, T) {
        getline (cin, ipT);
        cout << "Case #" << i << ": ";
        forab (j, 0, (ipT.length() - 2)) {
            if (ipT[j] > ipT[j+1]) {
                ipT[j]-=1;
                forab (k, (j+1), (ipT.length() - 1)) {
                    ipT[k]='9';
                }
                if (j > 0) {
                    j-=2;
                }
            }
        }
        flag = false;
        forab (l, 0, (ipT.length() - 1)) {
            if (flag || ipT[l] != '0') {
                flag = true;
                cout << ipT[l];
            }
        }
        cout << endl;
    }

    return 0;
}
