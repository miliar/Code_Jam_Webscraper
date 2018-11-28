#include <iostream>
#include <vector>
#include "unordered_map"
#include "map"
#include <cmath>
#include <climits>
#include "queue"
#include "tuple"
#include <algorithm>
#include "sstream"

using ll=long long;
using ull=unsigned long long;
using namespace std;

template <typename T>
inline void printQueue(queue<T>&oq){queue<T>q(oq);int qCount=q.size();for(int i=0;i<qCount;++i){T qe=q.front();q.pop();
        cout<<qe;if(i!=qCount-1){cout << ", ";}q.push(qe);}cout << endl;}

template<typename T>
inline void PV(vector<T> v){int vc=v.size();for(int i=0;i<vc;++i){cout << v[i];if(i!=vc-1){cout<<", ";}}cout << endl;}

int main() {
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        ull R;
        cin >> R;
        ull C;
        cin >> C;
        vector<char> c(C);
        vector<vector<char>> m(R, c);
        for(int j = 0; j < R; ++j) {
            for(int l = 0; l < C; ++l) {
                cin >> m[j][l];
            }
        }
        for(int j = 0; j < R; ++j) {
            for(int l = 0; l < C; ++l) {
                if(m[j][l] == '?') {
                    continue;
                }
                char in = m[j][l];
                if(((l + 1 == C) || (l + 1 < C && m[j][l] != m[j][l + 1]))
                   && ((l == 0) || (l - 1 >= 0 && m[j][l] != m[j][l - 1]))) {
                    int k = j + 1;
                    while(k < R) {
                        if(m[k][l] != '?') {
                            break;
                        }
                        m[k][l] = in;
                        ++k;
                    }
                    k = j - 1;
                    while(k >= 0) {
                        if(m[k][l] != '?') {
                            break;
                        }
                        m[k][l] = in;
                        --k;
                    }
                }
            }
        }
        for(int j = 0; j < R; ++j) {
            for(int l = 0; l < C; ++l) {
                if(m[j][l] == '?') {
                    continue;
                }
                char in = m[j][l];
                int k = l + 1;
                while(k < C) {
                    if(m[j][k] != '?') {
                        break;
                    }
                    m[j][k] = in;
                    ++k;
                }
                k = l - 1;
                while(k >= 0) {
                    if(m[j][k] != '?') {
                        break;
                    }
                    m[j][k] = in;
                    --k;
                }
            }
        }
        cout << "Case #" << i << ": " << "" << endl;
        for(int j = 0; j < R; ++j) {
            for(int l = 0; l < C; ++l) {
                cout << m[j][l];
            }
            cout << endl;
        }
    }
}
