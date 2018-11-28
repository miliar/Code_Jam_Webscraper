#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        string c;
        cin >> c;
        int k, step = 0;
        cin >> k;
        auto it = c.begin();
        for(; it != c.end() - k + 1; it++)
            if(*it == '-') {
                *it = '+';
                for(int j = 1; j < k; j++)
                    if(*(it + j) == '-')
                        *(it + j) = '+';
                    else
                        *(it + j) = '-';
                step++;
            }
        bool possible = true;
        for(; it != c.end(); it++)
            if(*it == '-') {
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
                possible = false;
                break;
            }
        if(possible)
            cout << "Case #" << i << ": " << step << endl;
    }
    return 0;
}
