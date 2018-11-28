#include<iostream>
#include<cstdlib>
#include<string>
#include<cmath>

#define large unsigned long long

using namespace std;

int main(){
    unsigned int To, len;
    large N;
    bool tidy;
    cin >> To;

    for(int T = 0; T < To; T++){
        cin >> N;
        for(large i = N; i >= 1;){
            large j;
            string strI = to_string(i);
            len = strI.length();

            tidy = true;

            for(j = len-1; j > 0; j--){
                if(int(strI[j]) < int(strI[j-1])){
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
