#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int ncase = 1; ncase <= T; ++ncase) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        
        pair<char, int> min, mid, max;
        
        int mini = R; char minc = 'R';
        if (Y < mini) {
            mini = Y;
            minc = 'Y';
        } if (B < mini) {
            mini = B;
            minc = 'B';
        }
        min.first = minc; min.second = mini;
        
        int maxi = R; char maxc = 'R';
        if (maxi <= Y) {
            maxi = Y;
            maxc = 'Y';
        } if (maxi <= B) {
            maxi = B;
            maxc = 'B';
        }
        max.first = maxc; max.second = maxi;
        
        int midc = (char) ('R' + 'Y' + 'B' - min.first - max.first);
        int midi = R+Y+B-min.second-max.second;
        mid.first = midc;
        mid.second = midi;
        
        
        cout << "Case #" << ncase << ": ";
        // output answer
        
        if (max.second > min.second + mid.second)
            if (max.second == 1)
                cout << max.first;
            else
                cout << "IMPOSSIBLE";
        else {
            
            while (max.second > 0) {
                if (min.second == 0) {
                    while (max.second > 0) {
                        cout << max.first << mid.first;
                        --max.second; --mid.second;
                    }
                } else if (max.second > mid.second) {
                    while (min.second > 0 && max.second > mid.second) {
                        cout << max.first << min.first;
                        --max.second; --min.second;
                    }
                } else {
                    while (min.second > 0) {
                        cout << max.first << mid.first << min.first;
                        --max.second; --mid.second; --min.second;
                    }
                }
            }
            
        }
        
        
        //
        cout << "\n";
    }
    
    return 0;
}
