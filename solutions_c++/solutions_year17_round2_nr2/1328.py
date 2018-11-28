#include "bits.h"
using namespace std;

int max(int a, int b) {
    return a > b ? a : b;
}

int maxIndex(const vector<int> &all) {
    int max = 0, index = -1;
    for (int i = 0; i < all.size(); i++) {
        if (all[i] > max) {
            max = all[i];
            index = i;
        }
    }
    return index;
}

int maxExcept(vector<int> all, int index, int prefToAvoid) {
    all[index] = 0;
    int notAvoiding = maxIndex(all);
    all[prefToAvoid] --;
    int avoiding = maxIndex(all);
    if (all[avoiding] == all[notAvoiding]) {
        return avoiding;
    } else {
        return notAvoiding; 
    }
}

int maxExcept(vector<int> all, int index) {
    all[index] = 0;
    return maxIndex(all);
}

void solve() {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    vector<int> all = { R, O, Y, G, B, V };
    string chars = "ROYGBV";


    string s(N,' ');
    int index = maxIndex(all);
    int num = all[index];
    double density = num / double(N);

    // sanity check to make sure it is possible
    if (density > 0.5) { cout << "IMPOSSIBLE"; return; }

    num = 0;
    double epsilon = 0.000001;
    for (int i = 0; i < s.size(); i++) {
        if (i == 0 || num/double(i) < density + epsilon) {
            s[i] = chars[index];
            num++;
            all[index]--;
        }
    }
    
    //cerr << "8" << s << endl;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] != ' ') { continue; }
        if (i < s.size() - 1 && s[i+1] == ' ') {
            // length 2
            switch (index) {
                case 0:
                    s[i] = chars[2];
                    s[i+1] = chars[4];
                    all[2]--;
                    all[4]--;
                    break;
                case 2:
                    s[i] = chars[0];
                    s[i+1] = chars[4];
                    all[0]--;
                    all[4]--;
                    break;
                case 4:
                    s[i] = chars[2];
                    s[i+1] = chars[0];
                    all[2]--;
                    all[0]--;
                    break;
            }

        } else {
            // length 1
            // do it later !
        }
    }

    for (int i = 0; i < s.size(); i++) {
        if (s[i] != ' ') { continue; }
        int q = maxIndex(all);
        s[i] = chars[q];
        all[q]--;
    }




    cout << s;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
