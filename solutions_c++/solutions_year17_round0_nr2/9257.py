#include<iostream>
#include<cstdlib>
#include<string>
#include<cmath>

#define large unsigned long long

using namespace std;

int main(){
    large Total;
    large len;
    large N;
    bool tidy;
    cin >> Total;

    for(int T = 0; T < Total; T++){
        cin >> N;
        for(large i = N; i >= 1;){
            large j;
            string I = to_string(i);
            len = I.length();

            tidy = true;

            for(j = len-1; j > 0; j--){
                if(int(I[j]) < int(I[j-1])){
                    tidy = false;
                    break;
                }
            }

            if(tidy){
                cout << "Case #" << T+1 << ": " << i << endl;
                break;
            }
            large padding = pow(10, (len - j));
            large frontI = i / padding - 1;
            i = frontI * padding + (padding - 1);
        }
    }
}
