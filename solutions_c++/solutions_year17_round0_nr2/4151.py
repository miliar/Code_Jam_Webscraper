#include <iostream>
#include <string>

using namespace std;

long long power(int x, int y){
    if(y <= 0) return 1;
    else return power(x, y-1) * x;
}

long long tidy(long long num){
    int pow = 0;
    while(num > power(10,pow)){
        // cout << "fak";
        // cout << (num % power(10, pow+2))/power(10, pow+1) << " " << (num % power(10, pow+1))/power(10, pow) << " | ";
        if( (num % power(10, pow+2))/power(10, pow+1) > (num % power(10, pow+1))/power(10, pow) ){
            // cout << (num/power(10, pow+2)) * power(10, pow+2) << " " << (num % power(10, pow+2))/power(10, pow+1) * power(10,pow+1) << " | ";
            num = (num/power(10, pow+2)) * power(10, pow+2) + (num % power(10, pow+2))/power(10, pow+1) * power(10,pow+1) - 1;
        }
        pow++;
    }
    return num;
}

int main(){
    int numIn;
    long long T[100];
    cin >> numIn;
    for(int i=0; i<numIn; i++){
        cin >> T[i];
    }

    for(int i=0; i<numIn; i++){
        long long result = tidy(T[i]);
        cout << "Case #" << i+1 << ": " << result << "\n";
    }
}