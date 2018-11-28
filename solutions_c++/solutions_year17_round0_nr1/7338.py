#include <iostream>
#include <cstring>
using namespace std;
int main(){
    int n;
    int k;
    int length;
    int counter = 0;
    bool find = true;

    cin >> n;

    char cake[1003];
    for(int round = 1; round <= n; round++){
        cin >> cake >> k;
        length = strlen(cake)- k;
        for(int i = 0; i < length; i++){
            if(cake[i] == '+')
                continue;
            counter++;
            cake[i] = '+';
            for(int j = i + 1; j < i + k; j++){
                if(cake[j] == '+')
                    cake[j] = '-';
                else
                    cake[j] = '+';
            }
        }
        if(cake[length] == '-'){
            counter++;
            for(int j = length ; j < strlen(cake); j++){

                    if(cake[j] == '+')
                        cake[j] = '-';
                    else
                        cake[j] = '+';
            }
        }

        for(int i = 0; i < strlen(cake); i++){
            if(cake[i] == '-'){
                find = false;
                break;
            }
        }

        if(find)
            cout << "Case #" << round << ": " << counter << endl;
        else
            cout << "Case #" << round << ": " << "IMPOSSIBLE" << endl;

        find = true;
        counter = 0;
    }
    return 0;
}
