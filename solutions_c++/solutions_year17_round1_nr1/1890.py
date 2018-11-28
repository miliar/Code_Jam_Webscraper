#ifdef F
#include <fstream>
std::ifstream cin("input.txt");
std::ofstream cout("output.txt");
#else
#include <iostream>
using std::cin;
using std::cout;
#endif
#include <sstream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int main() {
    int t;
    char g[25][25];
    cin >> t;
    for (int i=0; i<t; i++) {
        int r, c;
        cin >> r >> c;
        for (int j=0; j<r; j++) {
            for (int k=0; k<c; k++) {
                cin >> g[j][k];
            }
        }

        for (int k=0; k<c; k++) {
            if (g[0][k] =='?') {
                for (int j=0; j<r; j++) {
                    //cout << "\n1: "<<j << " " << k; 
                    if (g[j][k] != '?') {g[0][k] = g[j][k]; break;}
                }
            } 
        }
        for (int j=1; j<r; j++) {
            for (int k=0; k<c; k++) {
                if (g[j][k]=='?') g[j][k] = g[j-1][k];
            }
        }
        for (int j=0; j<r; j++) {
            if (g[j][0] == '?')
            for (int k=0; k<c; k++) {
                if (g[j][k] != '?') {g[j][0] = g[j][k]; break;}
            }
        }
        for (int j=0; j<r; j++) {
            for (int k=1; k<c; k++) {
                if (g[j][k]=='?') g[j][k] = g[j][k-1];
            }
        }

        cout << "Case #" << i+1 << ":" << "\n";
        for (int j=0; j<r; j++) {
            for (int k=0; k<c; k++) {
                cout << g[j][k];
            }
            cout <<"\n";
        }
    }
    return 0;
}
