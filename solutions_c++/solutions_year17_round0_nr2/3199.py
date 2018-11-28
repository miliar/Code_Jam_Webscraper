#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        string t, u = "";
        cin >> t;
        int a = t.length();
        bool b = false;
        int last = 0;
        int same = 0;
        int sameval = 0;
        for(int j = 0; j < a; j++) {
            if(b == true) {
                sameval = -1;
                u = u + '9';
                //cout << "reached b = true " << u << endl;
                continue;
            }
            if(t[j] - '0' > last) {
                for(int k = 0; k < same; k++) u = u + char(sameval + int('0'));
                same = 1;
                sameval = t[j] - '0';
                //cout << "reached if 1 " << t[j] - '0' << last << " " << sameval << " " << u << endl;
                last = sameval;
            }
            else if(t[j] - '0' == last) same++;
            else {
                if(sameval > 1) u = u + char(sameval - 1 + int('0'));
                for(int k = 0; k < same; k++) u = u + '9';
                b = true;
                //cout << "reached else " << t[j] - '0' << last  << u << endl;
                sameval = -1;
            }
        }
        if(sameval == 0) u = u + '9';
        if(sameval > 0) {
            for(int k = 0; k < same; k++) u = u + char(sameval + int('0'));
        }
        cout << "Case #" << i + 1<< ": " << u << "\n";
    }
    return 0;
}