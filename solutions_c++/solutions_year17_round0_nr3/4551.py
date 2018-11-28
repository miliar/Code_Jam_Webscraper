#include<iostream>
#include<fstream>
#include<queue>
#include<cmath>
using namespace std;

int main() {
    ifstream fin("3.in");
    ofstream cout("3.out");
    priority_queue<int> h;
    int num_test;
    fin >> num_test;
    for (int iter_test = 0; iter_test < num_test; iter_test ++){
        
        cout << "Case #" << iter_test + 1 << ": ";
        int n, k;
        fin >> n >> k;
        //cout << n << k << endl;
        h.push(n);

        int x, y;
        for (int i = 0; i < k; i++) {
            int z = h.top();
            x = (z - 1) / 2;
            y = z - 1 - x;
            //cout << x << y << endl;
            //cin >> n;
            h.pop();
            h.push(x);
            h.push(y);
        }
        while (!h.empty()) h.pop();
        cout << max(x, y) << " " << min(x,y) << endl;
    }
}
