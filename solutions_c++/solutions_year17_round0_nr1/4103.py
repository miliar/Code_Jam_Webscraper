#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    int T; cin >> T;
    for(int z = 1; z <= T; z++){
        string x; ll time;
        cin >> x; cin >> time;
        cout << "Case #" << z << ": ";
        ll timeuse = 0;
        ll iftrue = 1;
        for(ll i = 0; i < x.size(); i++){
            if(x[i] == '-'){
                if(i + time - 1 >= x.size()){
                    cout << "IMPOSSIBLE" << endl;
                    iftrue = 0;
                    break;
                }
                for(ll j = 0; j < time; j++){
                   if(x[i+j] == '+'){
                        x[i+j] = '-';
                   }
                   else if(x[i+j] == '-') x[i+j] = '+';
                }
                timeuse ++;
            }
        }
        if(iftrue) cout << timeuse << endl;
    }
}
