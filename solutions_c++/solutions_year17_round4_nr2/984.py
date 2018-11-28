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
int t, n, c, m, pi, bi;
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int i=0;i<t;i++){
        in >> n >> c >> m;
        vector<vector<int> > tickets;
        for (int j=0;j<m;j++){
            in >> pi >> bi;
            vector<int> help;
            help.push_back(pi);
            help.push_back(bi);
            tickets.push_back(help);
        }
        sort(tickets.begin(), tickets.end());
        int answer;
        int left = 0;
        int right = m+1;
        while (right-left > 1){
            int mid = (left + right) / 2;
            int dp[c];
            for (int j=0;j<c;j++){
                dp[j] = 0;
            }
            bool cl = false;
            for (int j=0;j<m;j++){
                dp[tickets[j][1] - 1] ++;
                if (dp[tickets[j][1] - 1] > mid){
                    cl = true;
                    break;
                }
            }
            if (cl){
                left = mid;
                continue;
            }
            int np = 1;
            int now = 0;
            int can = 0;
            int aa = 0;
            int u = 0;
            while (u < m){
                if (tickets[u][0] > np){
                    now = 0;
                    can += mid;
                    np++;
                    continue;
                }
                now ++;
                if (now > mid){
                    can --;
                    now --;
                    aa ++;
                    if (can < 0){
                        cl = true;
                        break;
                    }
                }
                u ++;
            }
            if (cl){
                left = mid;
                continue;
            }
            right = mid;
            answer = aa;
        }
        out << "Case" << " #" << i + 1 << ": " << right << " " << answer << endl;
    }
    return 0;
}
