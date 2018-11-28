#include<iostream>
#include<string>
#include<bitset>
#include<queue>
#include<map>
#include<vector>
#include<set>
#include<deque>
#include<stack>

using namespace std;

typedef long long ll;
typedef pair<long long, long long> pll;

long long t, n, d;
double s, loc;
double solve() {
    vector<pair<double, double>> data;
    double maxTime = -1;
    for (int i = 0; i < n; ++i) {
        cin >> loc >> s;
        data.push_back(make_pair(loc, s));
        double t = (d - loc) / s;
        if (t > maxTime) maxTime = t;
    }

    sort(data.begin(), data.end());
    double minSpeed = 1;
    double maxSpeed = d / maxTime + 10;
    //cout << "max speed " << maxSpeed << endl;
    double prevSpeed = -1;
    double thisSpeed = -1;
    do {
        prevSpeed = thisSpeed;
        double mySpeed = minSpeed + (maxSpeed - minSpeed) / 2;
        thisSpeed = mySpeed;
        bool possible = true;
        //cout << "trying speed " << mySpeed << " with diff = " << (maxSpeed - minSpeed)<< endl;
        for (int i = 0; i < n; ++i) {
            if (mySpeed > data[i].second) {
                double timeToCatchUp = data[i].first / (mySpeed - data[i].second);
                double pointOfCatchUp = timeToCatchUp * mySpeed;
                //cout << "POC " << i << " at point " << pointOfCatchUp << endl;
                if (pointOfCatchUp < d) {
                    //cout << "not ok, catching up with horse " << i << " at point " << pointOfCatchUp << endl;
                    possible = false;
                    break;
                }
            }
        }
        //cout << possible << endl;
        if (possible) {
            minSpeed = mySpeed;
        }
        else {
            maxSpeed = mySpeed;
        }
    } while (abs(prevSpeed - thisSpeed) > 1e-7);

    return minSpeed;
}

int main() {
    cin >> t;
    for (ll i = 1; i <= t; ++i) {
        cin >> d >> n;
        cout << "Case #" << i << ": ";
        printf("%.7f\n", solve());
    }
    return 0;
}
