#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    int K;
    cin >> K;
    int caso = 1;
    while (K--){
        long long numbr;
        cin >> numbr;
        vector<int> numbers;
        int mayor = ((long long)(numbr / pow(10,floor(log10(numbr)) )) % 10);
        for (int i=log10(numbr); i>= 0  ; i--){
            numbers.push_back(((long long)(numbr / pow(10,i) ) % 10));
        }

        for (int j=1; j<numbers.size() ; j++){
            if (numbers[0] <=0){
                for (int e=1;e< numbers.size() ; e++)
                numbers[e] = 9;
                continue;
            }

            if (numbers[j] < mayor){
                numbers[j-1]--;
                for (int e=j;e< numbers.size() ; e++){
                  numbers[e] = 9;
                }

                j-=2;
            }
            mayor = numbers[j];
        }
        cout << "Case #" << caso << ": ";
        if (numbers[0]){
           for (int j=0; j<numbers.size() ; j++){
                cout << numbers[j];
            }
            cout << endl;

        }
        else {
           for (int j=1; j<numbers.size() ; j++){
                cout << numbers[j];
            }
            cout << endl;
        }

        caso++;
    }
    return 0;
}
