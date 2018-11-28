#include<iostream>
using namespace std;
int cmp(int a, int b, int c) {
    if (a == b &  b == c) return 0;
    if (a >= b && a >= c) return 1;
    if (b >= a && b >= c) return 2;
    if (c >= a && c >= b) return 3;
}
int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ++ca) {
        int n;
        int R, O, Y, G, B ,V;
        cin >> n;
        cin >> R >> O >> Y >> G >> B >> V;
        if (O == 0 && G == 0 && V == 0) {
            if ((R > (n / 2)) || (Y > (n / 2)) || (B > (n / 2)))
                cout << "Case #" << ca << ": IMPOSSIBLE" << endl;
            else {
                cout << "Case #" << ca << ": ";
                int a, b, c;
                a = R; b = Y; c = B;
                char aa = 'R', bb = 'Y', cc ='B';
                if (cmp(R,Y,B) != 0) {
                    if (cmp(R,Y,B) == 1) {
                        aa = 'R'; a = R;
                        if (Y >= B) {
                            bb = 'Y'; b = Y;
                            cc = 'B'; c = B;
                        } else {
                            bb = 'B'; b = B;
                            cc = 'Y'; c = Y;
                        }
                    } else if (cmp(R, Y, B) == 2) {
                        aa = 'Y'; a = Y;
                        if (R >= B) {
                            bb = 'R'; b = R;
                            cc = 'B'; c = B;
                        } else {
                            bb = 'B'; b = B;
                            cc = 'R'; c = R;
                        }
                    } else {
                        aa = 'B'; a = B;
                        if (Y >= R) {
                            bb = 'Y'; b = Y;
                            cc = 'R'; c = R;
                        } else {
                            bb = 'R'; b = R;
                            cc = 'Y'; c = Y;
                        }
                    }
                    while (b > c) {
                        cout << aa << bb;
                        a--;
                        b--;
                    }
                    if (a > b) {
                        while (a>=2) {
                            cout << aa << bb << aa << cc;
                            a-=2;
                            b--;
                            c--;
                        }
                    }
                }
                while (a + b + c != 0) {
                    if (a > 0) {cout << aa; a--;}
                    if (b > 0) {cout << bb; b--;}
                    if (c > 0) {cout << cc; c--;}
                }
                cout << endl;
            }
        
        }
    }
}