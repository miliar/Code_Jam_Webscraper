#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int casos;
    cin >> casos;
    for ( int i = 0 ; i < casos ; i++){
        priority_queue<int> colita;
        string res = "";
        int a, b;
        cin >> a;
        cin >> b;
        int min = a;
        colita.push(a);
        if ( b <= a/2 +a/4) {
            while (b > 1 && colita.top() > 0) {
                int c = colita.top();
                colita.pop();
                c--;
                if (c / 2 < min) min = c / 2;
                colita.push(int((c + 1) / 2));
                colita.push(int(c / 2));
                b--;
            }
            cout << "Case #" << i + 1 << ": " << colita.top() / 2 << " " << (colita.top() - 1) / 2 << endl;
        } else {
            cout << "Case #" << i + 1 << ": 0 0" << endl;
        }
    }
    return 0;
}