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
int t, n, q, ai, bi;
double ci, di;
double matrix[100][100];
double fl[101][101][101];
double CONST = 1000000000000;
vector<vector<int> > ask;
vector<vector<double> > horse;
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    ios_base::sync_with_stdio(false);
    in >> t;
    for (int p=0;p<t;p++){
        horse.clear();
        ask.clear();
        in >> n >> q;
        vector<double> answer;
        for (int i=0;i<n;i++){
            in >> ci >> di;
            vector<double> help;
            help.push_back(ci);
            help.push_back(di);
            horse.push_back(help);
        }
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                in >> ci;
                matrix[i][j] = ci;
            }
        }
        for (int i=0;i<q;i++){
            in >> ai >> bi;
            vector<int> help;
            help.push_back(ai);
            help.push_back(bi);
            ask.push_back(help);
        }
        for (int i=0;i<n+1;i++){
            for (int j=0;j<n+1;j++){
                for (int k=0;k<n+1;k++){
                    fl[i][j][k] = CONST;
                }
            }
        }
        for (int j=0;j<n;j++){
            for (int k=0;k<n;k++){
                if (matrix[j][k] != -1){
                    fl[0][j+1][k+1] = matrix[j][k];
                }
            }
        }
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++){
                for (int k=1;k<=n;k++){
                    fl[i][j][k] = min(fl[i-1][j][k], fl[i-1][j][i] + fl[i-1][i][k]);
                }
            }
        }
        for (int j=1;j<=n;j++){
            for (int k=1;k<=n;k++){
                double ls = fl[n][j][k];
                if (ls <= horse[j-1][0]){
                    fl[0][j][k] = ls / horse[j-1][1];
                }
                else{
                    fl[0][j][k] = CONST;
                }
            }
        }
        for (int j=1;j<=n;j++){
            for (int k=1;k<=n;k++){
                cout << fl[0][j][k] << " ";
            }
            cout << endl;
        }
        cout << endl;
        for (int i=1;i<n+1;i++){
            for (int j=0;j<n+1;j++){
                for (int k=0;k<n+1;k++){
                    fl[i][j][k] = CONST;
                }
            }
        }
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++){
                for (int k=1;k<=n;k++){
                    fl[i][j][k] = min(fl[i-1][j][k], fl[i-1][j][i] + fl[i-1][i][k]);
                }
            }
        }
        for (int i=0;i<q;i++){
            double ans = fl[n][ask[i][0]][ask[i][1]];
            answer.push_back(ans);
        }
        out.precision(20);
        out << "Case #" << p + 1 << ": ";
        for (int i=0;i<q;i++){
            out << answer[i] << " ";
        }
        out << endl;
    }
    out.close();
    return 0;
}

