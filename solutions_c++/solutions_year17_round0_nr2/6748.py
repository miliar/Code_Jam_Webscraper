#include <iostream>
#include <cmath>

using namespace std;

bool isTidy(unsigned long &number){
    int lastDigit = 9;
    int counter = 0;

    do{
        int digit = number % 10;
        if (digit > lastDigit){
            //optimization for large set
            unsigned long tens = pow(10, counter);
            number = number*tens;
            return false;
        }

        lastDigit = digit;
        number = number/10;
        counter++;

    }while(number>0);

    return true;
}


int main(){
    int T;
    cin >> T;

    for(int c = 0; c < T; c++){
        unsigned long N;
        cin >> N;
        unsigned long copy = N;
        while(!isTidy(copy)){
            copy--;
            N = copy;
        }

        cout << "Case #"<<(c+1)<<": "<<N<<endl;
    }
}
