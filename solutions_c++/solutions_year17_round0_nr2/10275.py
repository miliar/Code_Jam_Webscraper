#include<iostream>

using namespace std;

bool is_tidy(int n){
    int a = n % 10;
    n = n / 10;

    if(n < 1){
        return true;
    }

    while(n > 0){
        int b = n % 10;
        n = n / 10;
        if(a < b){
            return false;
        }
        a = b;
    }

    return true;
}

int main(){
    int n;
    int count = 1;
    cin >> n;

    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        for(int j = x; j > 0; j--){
            if(is_tidy(j)){
                cout << "Case #" << count << ": " << j << endl;
                count++;
                break;
            }
            continue;
        }
    }
}
