#include<iostream>
using namespace std;
void p(int _) {
    string n;
    cin >> n;
    cout << "Case #" << _ << ": ";
    for(int i = 1; i < n.size(); i ++) {
        if(n[i] < n[i - 1]) {
            int k = i - 1;
            while(k > 0 && n[k - 1] == n[k])    k --;
            for(int j = 0;j < k; j ++) {
                cout << n[j];
            }
            if(!(k == 0 && n[k] == '1')) cout << n[k] - '0' - 1;
            for(int j = k + 1; j < n.size(); j ++) {
                cout << 9;
            }
            return;
        }
    }
    cout << n;
    return;
}
int main() {
    int t;
    cin >> t;
    for(int i = 0; i < t; i ++) {
        p(i + 1);
        cout << endl;
    }
}
