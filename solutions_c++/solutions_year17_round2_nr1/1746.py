#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    
    for (int ncase = 1; ncase <= T; ++ncase) {
        int D, N;
        cin >> D >> N;
        
        map<int, int> horses;
        for (int n = 0; n < N; ++n) {
            int tmp_pos; cin >> tmp_pos;
            int tmp_spd; cin >> tmp_spd;
            horses[tmp_pos] = tmp_spd;
        }
        
        int min_pos; double min_t = -1.0;
        for (map<int, int>::iterator it = horses.begin(); it != horses.end(); ++it) {
            int cur_pos; double cur_t;
            cur_pos = it->first;
            cur_t = (double) (D-cur_pos) / it->second; // gives time to reach end
            if (cur_t > min_t) {
                min_t = cur_t;
                min_pos = cur_pos;
            }
        }
        
        double speed = double (D) / min_t;
        
        cout << fixed;  
        cout.precision(6);
        cout << "Case #" << ncase << ": ";
        // output answer
        //cout << speed;
        printf("%.6f", speed);
        //
        cout << "\n";
    }
    
    return 0;
}
