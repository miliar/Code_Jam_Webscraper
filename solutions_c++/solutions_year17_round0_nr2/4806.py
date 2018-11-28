#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI acos(-1)
#define endl '\n'
using namespace std;

typedef long long ll;

int main() {

    int t;
    string n;

    cin >> t;
    for(int i = 1; i <= t; i++) {

        cin >> n;
        int len = n.length();
        bool foundZero = false;
        
        for(int j = len - 1; j >= 0; j--) {

            //548
    
            if(n[j] == '0') {
                foundZero = true;
                n[j] = '9';  
            
                int k = j;
                while(k < len - 1 && n[k + 1] < n[k]) {
                    n[++k] = '9';
                }
                /*if(j < len - 1 && n[j + 1] < n[j])
                    n[j + 1] = '9';*/
            }
            else {
                if(foundZero) {
                    n[j]--;
                    foundZero = false;
                }
                else {
                    int k = j;
                    int aux = n[j];
                    while(k < len - 1 && n[k + 1] < n[k]) {
                        n[++k] = '9';
                        n[j] = aux - 1;
                    }
                }/*if(j < len - 1 && n[j + 1] < n[j]) {
                    n[j + 1] = '9';
                    n[j]--;
                }  */       
            }
        }            

        cout << "Case #" << i << ": ";// << n << endl;
        bool leadingZeroes = true;
        for(int i = 0; i < len; i++) {
            if(n[i] != '0')
                leadingZeroes = false;
            if(!leadingZeroes)
                cout << n[i];
        }
        cout << endl;

    }

    return 0;
}
