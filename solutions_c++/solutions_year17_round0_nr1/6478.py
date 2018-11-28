#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void flip(string &pancakes, int pos, int pansize) {
    for (int i=pos; i < pos+pansize && i < pancakes.size(); ++i) {
        if (pancakes[i] == '+') {
            pancakes[i] = '-';
        } else {
            pancakes[i] = '+';
        }
    }
}

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
        string pancakes;
        fin >> pancakes;
        int pansize = 2;
        fin >> pansize;
        int flips = 0;
        for (int i=0; i <= pancakes.size()-pansize; ++i) {
            if (pancakes[i] == '-') {
                //cerr << pancakes << endl;
                flip(pancakes, i, pansize);
                ++flips;
            }
        }
        //cerr << pancakes << endl;
        bool happy = true;
        for (size_t i=pancakes.size()-pansize; happy && i < pancakes.size(); ++i) {
            if (pancakes[i] == '-') {
                happy = false;
            }
        }
        if (happy) {
            fout << "Case #" << t+1 << ": " << flips << endl;
        } else {
            fout << "Case #" << t+1 << ": IMPOSSIBLE\n";
        }
    }
    fin.close();
    fout. close();
    return 0;
}
