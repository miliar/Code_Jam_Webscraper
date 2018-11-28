#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

bool overlap(int a1, int a2, int b1, int b2) {
  if(a1 > a2 || b1 > b2) return false;
  cout << a1 << ' ' << a2 << ' ' << b1 << ' ' << b2 << endl;
  cout << ((b1 < a1 && b2 < a1) || (b2 > a2 && b1 > a2)) << endl;;
    return !((b1 < a1 && b2 < a1) || (b2 > a2 && b1 > a2));
}

int main() {
    ofstream fout;
    ifstream fin;
    fin.open("input.txt");
    fout.open("output.txt");
    int t; fin >> t;
    for(int tc = 1; tc <= t; tc++) {
        int n, p; fin >> n >> p;
        int r[n];
        for(int i = 0; i < n; i++) {
          fin >> r[i];
        }
        int q[n][p];
        for(int i = 0; i < n; i++) {
          for(int j = 0; j < p; j++) {
            fin >> q[i][j];
          }
        }
        for(int i = 0; i < n; i++) {
          sort(q[i], q[i] + p);
        }

        int cnt[n][p][2];//min, max
        for(int i = 0; i < n; i++) {
          for(int j = 0; j < p; j++) {
            double num = q[i][j];
            num /= r[i];
            cnt[i][j][0] = ceil(num/1.1);
            cnt[i][j][1] = floor(num/0.9);
          }
        }

        for(int i = 0; i < n; i++) {
          for(int j = 0; j < p; j++) {
            cout << cnt[i][j][0] << ' ' << cnt[i][j][1] << endl;
          }
        }

        int count = 0;
        int pointers[n];
        for(int i = 0; i < n; i++) pointers[i] = 0;
        while(true) {
            int maxi = 0; bool pass = true;
            for(int i = 0; i < n; i++) {
                pass = pass && overlap(cnt[0][pointers[0]][0], cnt[0][pointers[0]][1], cnt[i][pointers[i]][0], cnt[i][pointers[i]][1]);
                maxi = max(maxi, cnt[i][pointers[i]][0]);
            }
            if(pass) {
                count++;
                for(int i = 0; i < n; i++) {
                    pointers[i]++;
                }
            } else {
              for(int i = 0; i < n; i++) {
                  if(cnt[i][pointers[i]][1] < maxi) {
                      pointers[i]++;
                  }
              }
            }

            bool end = false;
            for(int i = 0; i < n; i++) {
                //cout << pointers[i] << ' ';
                if(pointers[i] >= p) {
                    end = true;
                    break;
                }
            }
            //cout << endl;
            if(end) {
                break;
            }
        }

        fout << "Case #" << tc << ": " << count << endl;

    }
    return 0;
}
