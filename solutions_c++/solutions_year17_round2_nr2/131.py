#include <bits/stdc++.h>

using namespace std;

int a[30001];

int main()
{
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (int cur = 0; cur < t; cur++){
        cout << "Case #" << cur + 1 << ": ";
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        if ((o > b - 1 && o != 0) || (g > r - 1 && g != 0) || (v > y - 1 && v != 0)){
            if (o == b && g == r && y == v && o == 0 && g == 0){
                for (int i = 0; i < n; i++){
                    if (i & 1) cout << "Y";
                    else cout << "V";
                }
            }
            else if (o == b && g == r && y == v && o == 0 && y == 0){
                for (int i = 0; i < n; i++){
                    if (i & 1) cout << "R";
                    else cout << "G";
                }
            }
            else if (o == b && g == r && y == v && y == 0 && g == 0){
                for (int i = 0; i < n; i++){
                    if (i & 1) cout << "B";
                    else cout << "O";
                }
            }
            else
                cout << "IMPOSSIBLE";
            cout << "\n";
            continue;
        }
        b -= o;
        r -= g;
        y -= v;
        if (b + r < y || b + y < r || r + y < b){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        int z = r + b + y;
        int x = (r > b && r > y) ? 1 : (b > y ? 2 : 3);
        for (int i = 0; i < z; i += 2){
            if (x == 1){
            if (r > 0){
                r--;
                a[i] = 1;
            }
            else if (b > 0){
                b--;
                a[i] = 2;
            }
            else{
                y--;
                a[i] = 3;
            }
            }
            else if (x == 2){
            if (b > 0){
                b--;
                a[i] = 2;
            }
            else if (r > 0){
                r--;
                a[i] = 1;
            }
            else{
                y--;
                a[i] = 3;
            }
            }
            else{
            if (y > 0){
                y--;
                a[i] = 3;
            }
            else if (b > 0){
                b--;
                a[i] = 2;
            }
            else{
                r--;
                a[i] = 1;
            }
            }
        }
        for (int i = 1; i < z; i += 2){
            if (x == 1){
            if (r > 0){
                r--;
                a[i] = 1;
            }
            else if (b > 0){
                b--;
                a[i] = 2;
            }
            else{
                y--;
                a[i] = 3;
            }
            }
            else if (x == 2){
            if (b > 0){
                b--;
                a[i] = 2;
            }
            else if (r > 0){
                r--;
                a[i] = 1;
            }
            else{
                y--;
                a[i] = 3;
            }
            }
            else{
            if (y > 0){
                y--;
                a[i] = 3;
            }
            else if (b > 0){
                b--;
                a[i] = 2;
            }
            else{
                r--;
                a[i] = 1;
            }
            }
        }
        bool fr = 0, fb = 0, fy = 0;
        for (int i = 0; i < z; i++){
            if (a[i] == 1) {
                if (!fr){
                    fr = true;
                    for (int i = 0; i < g; i++)
                        cout << "RG";
                }
                cout << "R";
            }
            else if (a[i] == 2) {
                if (!fb){
                    fb = true;
                    for (int i = 0; i < o; i++)
                        cout << "BO";
                }
                cout << "B";
            }
            else{
                if (!fy){
                    fy = true;
                    for (int i = 0; i < v; i++)
                        cout << "YV";
                }
                cout << "Y";
            }
        }
        cout << "\n";
    }
    return 0;
}

