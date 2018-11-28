#include <iostream> 

using namespace std;

bool istidy(long long int n){
    bool t = true;
    int prev = 10;
    for(long long int i = n; i > 0; i = i/10){
        if(i%10 > prev){
            t = false;
        }
        prev = i%10;
    }
    return t;
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        
        long long int N;
        cin >> N;
        long long int fval = N;
        while(!istidy(fval)){
            fval = fval - (fval%10) - 1;
        }
        
        cout << "Case #"<< (i+1) << ": " << fval << endl;
    }
}