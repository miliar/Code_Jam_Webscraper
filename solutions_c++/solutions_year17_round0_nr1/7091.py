#include <bits/stdc++.h>
//#include <unordered_map>
#define _USE_MATH_DEFINES//M_PI
using namespace std;
typedef long long ll;

int main()
{
    int n, counter = 1;
    cin >> n;
    while(n--) {
        int swaps = 0;
        string pancakes;
        int k;
        cin >> pancakes >> k;
        cout << "Case #" << counter++ << ": ";
        int i;
        for(i = 0; i <= pancakes.size() - k; i++) {
            if(pancakes[i] == '-') {
                swaps++;
                for(int j = i; j < i + k; j++) {
                    if(pancakes[j] == '-') pancakes[j] = '+';
                    else pancakes[j] = '-';
                }
            }
        }
        bool possible = true;
        while(i < pancakes.size() && possible) {
            if(pancakes[i] == '-') {
                cout << "IMPOSSIBLE" << endl;
                possible = false;
            }
            i++;
        }
        if(possible)
        cout << swaps << endl;
    }
    return 0;
}
