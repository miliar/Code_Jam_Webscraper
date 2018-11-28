#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";

        int NC, NJ; cin >> NC >> NJ;
        int N = NC + NJ;

        vector<pair<pair<int,int>, bool>> act(N);

        for(int i = 0; i < N; i++) {
            cin >> act[i].first.first >> act[i].first.second;
            act[i].second = (i < NC);
        }
        sort(act.begin(), act.end());

        int least = 0, most = 0;
        int rswitch = 0;

        vector<int> PC, PJ;
        for(int i = 0; i < N; i++) {
            if(act[i].second) {
                least += act[i].first.second - act[i].first.first;
                most += act[i].first.second - act[i].first.first;
            }

            int j = (i + 1) % N;
            int beginp = act[i].first.second;
            int endp = act[j].first.first;
            int lenp = endp - beginp;
            if(lenp < 0)
                lenp += 24*60;
            if(act[i].second == act[j].second) {
                if(act[i].second) {
                    least += lenp;
                    most += lenp;
                    PC.push_back(lenp);
                }
                else {
                    PJ.push_back(lenp);
                }
            }
            else {
                rswitch++;
                most += lenp;
            }
        }
        sort(PC.begin(), PC.end());
        reverse(PC.begin(), PC.end());
        sort(PJ.begin(), PJ.end());
        reverse(PJ.begin(), PJ.end());

        //cout << "least: " << least << " most: " << most << " rswitch: " << rswitch << endl;

        if(least <= 24*30 && 24*30 <= most) {
            //cout << "no extra switches" << endl;
            cout << rswitch << endl;
        }
        else if(least > 24*30) {
            //cout << "least needs to be lower" << endl;
            int k = 0;
            while(least > 24*30) {
                rswitch += 2;
                least -= PC[k];
                k++;
            }
            cout << rswitch << endl;
        }
        else if(most < 24*30) {
            //cout << "most needs to be higher" << endl;
            int k = 0;
            while(most < 24*30) {
                rswitch += 2;
                most += PJ[k];
                k++;
            }
            cout << rswitch << endl;
        }
    }
    return 0;
}
