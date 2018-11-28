#include <iostream>
#include <string>

using namespace std;

void FlipPancakes(string& pancakes, int k, int idx) {
    for (int i=idx; i < idx + k; ++i) {
        pancakes[i] = (pancakes[i] == '+' ? '-' : '+');
    }
}

bool DoRun()
{
    string pancakes;
    int k;
    cin >> pancakes >> k;
    if (cin.fail()) return false;  
    
    int flips = 0;
    for (int i=0; i < pancakes.size() - k + 1; ++i) {
        if (pancakes[i] == '-') {
            FlipPancakes(pancakes, k, i);
            ++flips;
        }
    }

    if (pancakes == string(pancakes.size(), '+')) cout << flips;
    else cout << "IMPOSSIBLE";
 
    return true;
}

int main()
{
    int runs;
    cin >> runs;
    for (int i=0; i < runs; ++i) {
        cout << "Case #" << i + 1 << ": ";
        if (!DoRun()) {
            cerr << "RUN FAILED\n";
            return 1;
        }
        cout << "\n";
    }
    cerr << "Success.\n";
    return 0;
}

