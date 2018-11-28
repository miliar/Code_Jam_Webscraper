#include<iostream>
#include <iomanip>
#include<fstream>
#include<queue>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

ifstream fin("3.in");
const int maxn = 1000;
const long long maxdis = 1232123212321232;
int n, q;
int e[maxn], s[maxn];
int a[maxn][maxn];
long long d[maxn][maxn];
double t[maxn][maxn], ans[maxn][maxn];
int qs[maxn], qt[maxn];

int main() {
    ofstream cout("3.out");
    int num_test;
    fin >> num_test;
    for (int iter_test = 0; iter_test < num_test; iter_test ++){
        fin >> n >> q;
        for (int i = 0; i < n; i++) {
            fin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                fin >> a[i][j];
            }
        }
        for (int i = 0; i < q; i++) {
            fin >> qs[i] >> qt[i];
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] == -1) 
                    d[i][j] = maxdis;
                else{
                    d[i][j] = a[i][j];
                }

            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++){
                    if (d[i][k] + d[k][j] < d[i][j]) {
                        d[i][j] = d[i][k] + d[k][j];
                    }
                }
            }
        }


        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++) {
                if (d[i][j] <= e[i]) {
                    t[i][j] = d[i][j] * ((double)1.0) / s[i];
                }
                else {
                    t[i][j] = -1;
                }
            }
        /*
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cout << t[i][j] << " ";
            cout << endl;
        }
        */
        
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++) {
                if (t[i][j] == -1) {
                    ans[i][j] = -1;//maxdis;
                }
                else {
                    ans[i][j] = t[i][j];
                }
            }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if ((ans[i][k] != -1) && (ans[k][j] != -1) && ((ans[i][j] == -1) || (ans[i][k] + ans[k][j] < ans[i][j])))
                        ans[i][j] = ans[i][k] + ans[k][j];

        cout << "Case #" << iter_test + 1 << ": ";
        for (int i = 0; i < q-1; i++) {
            cout << setprecision(12) << ans[qs[i]-1][qt[i]-1] << " ";
        }
        cout << setprecision(12) << ans[qs[q-1]-1][qt[q-1]-1] << endl;
    }
}
