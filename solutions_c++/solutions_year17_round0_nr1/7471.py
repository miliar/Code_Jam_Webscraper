#include <iostream>
#include <string>

using namespace std;

int T, K;
string S;

int main(){

    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> S >> K;
        getchar();

        int i = 0;
        int answer = 0;
        while((int) S.size() - i >= K){
            if(S[i]=='-'){
                answer++;
                for(int j = i; j < i+K; j++){
                    if(S[j]=='+'){
                        S[j]='-';
                    }else{
                        S[j]='+';
                    }
                }
            }
            i++;
        }

        bool possible = true;
        for(int i = 0; i < S.size(); i++){
            if(S[i]=='-'){
                possible = false;
            }
        }

        if(!possible){
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << t << ": " << answer << endl;
        }


    }





    return 0;
}
