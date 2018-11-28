#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <tuple>
typedef long long ll;
using namespace std;
int t,n,k,a,b;
double pi = atan(1)*4;

void solve(int Case){
    vector<pair<double, double> > vals;
    cin >> n >> k;
    for(int i=0; i<n; i++){
        cin >> a >> b;
        vals.push_back(make_pair(pi*a*b*2, pi*a*a));
    }
    sort(vals.rbegin(), vals.rend());
    int ind = 0;
    double area = 0, totalarea = 0;
    double maxflat = 0;
    for(; ind<k-1; ind++){
        area += vals[ind].first;
        maxflat = max(maxflat, vals[ind].second);
    }
    for(; ind<n; ind++){
        totalarea = max(totalarea, area + vals[ind].first + max(maxflat, vals[ind].second) );
    }
    cout << "Case #" << Case << ": " << totalarea << "\n";
}



int main()
{
    ios::sync_with_stdio(false);
    cout.precision(17);
    cin >> t;
    for(int i=0; i<t; i++){
        solve(i+1);
    }
    return 0;
}
