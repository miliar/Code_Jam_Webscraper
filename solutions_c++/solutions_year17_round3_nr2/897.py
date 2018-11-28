#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility> //pair
#include <map>
#include <cstring>
#include <cmath>

using namespace std;

int min2(int a, int b) {
    if (a<b) return a;
    else return b;
}

int max2(int a, int b) {
    if (a>b) return a;
    else return b;
}

int main()
{
    int t, ac, aj, c[100], d[100], j[100], k[100];
    cin >> t;
    for (int x=1;x<=t;x++) {
        cin >> ac >> aj;
        for (int i=0;i<ac;i++) cin >> c[i] >> d[i];
        for (int i=0;i<aj;i++) cin >> j[i] >> k[i];
        cout << "Case #" << x << ": ";
        if (ac+aj==1) cout << "2\n";
        else if (ac==1 && aj==1) cout << "2\n";
        else if (ac==2) {
            if (max2(d[0],d[1])-min2(c[0],c[1])<=720) cout << "2\n";
            else if (max2(c[0],c[1])-min2(d[0],d[1])>=720) cout << "2\n";
            else cout << "4\n";
        } else if (aj==2) {
            if (max2(k[0],k[1])-min2(j[0],j[1])<=720) cout << "2\n";
            else if (max2(j[0],j[1])-min2(k[0],k[1])>=720) cout << "2\n";
            else cout << "4\n";
        }
    }
    return 0;
}

// PROG_NAME < X-small-practice.in > output.txt
