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
ll t,d,n,k,a,b;

void solve(int ind){
    cin >> d >> n;
    double time=0.0;
    for(int i=0; i<n; i++){
        cin >> a >> b;
        double t1 = (double)abs(d-a)/(double)b;
        time = max(time,t1);
    }
    cout << "Case #" << ind << ": " << (double)d/time << "\n";
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
