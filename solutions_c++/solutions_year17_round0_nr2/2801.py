#include <iostream>
#include <string>

using namespace std;

bool is_tidy(string k){
    bool b = true;
    for (int i = 0; i < k.size()-1; i++){
        b = b && (k[i] <= k[i+1]);
    }
    return b;
}

int main()
{
    int n;
    cin >> n;
    for (int k = 1; k <= n; k++){
        string max;
        cin >> max;
        while (!is_tidy(max)){ //it`s also checking for tidy
            for (int i = 0; i < max.size()-1; i++){//checking for incorect include
                if (max[i] > max[i+1]){ //making tidy number after first incorect include
                    max[i]--;
                    for (int j = i+1; j < max.size(); j++){//make nines
                        max[j] = '9';
                    }
                    break;
                }
            }
        }
        long long tidy = std :: stol(max);

        cout << "Case #" << k << ": " << tidy << endl;
    }
    return 0;
}
