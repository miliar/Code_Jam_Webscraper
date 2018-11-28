#include <iostream>

using namespace std;

int main(){
    int t, k, res;
    cin >> t;
    for (int i = 1; i <= t; ++i){

        res = 0;
        string pancakes;
        cin >> pancakes >> k;

        for(int j = 0; j < pancakes.length() - k + 1; j++){
            if(pancakes.at(j) == '-'){
                res++;
                for(int w = 1; w < k; w++){
                    if (pancakes.at(j + w) == '+'){
                        pancakes.at(j + w) = '-';
                    } else (pancakes.at(j + w) = '+');

                }
                //cout << pancakes << endl;
            }
        }

        for (int j = pancakes.length() - k + 1; j < pancakes.length(); j++){
            if(pancakes.at(j) == '-'){
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
                res = -1;
                break;
            }
        }

    if(res >= 0) {
        cout << "Case #" << i << ": " << res << endl;
    }
    }

}