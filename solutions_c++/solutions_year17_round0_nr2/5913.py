#include <iostream>
#include <string>
using namespace std;

int c(char x){
    return x - 48;
}

bool check(string n){
    for(int i = 1; i < n.size(); i++){
        if(c(n[i - 1]) > c(n[i]))
            return false;
    }
    return true;
}


string clear(string n){
    string aux = "";

    bool change = false;
    for(int i = 0; i < n.size(); i++){

        if(n[i] == '0' && !change)
            continue;
        else
            change = true;

        if(change)
            aux += n[i];
    }

    return aux;
}

inline string calc (string n){
    if(check(n))
        return n;
    for(int i = 1; i < n.size(); i++){
        if(c(n[i]) < c(n[i - 1])){
            if(c(n[i - 1]) >= 2){

                n[i - 1] = c(n[i - 1]) - 1 + 48;
                for(int j = i; j < n.size(); j++){
                    n[j] = '9';
                }
                return calc(clear(n));
            }else if(c(n[i - 1]) == 1 && c(n[i]) == 0){
                n[i - 1] = '0';
                for(int j = i; j < n.size(); j++){
                    n[j] = '9';
                }
                return calc(clear(n));
            }
        }
    }

    return n;
}




int main(){
    int t;
    string n;
    int caso = 0;
    cin >> t;
    while(t--){
        cin >> n;

        cout << "Case #" << caso + 1 << ": ";
        cout << calc(n) << "\n";
        caso++;
    }

    return 0;
}
