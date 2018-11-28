#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        cout << "Case #" << t1 << ": ";
        int ac, aj;
        cin >> ac >> aj;
        vector < pair <int, int> > vc (ac), vj (aj);
        for (int i = 0; i < ac; ++i)
            cin >> vc[i].first >> vc[i].second;
        for (int i = 0; i < aj; ++i)
            cin >> vj[i].first >> vj[i].second;

        sort (vc.begin(), vc.end());
        sort (vj.begin(), vj.end());
        if (ac < 2 && aj < 2) {
            cout << 2 << endl;
            continue;
        }

        if (ac < 2) {
            swap (ac, aj);
            swap (vc, vj);
        }

        long long luft = vc[1].first - vc[0].second;
        long long luft2 = 1440 - (vc[0].second - vc[0].first) - (vc[1].second - vc[1].first) - luft;
        if (luft >= 720 || luft2 >= 720)
            cout << 2 << endl;
        else
            cout << 4 << endl;
    }
}
