#include <iostream>

using namespace std;


int T, N, D;
int K[1007];
int S[1007];
long double answer;

int main(){

    cin >> T;
    for(int i = 1; i <= T; i++){

        cin >> D >> N;
        for(int j = 1; j <= N; j++){
            cin >> K[j] >> S[j];
        }

        long double max = 0;

        for(int j = 1; j <= N; j++){

            K[j] = D-K[j];
            long double act = (long double) K[j]/S[j];

            if(act > max){
                max = act;
            }
        }

        answer = D/max;

        cout.precision(10);
        
        cout << "Case #" << i << ": " << answer << endl;
    }


            






    return 0;
}
