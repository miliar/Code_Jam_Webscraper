#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

int main() {
    int casos;
    cin >> casos;
    for ( int i = 0 ; i < casos ; i++){
        vector<string> colita;
        string res = "";
        string a;
        int b;
        cin >> a;
        cin >> b;
        res.append(a.size(), '+');
        int cont = 0;

        colita.push_back(a);
        for (int j = 0; j + b - 1 <a.size() ; j++){
            if(a[j] == '-'){
                cont ++;
                for (int k = j; k < j+b  ; k++){
                    if (a[k]=='+') a[k] = '-';
                    else a[k] = '+';
                }
            }
        }
        if (a == res) cout << "Case #" << i + 1 << ": "  << cont << endl;
        else cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
    return 0;
}