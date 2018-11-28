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
#include <time.h>
#define int long long
using namespace std;
int t, n, k;
double r, h;
double PI = 3.1415926535897932384626;
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    out.precision(30);
    for (int it=0;it<t;it++){
        in >> n >> k;
        vector<vector<double> > data;
        for (int i=0;i<n;i++){
            in >> r >> h;
            vector<double> help;
            help.push_back(r);
            help.push_back(h);
            data.push_back(help);
        }
        sort(data.begin(), data.end(), greater<vector< double> >());
        double answer = 0;
        for (int i=0;i<=n-k;i++){
            double na = PI * data[i][0] * data[i][0];
            na += 2 * PI * data[i][0] * data[i][1];
            vector<double> big;
            for (int j=i+1;j<n;j++){
                double pl = data[j][0] * data[j][1] * 2 * PI;
                big.push_back(pl);
            }
            sort(big.begin(), big.end(), greater<double>());
            for (int j=0;j<k-1;j++){
                na += big[j];
            }
            answer = max(answer, na);
        }
        out << "Case #" << it+1 << ": ";
        out << answer << endl;
    }
    return 0;
}
