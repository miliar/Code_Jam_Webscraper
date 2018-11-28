#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <fstream>
#include <bitset>
#define int long long
using namespace std;
int t, n;
double finish, speed, now;
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    ios_base::sync_with_stdio(false);
    in >> t;
    out.precision(30);
    for (int i=0;i<t;i++){
        in >> finish >> n;
        double ans = pow(10, 18);
        for (int j=0;j<n;j++){
            in >> now >> speed;
            double t = (finish - now) / speed;
            ans = min(ans, finish / t);
        }
        out << "Case #" << i + 1 << ": ";
        out << ans << endl;
    }
    out.close();
    return 0;
}

