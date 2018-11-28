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
int t, n, m;
char s;
int main(){
    ios_base::sync_with_stdio(false);
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int i=0;i<t;i++){
        in >> n >> m;
        char dp[n][m];
        set<int> yes;
        int mm = n;
        for (int j=0;j<n;j++){
            for (int k=0;k<m;k++){
                in >> s;
                dp[j][k] = s;
                if (s != '?') {yes.insert(j); mm = min(mm, j);}
            }
        }
        bool da = false;
        for (int j=0;j<n;j++){
            if (yes.count(j)){
                da = true;
                int now = 0;
                char ss;
                for (int k=0;k<m;k++){
                    if (dp[j][k] != '?'){
                        ss = dp[j][k];
                        for (int p=now;p<k;p++){
                            dp[j][p] = ss;
                        }
                        now = k + 1;
                    }
                }
                for (int k=now;k<m;k++){
                    dp[j][k] = ss;
                }
            }
            else{
                if (da){
                    for (int k=0;k<m;k++){
                        dp[j][k] = dp[j-1][k];
                    }
                }
            }
        }
        for (int j=mm-1;j>=0;j--){
            for (int k=0;k<m;k++){
                dp[j][k] = dp[j+1][k];
            }
        }
        out << "Case #" << i + 1 << ":" << endl;
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                out << dp[i][j];
            }
            out << endl;
        }
    }
    out.close();
    return 0;
}
