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
double pl, ai;
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int it=0;it<t;it++){
        in >> n >> k;
        in >> pl;
        vector<double> data;
        for (int i=0;i<n;i++){
            in >> ai;
            data.push_back(ai);
        }
        sort(data.begin(), data.end());
        double nn = n;
        double one = 1;
        double nole = 0;
        for (double i=0;i<n-1;i++){
            double diff = (data[i+1] - data[i]) * (i + one);
            if (pl < diff){
                for (int j=0;j<=i;j++){
                    data[j] += pl / (i + one);
                }
                pl = nole;
            }
            else{
                pl -= diff;
                for (int j=0;j<=i;j++){
                    data[j] = data[i+1];
                }
            }
        }
        double diff = (one - data[n-1]) * nn;
        if (pl < diff){
            for (int j=0;j<n;j++){
                data[j] += pl / nn;
            }
            pl = 0;
        }
        else{
            for (int j=0;j<n;j++){
                data[j] = one;
            }
        }
        double ans = one;
        for (int i=0;i<n;i++){
            ans *= data[i];
        }
        out.precision(20);
        out << "Case #" << it + 1 << ": " << ans << endl;
    }
    return 0;
}
