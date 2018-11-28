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
using namespace std;
long long t, n, m, ai;
vector<long long> wanted;
bool dp[50][50];
int main(){
    ios_base::sync_with_stdio(false);
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int i=0;i<t;i++){
        in >> n >> m;
        wanted.clear();
        vector<vector<long long> > data;
        for (int j=0;j<n;j++){
            in >> ai;
            wanted.push_back(ai);
        }
        for (int j=0;j<n;j++){
            vector<long long> help;
            for (int k=0;k<m;k++){
                in >> ai;
                help.push_back(ai);
                dp[j][k] = false;
            }
            sort(help.begin(), help.end());
            data.push_back(help);
        }
        long long answer = 0;
        long long p = 1;
        while (p<2000000){
            bool go = true;
            for (int j=0;j<n;j++){
                long long rrr = wanted[j] * p;
                long long rr = rrr * 11 / 10;
                long long ll = rrr * 9 / 10;
                if (rrr % 10 != 0) ll ++;
                bool yes = false;
                for (int k=0;k<m;k++){
                    if (data[j][k] >= ll && data[j][k] <= rr && !dp[j][k]){
                        yes = true;
                        break;
                    }
                }
                if (!yes) {go = false; break;}
            }
            if (go){
                answer ++;
                for (int j=0;j<n;j++){
                    long long rrr = wanted[j] * p;
                    long long rr = rrr * 11 / 10;
                    long long ll = rrr * 9 / 10;
                    if (rrr % 10 != 0) ll ++;
                    for (int k=0;k<m;k++){
                        if (data[j][k] >= ll && data[j][k] <= rr && !dp[j][k]){
                            dp[j][k] = true;
                            break;
                        }
                    }
                }
            }
            else{
                p ++;
            }
        }
        out << "Case #" << i + 1 << ": " << answer << endl;
    }
    out.close();
    return 0;
}
