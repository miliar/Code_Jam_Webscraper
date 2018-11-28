#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("op.txt", "w", stdout);

    int t;
    cin >> t;
    for(int q = 0; q<t; ++q) {
        
        ll r, c, n;
        cin >> r >> c;
        n = max(r,c);

        char cake[25][25];
        int count = 0;
        
        for(int i = 0; i<r; ++i) {
            for(int j = 0; j<c; ++j) {
                cin >> cake[i][j];
                if(cake[i][j] == '?') {
                    count++;
                }
            }
        }
        
        //horz pass
        for(int i = 0; i<r; ++i) {
            for(int j = 0; j<c && count>0; ++j) {
                if(cake[i][j] == '?') {
                    int f = 0, w = 1;
                    while(w < n && !f) {
                        int ud = i - w;
                        int dd = i + w;
                        if(ud>=0) {
                            if(cake[ud][j] != '?') {
                                f = 1;
                                cake[i][j] = cake[ud][j];
                                count--;
                            }
                        }
                        if(dd<r &&!f) {
                            if(cake[dd][j] != '?') {
                                f = 1;
                                cake[i][j] = cake[dd][j];
                                count--;
                            }
                        }
                        w++;
                    }
                }
            }
        }
//
//        cout << "\n\nAfter hoez pass\n\n";
//        for(int i = 0; i<r; ++i) {
//            for(int j = 0; j<c; ++j) {
//                cout << cake[i][j];
//            }
//            cout << endl;
//        }
        
        //vert pass
        for(int j = 0; j<c; ++j) {
            for(int i = 0; i<r && count>0; ++i) {
                if(cake[i][j] == '?') {
                    int f = 0, w = 1;
                    while(w < n && !f) {
                        int ud = j - w;
                        int dd = j + w;
                        if(ud>=0) {
                            if(cake[i][ud] != '?') {
                                f = 1;
                                cake[i][j] = cake[i][ud];
                                count--;
                            }
                        }
                        if(dd<c &&!f) {
                            if(cake[i][dd] != '?') {
                                f = 1;
                                cake[i][j] = cake[i][dd];
                                count--;
                            }
                        }
                        w++;
                    }
                }
            }
        }
        
        if(count) {
            cout << "\n\n\nYou're screwed!!" << count << "\n\n\n";
        }
        cout << "Case #" << q+1 << ":" << endl;
        for(int i = 0; i<r; ++i) {
            for(int j = 0; j<c; ++j) {
                cout << cake[i][j];
            }
            cout << endl;
        }
        
    }

    return 0;
}
