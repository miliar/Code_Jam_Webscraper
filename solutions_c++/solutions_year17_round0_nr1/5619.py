#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int min_flips = 100000;

void flip(string& pancakes, int size, int loc) {
    for (int i = 0; i < size; ++i) {
        if (pancakes[i+loc] == '+')
            pancakes[i+loc] = '-';
        else
            pancakes[i+loc] = '+';
    }
}

void recursive_func(string pancakes, int size, int loc, int num_flips) {
    // cout << "Pancake line: " << pancakes << "\nloc: " << loc << endl;
    // At the end of the pancake line
    if (loc + size > pancakes.length()) {
        if (pancakes.find('-') == string::npos) {
            min_flips = min(min_flips, num_flips);
        }
        return;
    }
    // Recurse w/o flipping at current location
    recursive_func(pancakes, size, loc+1, num_flips);

    // Flip, then recurse
    flip(pancakes, size, loc);
    recursive_func(pancakes, size, loc+1, num_flips+1);
}

    
int main() {
    int iters;
    ifstream fin;
    fin.open("input.txt");
    fin >> iters;
    ofstream fout;
    fout.open("output.txt");
    for (int i = 0; i < iters; ++i) {
        min_flips = 100000;
        string pancakes;
        int size;
        fin >> pancakes >> size;
        recursive_func(pancakes, size, 0, 0);
        fout << "Case #" << i+1 << ": ";
        if (min_flips < 10000) {
            fout << min_flips << endl;
        } else {
            fout << "IMPOSSIBLE" << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
