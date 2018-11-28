#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

struct session {
    int start;
    int end;
    bool is_cam;    
};

void solve() {
    int Ac, Aj; cin >> Ac >> Aj;

    vector<session> S(Ac + Aj);

    for (int i = 0; i < Ac; i++) {
        cin >> S[i].start >> S[i].end;
        S[i].is_cam = true;
    }

    
    for (int i = 0; i < Aj; i++) {
        cin >> S[Ac+i].start >> S[Ac+i].end;
        S[Ac+i].is_cam = false;
    }

    auto time_comp = [](session s1, session s2)->bool {
        return s1.start < s2.start;
    };

    sort(S.begin(), S.end(), time_comp);

    int min_swaps = 0;
        
    vector<int> Ec;
    vector<int> Ej;

    int min_cam = 0;
    int max_cam = 0;

    for (int i = 0; i < S.size(); i++) {

        if (S[i].is_cam) {
            min_cam += S[i].end-S[i].start;
            max_cam += S[i].end-S[i].start;
        }
        int dur = (S[i].start - S[(i-1+S.size())%S.size()].end + 24*60) % (24*60);
        if (S[i].is_cam != S[(i-1+S.size())%S.size()].is_cam) {
            min_swaps++;
            max_cam += dur;
        }
        else {
            if (S[i].is_cam) {
                min_cam += dur;
                max_cam += dur;
            }

            if (dur != 0) {
                if (S[i].is_cam) {
                    Ej.push_back(dur);
                }   
                else {
                    Ec.push_back(dur);
                }
            }
        }
    }

    if (min_cam > 12 * 60) {
        sort(Ej.begin(), Ej.end(), greater<int>());
        for (int i = 0; i < Ej.size(); i++) {
            min_cam -= Ej[i];
            min_swaps += 2;
            if (min_cam <= 12 * 60) break;
        }
    }
    else if (max_cam < 12 * 60) {
        sort(Ec.begin(), Ec.end(), greater<int>());
        for (int i = 0; i < Ec.size(); i++) {
            max_cam += Ec[i];
            min_swaps += 2;
            if (max_cam >= 12*60) break;
        }
    }

    cout << min_swaps << endl;
}

int main (void) {
    
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
