#include <iostream>
#include <vector>
using namespace std;

void solve(const int& tc) {
    int r,c;
    cin >> r >> c;
    vector<vector<char>> a(r,vector<char>(c));
    for(int i=0;i<r;i++) {
        for(int j=0;j<c;j++) cin >> a[i][j];
    }
    for(int i=0;i<r;i++) {
        char clr = '?';
        for(int j=0;j<c;j++) {
            if(a[i][j] == '?') a[i][j] = clr;
            else clr = a[i][j];
        }
        for(int j=c-1;j>=0;j--) {
            if(a[i][j] == '?') a[i][j] = clr;
            else clr = a[i][j];
        }
    }
    vector<char> vect_clr(c,'?');
    const vector<char> blank(c,'?');
    for(int i=0;i<r;i++) {
        if(a[i] == blank) a[i] = vect_clr;
        else vect_clr = a[i];
    }
    for(int i=r-1;i>=0;i--) {
        if(a[i] == blank) a[i] = vect_clr;
        else vect_clr = a[i];
    } 
    cout << "Case #" << tc << ":" << endl;
    for(auto i:a) {
        for(auto j:i) cout << j;
        cout << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for(int i=1;i<=t;i++) solve(i);
}
