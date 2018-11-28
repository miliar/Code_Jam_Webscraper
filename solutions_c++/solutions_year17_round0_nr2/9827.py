#include <iostream>
#include <string>

using namespace std;

int main(void){
    int T;
    string n;
    cin >> T;
    bool back;
    for (int t = 1; t <= T; t++){
        cin >> n;
        back = false;
        for (int i = 0; i < n.size() - 1 && !back; i++){
            if (n[i] > n[i + 1]){
                if (n[i] == '0'){
                    n[i] = '9';
                } else {
                    n[i] = n[i] - 1;
                }
                for (int j = i + 1; j < n.size(); j++){
                    n[j] = '9';
                }
                back = true;
                for (int j = i; j > 0; j--){
                    if (n[j] < n[j - 1]){
                        n[j] = '9';
                        if (n[j - 1] == '0'){
                            n[j - 1] = '9';
                        } else {
                            n[j - 1] = n[j - 1] - 1;
                        }
                    }
                }
            }
        }
        if (n[0] == '0'){
            n.erase(n.begin());
        }
        cout << "Case #" << t << ": " << n << endl;
    }
    return 0;
}
