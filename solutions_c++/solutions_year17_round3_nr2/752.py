
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;
#define JES 0
#define CAM 1
#define FREE -1

typedef pair<int,int> pii;


bool is_free(vector<int> &v, int a, int b) {
    for (int i = a; i <= b; i++) {
        if (v[i] != FREE) return false;
    }
    return true;
}

void assign_shift(vector<int> &v, int a, int b, int val) {
    for (int i = a; i < b; i++) {
        v[i] = val;
    }
}

void print_v(vector<pii> &v, string msg="") {
    cout << "print_vec: " << msg << endl;
    for (auto p: v) {
        cout << "    " << p.first << ' ' << p.second << endl;
    }
}

int main() {
    int T;
    int ac, aj;
    int cam_left, jes_left;
    vector<int> time_table;
    vector<pii> cam_shift;
    vector<pii> jes_shift;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> ac >> aj;
        time_table.assign(24*60, FREE);
        jes_shift.clear();
        cam_shift.clear();
        cam_left = jes_left = 720;
        for (int i = 0; i < ac; i++) {
            int a, b;
            cin >> a >> b;
            jes_left -= b-a;
            jes_shift.push_back({a,b});
            for (int j = a; j < b; j++)
                time_table[j] = JES;
        }
        for (int i = 0; i < aj; i++) {
            int a, b;
            cin >> a >> b;
            cam_left -= b- a;
            cam_shift.push_back({a, b});
            for (int j = a; j < b; j++)
                time_table[j] = CAM;
        }
        sort(jes_shift.begin(), jes_shift.end());
        sort(cam_shift.begin(), cam_shift.end());


        // print_v(cam_shift, "CAM");
        // print_v(jes_shift, "JES");


        while (cam_left > 0 && cam_shift.size() > 0) {
            int n = cam_shift.size();
            int idx = -1;
            int shortest = 720;
            for (int i = 0; i < n - 1; i++) {
                int a = cam_shift[i].second;
                int b = cam_shift[i+1].first - 1;
                if (is_free(time_table, a, b) && b+1-a < shortest) {
                    shortest = b+1 -a;
                    idx = i;
                }
            }
            if (is_free(time_table, 0, cam_shift[0].first - 1)
             && is_free(time_table, cam_shift[n-1].second, 60*24-1)) {
                int duration = 60*24 + cam_shift[0].first - cam_shift[n-1].second;
                if (duration < shortest) {
                    if (duration > cam_left) break;
                    cam_left -= duration;
                    assign_shift(time_table, 0, cam_shift[0].first, CAM);
                    assign_shift(time_table, cam_shift[n-1].second, 60*24, CAM);
                    cam_shift[0].first = 0;
                    cam_shift[n-1].second = 60*24-1;
                    continue;
                }
            }
            if (shortest > cam_left) break;
            int a = cam_shift[idx].second;
            int b = cam_shift[idx + 1].first;
            cam_left -= shortest;
            cam_shift[idx].second = cam_shift[idx + 1].second;
            cam_shift.erase(cam_shift.begin() + idx + 1);
            assign_shift(time_table, a, b, CAM);
        }

        // print_v(cam_shift, "CAM after");

        while (jes_left > 0 && jes_shift.size() > 0) {
            int n = jes_shift.size();
            int idx = -1;
            int shortest = 720;
            for (int i = 0; i < n - 1; i++) {
                int a = jes_shift[i].second;
                int b = jes_shift[i+1].first - 1;

                // cout << a << ' ' << b << " at i = " << i<< endl;
                // cout << "is free? " << is_free(time_table, a, b) << endl;
                // cout << time_table[2] << endl;

                if (is_free(time_table, a, b) && b+1-a < shortest) {
                    shortest = b+1 -a;
                    idx = i;
                }
            }
            if (is_free(time_table, 0, jes_shift[0].first - 1)
             && is_free(time_table, jes_shift[n-1].second, 60*24-1)) {
                int duration = 60*24 + jes_shift[0].first - jes_shift[n-1].second;
                if (duration < shortest) {
                    if (duration > jes_left) break;
                    jes_left -= duration;
                    assign_shift(time_table, 0, jes_shift[0].first, JES);
                    assign_shift(time_table, jes_shift[n-1].second, 60*24, JES);
                    jes_shift[0].first = 0;
                    jes_shift[n-1].second = 60*24-1;
                    continue;
                }
            }

            // cout << "JES HAS A PAIR of size " << shortest << endl;
            
            if (shortest > jes_left) break;
            int a = jes_shift[idx].second;
            int b = jes_shift[idx + 1].first;
            jes_left -= shortest;
            jes_shift[idx].second = jes_shift[idx + 1].second;
            jes_shift.erase(jes_shift.begin() + idx + 1);
            assign_shift(time_table, a, b, JES);
        }

        // print_v(jes_shift, "JES after");

        int cur = FREE;
        for (int i = 0; i < 60*24; i++) {
            if (time_table[i] == FREE && cur != FREE) {
                if (jes_left == 0)
                    time_table[i] = CAM;
                else if (cam_left == 0)
                    time_table[i] = JES;
                else {
                    time_table[i] = cur;
                    if (cur == JES)
                        jes_left--;
                    else
                        cam_left--;
                }
            } 
            else if (time_table[i] != FREE)
                cur = time_table[i];
        }
        int j = 0;
        while (time_table[j] == FREE) {
            if (jes_left == 0)
                time_table[j] = CAM;
            else if (cam_left == 0)
                time_table[j] = JES;
            else if (cur == JES) {
                jes_left--;
                time_table[j] = JES;
            } else if (cur == CAM) {
                cam_left--;
                time_table[j] = CAM;
            }
            j++;
        }

        int ans = 0;
        for (int i = 0; i < 60*24; i++)
            if (time_table[i] == FREE)
                cout << "ERR: " << i << endl;
            else if (time_table[i] != time_table[(i+1)%1440]) {
                ans++;
                // cout << i << endl;
            }
        // if (ans != 0)
        cout << "Case #" << cs << ": " << ans << endl;
        // else 
            // cout << "Case #" << cs << ": " << 2 << endl;
    }
}