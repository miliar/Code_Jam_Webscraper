#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iomanip>
#include <map>
#include <cmath>
#include <deque>
using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int maxn = 200010;
const double eps = 1e-8;

int T;
string s;
int a[250];
int b[250];
int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d: ",tt);
        cin >> s;
        int len = s.length();
        for (int i = 0; i < len; i++) {
            a[i] = s[i]-'0';
        }
        for (int i = 0; i < len; i++) {
            b[i] = a[i];
            if (i > 0 && b[i] < b[i-1]) {
                for (int j = i; j < len; j++) {
                    b[j] = 9;
                }
                int j = i-1;
                while (j> 0 && --b[j] < b[j-1]) {
                    b[j] = 9;
                    j--;
                }
                if (j == 0) {
                    b[0]--;
                }
                break;
            }
        }
        if (b[0]) {
            printf("%d",b[0]);
        }
        for (int i = 1; i < len; i++) {
            printf("%d",b[i]);
        }
        printf("\n");
    }
    return 0;
}
