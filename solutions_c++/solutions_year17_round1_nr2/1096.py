#include <bits/stdc++.h>

using namespace std;

int main () {
    int testCases;
    int N, P, answer;
    float temp;
    vector<vector<float>> Q;
    vector<pair<float,float>> R;
    vector<vector<pair<float,float>>> sizes;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        answer = 0;
        cin >> N >> P;

        R.clear();
        for (int i = 0; i < N; i++) {
            cin >> temp;
            R.push_back(pair<float,float>(temp - temp/10.0, temp + temp/10.0));
        }

        Q = vector<vector<float>>(N);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < P; j++) {
                cin >> temp;
                Q[i].push_back(temp);
            }
        }

        sizes = vector<vector<pair<float,float>>>(N);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < P; j++) {
                float lowest = floorf(Q[i][j] / R[i].first);
                float highest = ceilf(Q[i][j] / R[i].second);
                if (lowest >= highest) {
                    sizes[i].push_back(pair<float,float>(lowest,highest));
                }
            }
            sort(sizes[i].begin(), sizes[i].end());
        }

        /*for (auto stack : sizes) {
            for (auto package : stack) {
                cout << package.first << " " << package.second << " " << endl;
            }
            cout << endl;
        }*/

        if (sizes.size() == 1) {
            answer = sizes[0].size();
        }
        else {
            int size = P;
            int limiting = 0;
            vector<int> sequence;
            for (int i = 0; i < static_cast<int>(sizes.size()); i++) {
                if (static_cast<int>(sizes[i].size()) < size) {
                    size = sizes[i].size();
                    limiting = i;
                }
            }

            for (int i = 0; i < static_cast<int>(sizes[limiting].size()); i++) {
                //cout << "i:" << i << endl;
                for (int j = 0; j < static_cast<int>(sizes.size()); j++) {
                    //cout << "j:" << j << endl;
                    if (j != limiting) {
                        bool found = false;
                        for (int k = 0; k < static_cast<int>(sizes[j].size()); k++) {
                            //cout << "k:" << k << endl;
                            if (sizes[limiting][i].first >= sizes[j][k].second && sizes[limiting][i].second <= sizes[j][k].first) {
                                sequence.push_back(k);
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            sequence.clear();
                            break;
                        }
                    }
                    else {
                        sequence.push_back(i);
                    }
                }
                if (static_cast<int>(sequence.size()) == N) {
                    answer++;
                    for (int j = 0; j < static_cast<int>(sequence.size()); j++) {
                        if (j != limiting) {
                            sizes[j].erase(sizes[j].begin() + sequence[j]);
                        }
                    }
                    sequence.clear();
                }
            }
        }

        cout << "Case #" << curCase << ": " << answer << endl;
    }

    return 0;
}