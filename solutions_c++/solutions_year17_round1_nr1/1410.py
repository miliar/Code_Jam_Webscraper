#include <iostream>
#include <cstdio>  
#include <iostream>  
#include <string>  
#include <iterator>  
#include <algorithm>  
#include <vector>  
#include <cstring>  
#include <array>  
#include <queue>  
#include <set>  
#include <map>  
using namespace std;

char cake[30][30];
int t;  
int R, C;

void solve() {
    for(int i=0;i<R;i++) {
        char pre = '?';
        for(int j=0;j<C;j++) {
            char c = cake[i][j];
            if(c != '?') {
                pre = c;

            }
            else {
                cake[i][j] = pre;
            }
        }
    }
    for(int i=0;i<R;i++) {
        char pre = '?';
        for(int j=C-1;j>=0;j--) {
            char c = cake[i][j];
            if(c != '?') {
                pre = c;

            }
            else {
                cake[i][j] = pre;
            }
        }
    }
    for(int i=0;i<C;i++) {
        char pre = '?';
        for(int j=R-1;j>=0;j--) {
            char c = cake[j][i];
            if(c != '?') {
                pre = c;

            }
            else {
                cake[j][i] = pre;
            }
        }
    }
    for(int i=0;i<C;i++) {
        char pre = '?';
        for(int j=0;j<R;j++) {
            char c = cake[j][i];
            if(c != '?') {
                pre = c;

            }
            else {
                cake[j][i] = pre;
            }
        }
    }
}

// char val[1010] = {0};

int main()  
{  
    freopen("A-large.in.txt", "r", stdin);  
    //freopen("in.txt", "r",stdin);  
    freopen("out.txt", "w", stdout);  
    memset(cake, '?', sizeof(cake));
    scanf("%d", &t);  
    char c;
    for(int k=1;k<=t;k++) {
        scanf("%d %d", &R, &C);
        for(int i=0;i<R;i++) {
            for(int j=0;j<C;j++) {
                cin>>c;
                cake[i][j] = c;
            }
        }
        solve();
        printf("Case #%d:\n", k);
        for(int i=0;i<R;i++) {
            for(int j=0;j<C;j++) {
                cout<<cake[i][j];
            }
            cout<<endl;
        }
    }

    return 0;  
}  