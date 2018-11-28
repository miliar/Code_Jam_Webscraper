#include <iostream>
#include <vector>
#include <algorithm>
#include "utils.h"

using namespace std;




int main() {

    int nqueries;
    cin >> nqueries;
    int i = 1;
    while(nqueries) {
        string pancakes;
        int range;
        cin >> pancakes >> range;
        string result = "";
        int ans = 0;
        vector<bool> pancakesBool = transformPancakes(pancakes);
        for (int j = 0; j < pancakesBool.size(); ++j)
        {
            if (!pancakesBool[j]) {
                if (j + range <= pancakesBool.size()) {
                    flipPancakes(pancakesBool, range, j);
                    ans ++;
                } else if (count(pancakesBool.begin() + j, pancakesBool.end(), true) < distance(pancakesBool.begin() + j, pancakesBool.end())){
                    result = "IMPOSSIBLE";
                    break;
                }
            }
        }
        if (result == "")
            result = to_string(ans);
        cout << "Case #" << i << ": " << result << endl;
        nqueries --;
        i++;
    }
    return 0;
}