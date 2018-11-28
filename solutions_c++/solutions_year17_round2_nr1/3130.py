#include <iostream>
#include <vector>
#include "unordered_map"
#include "map"
#include <cmath>
#include <climits>
#include "queue"
#include "tuple"
#include <algorithm>
#include <iomanip>
#include "sstream"

using ll=long long;
using ull=unsigned long long;
using ld=long double;
using namespace std;

template <typename T>
inline void printQueue(queue<T>&oq){queue<T>q(oq);int qCount=q.size();for(int i=0;i<qCount;++i){T qe=q.front();q.pop();
        cout<<qe;if(i!=qCount-1){cout << ", ";}q.push(qe);}cout << endl;}

template<typename T>
inline void PV(vector<T> v){int vc=v.size();for(int i=0;i<vc;++i){cout << v[i];if(i!=vc-1){cout<<", ";}}cout << endl;}

inline double round( double val )
{
    if( val < 0 ) return ceil(val - 0.5);
    return floor(val + 0.5);
}

int main() {
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        double K;
        cin >> K;
        ull D;
        cin >> D;
        double m = INT_MIN;
        for(int j = 0; j < D; ++j) {
            double d;
            cin >> d;
            double s;
            cin >> s;
            double t = (K - d) / s;
            m = max(m, t);
        }
        double r = K / m;
        cout << "Case #" << i << ": " << fixed << setprecision(6) << r << endl;
    }
}
