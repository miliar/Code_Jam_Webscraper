#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// R + Y: O
// Y + B: G
// R + B: V
int R, O, Y, G, B, V;

void read() {
    int N;
    cin >> N >> R >> O >> Y >> G >> B >> V;
}


void work(int cases) {
    if (G > R || V > Y || O > B) {
        cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        return;
    }
    
    if (G > 0 && G == R) {
        if (V + Y + O + B > 0) {
            cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cases << ": ";
            for (int i = 0; i < G; ++i) {
                cout << "GR";
            }
            cout << endl;
        }
        return;
    }
    if (V > 0 && V == Y) {
        if (G + R + O + B > 0) {
            cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cases << ": ";
            for (int i = 0; i < V; ++i) {
                cout << "VY";
            }
            cout << endl;
        }
        return;
    } 
        
    if (O > 0 && O == B) {
        if (V + Y + G + R > 0) {
            cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cases << ": ";
            for (int i = 0; i < O; ++i) {
                cout << "OB";
            }
            cout << endl;
        }
        return;
    }
    
    vector< pair<int, int> > cnt2id;
    cnt2id.push_back(make_pair(R - G, 0));
    cnt2id.push_back(make_pair(Y - V, 1));
    cnt2id.push_back(make_pair(B - O, 2));
    sort(cnt2id.rbegin(), cnt2id.rend());

    if (cnt2id[0].first > cnt2id[1].first + cnt2id[2].first) {
        cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        return;
    }
    
    vector<int> ids(cnt2id[0].first, cnt2id[0].second);

    int idx = 0;
    for (int i = 0; i < cnt2id[1].first; ++i) {
        ids.insert(ids.begin() + idx, cnt2id[1].second);
        idx += 2;
    }
    
    for (int cnt = 0; cnt < cnt2id[2].first; ++cnt) {
        if (idx >= ids.size()) {
            idx = 0;
        }
        ids.insert(ids.begin() + idx, cnt2id[2].second);
        idx += 2;
    }

    // insert G
    for (int i = 0; i < ids.size(); ++i) {
        if (ids[i] == 0) {
            for (int j = 0; j < G; ++j) {
                ids.insert(ids.begin() + i, 3);
                ids.insert(ids.begin() + i, 0);
            }
            break;
        }
    }

    // insert V
    for (int i = 0; i < ids.size(); ++i) {
        if (ids[i] == 1) {
            for (int j = 0; j < V; ++j) {
                ids.insert(ids.begin() + i, 4);
                ids.insert(ids.begin() + i, 1);
            }
            break;
        }
    }
    
    // insert O
    for (int i = 0; i < ids.size(); ++i) {
        if (ids[i] == 2) {
            for (int j = 0; j < O; ++j) {
                ids.insert(ids.begin() + i, 5);
                ids.insert(ids.begin() + i, 2);
            }
            break;
        }
    }
    
    cout << "Case #" << cases << ": ";
    for (int i = 0; i < ids.size(); ++i) {
        cout << "RYBGVO"[ids[i]];
    }
    cout << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
