#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
using namespace std;

int main() {
    int tcase;
    int dest, n;
    vector< pair<double,double> > v;
    double k,s;
    double maxSpeed;
    cin >> tcase;
    for (int t=0;t<tcase;t++) {
        v.clear();
        maxSpeed = -1;
        cin >> dest >> n;
        for (int i=0;i<n;i++) {
            cin >> k >> s;
            v.push_back(make_pair(k,s));
        }
        sort(v.begin(), v.end());
        for (int i=0;i<n;i++){
            if (v[i].first > dest) {
                break;
            }
            double speed = v[i].second;
            double t = ((double)dest-v[i].first)/speed;
            if (maxSpeed != -1) {
                maxSpeed = min(maxSpeed, (double)dest/t);
            } else {
                maxSpeed = (double)dest/t;
            }
        }
        cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << maxSpeed << endl;
    }
}