#include <iostream>
#include <iomanip>
#include <sstream>

using namespace std;

int N;
string colorName[6] = {"R", "OB", "Y", "GR", "B", "VY"};
int next(int num[6], int highPrio) {
    int index = 0;
    for(int i = 0; i < 6; ++i) {
        if (num[i] > num[index])
            index = i;
        if(num[i] == num[index] && i == highPrio)
            index = highPrio;
    }

    if(index == 0 && num[0] == num[3])
        return 3;
    if(index == 2 && num[2] == num[5])
        return 5;
    if(index == 4 && num[4] == num[1])
        return 1;
    return index;
}

// ROYGBV
// red orange yellow green blue violet
int main() {
    int T;
    cin >> T;
    cout << fixed << setprecision(6);
    for(int i = 1; i <= T; ++i) {
        cin >> N;
        int color[6];
        for(int j = 0; j < 6; ++j)
            cin >> color[j];
        cout << "Case #" << i << ": ";
        stringstream stall;
        color[0] -= color[3];
        color[2] -= color[5];
        color[4] -= color[1];
        N = N - color[3] - color[5] - color[1];

        int last = -1;
        int first = -1;
        for(int j = 0; j < N; ++j) {
            int colorCopy[6];
            for(int k = 0; k < 6; ++k)
                colorCopy[k] = color[k];

            if(last == 0 || last == 3) {
                colorCopy[0] = 0;
                colorCopy[1] = 0;
                colorCopy[5] = 0;
            } else if (last == 1 || last == 4) {
                colorCopy[3] = 0;
                colorCopy[4] = 0;
                colorCopy[5] = 0;
            } else if (last == 2 || last == 5){
                colorCopy[1] = 0;
                colorCopy[2] = 0;
                colorCopy[3] = 0;
            }
            last = next(colorCopy, first);
            --color[last];
            stall << colorName[last];
            if(first == -1)
                first = last;
        }

        bool possible = true;
        for(int j = 0; j < 6; ++j)
            possible = possible && (color[j] == 0);

        if((first == last && (first == 0 || first == 2 || first == 4)) || first - last == 3 || last - first == 3)
            possible = false;
        
        if(possible)
            cout << stall.str() << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}