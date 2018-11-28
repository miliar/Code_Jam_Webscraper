#include <iostream>
#include <vector>
#include "unordered_map"
#include "map"
#include <cmath>
#include <climits>
#include "queue"
#include "tuple"
#include <algorithm>

using ll=long long;
using ull=unsigned long long;
using namespace std;

template <typename T>
inline void printQueue(queue<T> &oq)  {
    queue<T> q(oq);int qCount = q.size();
    for(int i=0;i<qCount;++i){T qe=q.front();q.pop();cout<<qe;if(i!=qCount-1) {cout << ", ";}q.push(qe);}
    cout << endl;
}

int main() {
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        ull sn;
        cin >> sn;
        ull pn;
        cin >> pn;
        queue<ull> mxQ;
        queue<ull> mnQ;
        mxQ.push(sn);
        ull mxfs;
        ull mnfs;
        for(ull j = 0; j < pn; ++j) {
            ull mfss;
            if(!mxQ.empty() && (mnQ.empty() || mxQ.front() >= mnQ.front())) {
                mfss = mxQ.front();
                mxQ.pop();
            }
            else {
                mfss = mnQ.front();
                mnQ.pop();
            }
            ull fss1 = mfss / 2;
            ull fss2 = fss1;
            if(mfss % 2 == 0) {
                --fss1;
            }
            mxfs = max(fss1, fss2);
            mnfs = min(fss1, fss2);
            if(mxfs > 0) {
                mxQ.push(mxfs);
            }
            if(mnfs > 0) {
                mnQ.push(mnfs);
            }
        }
        cout << "Case #" << i << ": " << mxfs << " " << mnfs << endl;
    }
}
