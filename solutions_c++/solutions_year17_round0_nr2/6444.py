#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("input.txt");
    if (!fin.is_open()) {
        cout << "Could not open file!\n";
        return 1;
    }
    ofstream fout;
    fout.open("output.txt");
    int T;
    fin >> T;
    for (int t=0; t<T; ++t) {
        string num;
        fin >> num;
        char max = num[0];
        bool tidy = true;
        for (int i=1; i < num.size(); ++i) {
            if (!tidy) {
                num[i] = '9';
                continue;
            }
            if (num[i] > max) {
                max = num[i];
            } else if (num[i] < max) {
                tidy = false;
                num[i] = '9';
                --num[i-1];
                for (int j = i-1; j>=1; --j) {
                    if (num[j] < num[j-1]) {
                        num[j] = '9';
                        --num[j-1];
                    }
                }
            }
        }
        if (num[0] == '0') {
            num.erase(0, 1);
        }
        fout << "Case #" << t+1 << ": " << num << endl;
    }
    fin.close();
    fout. close();
    return 0;
}
