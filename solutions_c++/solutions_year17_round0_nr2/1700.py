#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

ifstream in("B.in");
ofstream out("B.out");

int main(){
    int q;
    in >> q;
    for (int t = 0; t < q; t++){
        long long n;
        vector <int> r;
        in >> n;
        int k = 0;
        while (n != 0){
            r.push_back(n % 10);
            n /= 10;
            k++;
        }
        int fr = k, mn = 9;
        for (int i = 0; i < k; i++){
            if (r[i] > mn){
                r[i]--;
                fr = k - i;
            }
            mn = r[i];
        }
        long long res = 0;
        for (int i = 0; i < fr; i++){
            if (r[k - i - 1] != 0){
                res = res * 10 + r[k - i - 1];
            }
            //cout << res << endl;
        }
        for (int i = 0; i < k - fr; i++){
            res = res * 10 + 9;
            //cout << res << endl;
        }
        out << "Case #" << t + 1 << ": " << res << endl;
    }
}
