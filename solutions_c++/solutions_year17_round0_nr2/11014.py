#include <iostream>
#include <vector>

using namespace std;

vector<int> digits(int n);
bool isTidy(int n);

int main(){
    int t, n, tidy;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        tidy = 0;
        cin >> n;
        if(n < 10 )
            cout << "Case #" << i << ": " << n << endl;
        else{
            for(int j = 1; j <= n; j++){
                if( isTidy(j) )
                    tidy = j;

            }
            cout << "Case #" << i << ": " << tidy << endl;
        }

    }

    return 0;
}

vector<int> digits(int n){
    vector<int> digits;
    int aux = 0;

    while(n > 0){

        aux = n % 10;
        digits.push_back( aux );
        n = n / 10;

    }

    return digits;
}

bool isTidy(int n){
    vector<int> digi;
    int cont = 0;

    if(n < 10){
        return true;
    }else{
        digi = digits(n);

        for(int i = 0; i < digi.size() - 1; i++){
            if(digi[i] >= digi[i+1] )
                cont++;
        }
        if(cont == digi.size()-1)
            return true;
        else
            return false;
    }
}
