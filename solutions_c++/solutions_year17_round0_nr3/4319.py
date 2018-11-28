#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int l[4000001] = {0}, r[4000001] = {0};
int lastLeft, lastRight;

int solve (int pos, int s) {
    if (l[pos] == -1 && r[pos] == -1) {
        l[pos] = (s-1)/2;
        if (s % 2 == 1) {
            r[pos] = l[pos];
        } else {
            r[pos] = l[pos] + 1;
        }
        lastLeft = l[pos];
        lastRight = r[pos];
    } else {
        if (r[pos] > l[pos]) {
            solve (pos*2 + 1, r[pos]);
            r[pos] = max (l[pos*2+1], r[pos*2+1]);
        } else {
            solve (pos*2, l[pos]);
            l[pos] = max (l[pos*2], r[pos*2]);
        }
    }
    //cout << pos << ": " << s << "; " << l[pos] << ", " << r[pos] << endl;
    return 0;
}

int main() {
	// your code goes here
	int t, n, k;
	scanf ("%d", &t);
	for (int c = 1; c <= t; c++) {
	    scanf ("%d %d", &n, &k);
	    memset(l, -1, sizeof(int)*(4000001));
	    memset(r, -1, sizeof(int)*(4000001));
	    for (int x = 0; x < k; x++) {
	        solve (1, n);
	    }
	    cout << "Case #" << c << ": " << max(lastLeft, lastRight) << " " << min(lastLeft, lastRight) << "\n";
	}
	return 0;
}