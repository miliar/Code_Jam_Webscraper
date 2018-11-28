#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <iomanip>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

int main() {
    int np; cin>>np;
    rep(i, np){
        int d; int n; cin>>d>>n;
        double big_time = 0.0;
        rep(i, n) {
            int start; int speed; cin >> start >> speed;
            double time = (d - start) / double(speed);
            big_time = std::max(time, big_time);
        }

        cout << "Case #"<<(i+1)<<": " << setprecision(10) << fixed << d/big_time << endl;
    }
}
