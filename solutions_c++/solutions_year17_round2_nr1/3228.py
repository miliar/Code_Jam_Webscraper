#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;


double solve(int d, int n, vector<int> k, vector<int>s){
    vector<double> time(n);
    for (int i = 0; i < n; i++) {
        time[i] = (double)(d-k[i])/s[i];
    }
    sort(time.begin(),time.end());
    return d/time.back();
}

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int d,n;
        cin >> d >> n;
        vector<int> k(n);
        vector<int> s(n);
        for (int j = 0; j < n; j++) {
            cin >> k[j] >> s[j];
        }
        double answer;
        answer = solve(d, n, k, s);
        std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
        cout << "Case #" << (i+1) << ": " << std::setprecision(6) << answer << endl;
    }
    return 0;
}
