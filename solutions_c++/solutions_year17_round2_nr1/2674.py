#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#include <utility>
#define MAX 987654321
using namespace std;
typedef long long ll;

int main() {
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    int T;
    //cin >> T;
    input >> T;
    
    for (int t = 1;t <= T;t++) {
        int d, n;
        //cin >> d >> n;
        input >> d >> n;
        vector<pair<int,int>> v(n);
        for(int i = 0;i < n;i++) {
            //cin >> v[i].first >> v[i].second;
            input >> v[i].first >> v[i].second;
        }
        
        double m = 0;
        for(int i = 0;i < n;i++) {
            m = max(m, (d - v[i].first) / (double)v[i].second);
        }
        
        output.precision(6);
        output << "Case #" << t << ": " << fixed << d/m << endl;
    }
}
