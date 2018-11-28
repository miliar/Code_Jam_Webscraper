#include <iostream>
#include <iomanip>  
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
using namespace std; 
 
int main(int argc, char *argv[]) { 
	
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        vector<pair<int, char>> unicorns;
        unicorns.push_back(make_pair(R, 'R'));
        unicorns.push_back(make_pair(O, 'O'));
        unicorns.push_back(make_pair(Y, 'Y'));
        unicorns.push_back(make_pair(G, 'G'));
        unicorns.push_back(make_pair(B, 'B'));
        unicorns.push_back(make_pair(V, 'V'));
        if((R + B < Y) || (R + Y < B) || (Y + B < R)) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        } else {
            string ans;
            char last = ' ';
            while(true) {
                pair<int, char> max = unicorns[0];
                if(max.first == 0) break;
                if(max.second != last) {
                    ans = ans + max.second;
                    last = max.second;        
                    unicorns[0] = make_pair(max.first-1, max.second);
                } else {
                    max = unicorns[1];
                    ans = ans + max.second;
                    last = max.second;
                    unicorns[1] = make_pair(max.first-1, max.second);
                }
                std::sort(unicorns.begin(), unicorns.end(), greater<pair<int, char>>()); 
            }
            cout << "Case #" << t << ": " << ans << endl;
        }
    }
    
    
	return 0; 
} 
