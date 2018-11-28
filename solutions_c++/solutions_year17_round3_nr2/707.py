#include <bits/stdc++.h>

#define M_PI 3.14159265358979323846

using namespace std;

int main(){
    ifstream input("b.in");
    ofstream output;
    output.open ("b.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        cout << "Progress " << i << " / " << (T - 1) << endl;
        int C, J;
        input >> C >> J;
        int time[1440];
        for(int j = 0; j < 1440; j++) time[j] = 0;
        int Ct = 720;
        int Jt = 720;
        for(int j = 0; j < C; j++) {
            int Ci, Di;
            input >> Ci >> Di;
            for(int k = Ci; k < Di; k++) {
                time[k] = -1;
                Ct--;
            }
        }
        for(int j = 0; j < J; j++) {
            int Ji, Ki;
            input >> Ji >> Ki;
            for(int k = Ji; k < Ki; k++) {
                time[k] = 1;
                Jt--;
            }
        }
        list<pair<int, int> > s_gaps;
        int s_gaps_C = 0;
        int s_gaps_J = 0;
        list<pair<int, int> > d_gaps;
        for(int j = 0; j < 1440; j++) {
            if(j == 0 && ((time[j] == 1 && time[1439] == -1) || (time[j] == -1 && time[1439] == 1))) d_gaps.push_back(make_pair(j, 0));
            if(j != 0 && ((time[j] == 1 && time[j - 1] == -1) || (time[j] == -1 && time[j - 1] == 1))) d_gaps.push_back(make_pair(j, 0));
        }
        int tops = 1440;
        for(int j = 0; j < tops; j++) {
            if(time[j] == 0) {
                int start;
                int len;
                bool same;
                int gapF = j;
                int gapL = j;
                for(int k = j - 1; k != j; k = k == 0 ? 1439 : k - 1) {
                    if(k == -1) k = 1439;
                    if(time[k] != 0) {
                        if(k == 1439) {
                            gapF = 0;
                        } else gapF = k + 1;
                        start = time[k];
                        break;
                    }
                }
                for(int k = j + 1; k != j; k = k == 1439 ? 0 : k + 1) {
                    if(k == 1440) k = 0;
                    if(time[k] != 0) {
                        if(k == 0) {
                            gapL = 1439;
                        } else gapL = k - 1;
                        same = start == time[k];
                        break;
                    }
                }
                if(gapL >= gapF) {
                    len = gapL - gapF + 1;
                } else {
                    len = gapL + 1 + 1440 - gapF;
                    tops = gapF;
                }
                j = gapL + 1;
                if(same) {
                    s_gaps.push_back(make_pair(gapF, len));
                    if(start == -1) {
                        s_gaps_C++;
                    } else s_gaps_J++;
                } else {
                    d_gaps.push_back(make_pair(gapF, len));
                }
            }
        }
        int result = d_gaps.size();
        while(s_gaps.size()) {
            list<pair<int, int> >::iterator min_gap = s_gaps.begin();
            for(list<pair<int, int> >::iterator it = s_gaps.begin(); it != s_gaps.end(); ++it) {
                if(it->second < min_gap->second) min_gap = it;
            }
            int idx = min_gap->first - 1;
            if(idx == -1) idx = 1439;
            if(time[idx] == -1) {
                if(Ct >= min_gap->second) {
                    Ct -= min_gap->second;
                    s_gaps_C--;
                    s_gaps.erase(min_gap);
                } else {
                    result += s_gaps_C * 2;
                    s_gaps.clear();
                }
            } else {
                if(Jt >= min_gap->second) {
                    Jt -= min_gap->second;
                    s_gaps_J--;
                    s_gaps.erase(min_gap);
                } else {
                    result += s_gaps_J * 2;
                    s_gaps.clear();
                }
            }
        }
        output << "Case #" << (i + 1) << ": " << result << endl;
    }
    output.close();
    return 0;
}
