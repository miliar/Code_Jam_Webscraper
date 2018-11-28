#include <iostream>
#include <vector>
#include <string>

using namespace std;

int nextMinus(string list) {
    int nextMinus = (int) list.size();
    for (int i = 0; i < list.size(); i++) {
        if (list[i] == '-') {
            nextMinus = i;
            break;
        }
    }
    return nextMinus;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/danielsong/Downloads/A-large.in", "r", stdin);
    freopen("/Users/danielsong/Downloads/A-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string pancakes;
        cin >> pancakes;
        int size;
        cin >> size;
        int flips = 0;
        while (pancakes.size() - nextMinus(pancakes) >= size) {
            int next = nextMinus(pancakes);
            for (int i = next; i < next + size; i++) {
                pancakes[i] = pancakes[i] == '-' ? '+' : '-';
            }
            flips++;
        }
        if (pancakes.size() - nextMinus(pancakes) < size && nextMinus(pancakes) != pancakes.size()) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << t << ": " << flips << endl;
        }
    }
    
    return 0;
}
