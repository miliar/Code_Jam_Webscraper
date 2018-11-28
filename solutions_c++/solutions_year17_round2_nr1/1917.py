#include <vector>
#include <iostream>
#include <map>
#include <tuple>
using namespace std;


int main(){
    int n;
    cin >> n;
    cout.precision(10);
    cout << fixed;
    for(int i = 0; i < n; i++){
        cout << "Case #" << i + 1<< ": ";
        int d, n;
        cin  >> d >> n;
        vector<pair<int,int>> horses;
        for(int j = 0; j < n ; j ++){
            pair<int, int> tmp;

            cin >> tmp.first >> tmp.second;

            horses.push_back(tmp);
        }

        long double res = 10000000000000000;

        for(auto a : horses){
             
            res = min(res, (long double)(d) / ((d - a.first) / (long double)a.second));
        }

        cout << res;

        cout << endl;

    }
}
