#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <tuple>
using namespace std;


int main(){
    int nca;
    cin >> nca;
    for(int i = 0; i < nca; i++){

        int k, n;
        cin >> n >> k;
        std::vector<double> begp;
        double units;
        cin >> units;
        for(int j = 0; j < n; j++){
            double tmp;
            cin >> tmp;
            begp.push_back(tmp);
        }

        sort(begp.begin(), begp.end());

        while(units > 0.0000000001){
            int j;
            double first = begp[0];
            double next;
            for(j = 1; j < k; j++){
                if(begp[j] > first){
                    break;
                }
            
            }
            next = begp[j];
            if(j == n){
                next = 1.0;
            }
            if( (next - first) * (double) (j) <= units){
                units -= (next - first) * (double) (j);
                for(int k = 0; k < j; k ++){
                    begp[k] = next;
                       
                }
            } else {
                for(int k = 0; k < j; k ++){
                    begp[k] += units / (double) (j);
                }
                units = 0;
            }

        }

        double fp = 1.0;
        for(auto a : begp){
            fp *= a;
        }

        cout << fixed;
        cout.precision(10);
        cout << "Case #" << i + 1<< ": ";
        cout << fp;
        cout << endl;

    }
}
