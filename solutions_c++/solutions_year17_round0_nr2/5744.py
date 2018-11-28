#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");

    int t;

    fin >> t;

    for (int i = 0; i < t; i++) {
        fout << "Case #" << i + 1 << ": ";
        string n;
        fin >> n;

        for (int j = n.length() - 1; j > 0; j--) {
            if (n[j] < n[j-1]) {
                n[j-1] = n[j-1] - 1;
                for (int k = j; k < n.length(); k++) {
                    n[k] = '9';
                }
            }
        }

        int j = 0;
        while (n[j] == '0') j++;

        for (; j < n.length(); j++) {
            fout << n[j];
        }

        fout << "\n";
    }

    return 0;
}
