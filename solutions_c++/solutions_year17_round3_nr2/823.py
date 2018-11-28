#include <bits/stdc++.h>

using namespace std;

int T;

const int CAM = 100;
const int JAM = 200;
const int DEL = 300;

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int AC, AJ, A;
        cin >> AC >> AJ;
        A = AC + AJ;
        vector<pair<pair<int, int>, int> > activities;

        int nC = 0, nJ = 0;

        for (int i = 0; i < AC; ++i) {
            int C, D;
            cin >> C >> D;
            activities.push_back(make_pair(make_pair(C, D), CAM));
            nC += D-C;
        }
        for (int i = 0; i < AJ; ++i) {
            int J, K;
            cin >> J >> K;
            activities.push_back(make_pair(make_pair(J, K), JAM));
            nJ += K-J;
        }

        sort(activities.begin(), activities.end());

        auto ac0 = activities[0];
        ac0.first.first += 1440;
        ac0.first.second += 1440;

        activities.push_back(ac0);

        int switches = 0;
        vector<pair<int, int> > closures;

        for (int i = 0; i < A; ++i) {
            if (activities[i].second != activities[i+1].second) switches++;
            else {
                closures.push_back(make_pair(activities[i+1].first.first - activities[i].first.second, activities[i].second));
            }
        }

        sort(closures.begin(), closures.end());

        for (int i = 0; i < closures.size(); ++i) {
            int cost = closures[i].first;
            int type = closures[i].second;

            if (type == CAM) {
                if (nC + cost > 720) {
                    nJ++;
                    switches += 2;
                }
            }
            else if (type == JAM) {
                if (nJ + cost > 720) {
                    nC++;
                    switches += 2;
                }
            }
        }

        cout << "Case #" << t << ": " << switches << endl;
    }
}
