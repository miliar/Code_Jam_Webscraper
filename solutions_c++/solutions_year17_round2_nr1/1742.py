#include <iostream>
#include <vector>
#include <iomanip>
#include <fstream>

using namespace std;

ifstream in("A.in");
ofstream out("A.out");

int main(){
    int t;
    in >> t;
    for (int q = 0; q < t; q++){
        int n;
        long double d;
        long double maxt = 0;
        in >> d >> n;
        vector <long double> k(n);
        vector <long double> s(n);
        for (int i = 0; i < n; i++){
            in >> k[i] >> s[i];
            maxt = max(maxt, (d - k[i]) / s[i]);
        }
        out << fixed << setprecision(9) << "Case #" << q + 1 << ": " << d / maxt << endl;
    }
}
