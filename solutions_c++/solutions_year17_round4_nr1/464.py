#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        int n, p;
        cin >> n >> p;
        vector<int> vlr(p, 0);
        for (int i = 0; i < n; i++){
            int aux;
            cin >> aux;
            vlr[aux%p]++;
        }

        cout << "Case #" << cases++ << ": ";

        if (p == 2){
            cout << vlr[0]+((vlr[1]+1)/2) << endl;
        }
        else if (p == 3){
            int base = min(vlr[1], vlr[2]);
            vlr[1] -= base;
            vlr[2] -= base;
            int total = base + (vlr[1]+2)/3 + (vlr[2]+2)/3;
            cout << vlr[0]+total << endl;
        }
        else{
            int base = min(vlr[1], vlr[3]);
            vlr[1] -= base;
            vlr[3] -= base;
            int total = base + vlr[2]/2;
            int rest = vlr[2]%2;
            if (rest){
                total++;
                if (vlr[1] >= 2){
                    vlr[1] -= 2;
                }
                else if (vlr[3] >= 2){
                    vlr[3] -= 2;
                }
                else{
                    cout << vlr[0]+total << endl;
                    continue;
                }
            }
            total += (vlr[1]+3)/4 + (vlr[3]+3)/4;
            cout << vlr[0]+total << endl;

        }
    }
    return 0;
}
