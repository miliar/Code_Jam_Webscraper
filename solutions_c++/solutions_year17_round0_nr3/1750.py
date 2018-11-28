#include <iostream>
#include <fstream>

using namespace std;

ifstream in("C.in");
ofstream out("C.out");

int main(){
    int q;
    in >> q;
    for (int t = 0; t < q; t++){
        long long n, k;
        in >> n >> k;
        if (k == 1){
            out << "Case #" << t + 1 << ": " << (n) / 2 << " " << (n - 1) / 2 << endl;
            continue;
        }
        long long mx2 = 1;
        while (mx2 < k){
            mx2 = mx2 * 2 + 1;
        }
        mx2 /= 2;
        //cout << mx2 << endl;
        long long free = (n - mx2) / (mx2 + 1);
        long long bigger = n - free * (mx2 + 1) - mx2;
        //cout << free << " " << bigger << endl;
        if (bigger > k - mx2 - 1){
            out << "Case #" << t + 1 << ": " << (free + 1) / 2 << " " << (free + 0) / 2 << endl;
        }
        else {
            out << "Case #" << t + 1 << ": " << (free + 0) / 2 << " " << (free - 1) / 2 << endl;
        }
    }
}
