#include <iostream>
#include <string>

using namespace std;


int T;
int N, R, O, Y, G, B, V;

int main(){


    cin >> T;
    for(int t = 1; t <= T; t++){

        string answer = "";
        cin >> N >> R >> O >> Y >> G >> B >> V;
        bool possible = true;
        if((B <= O && O > 0) || (R <= G && G > 0) || (Y <= V && V > 0)){
            possible = false;
        }else if(B+O==N || R+G==N || Y+V==N){
            possible = false; 
        }
        else{

            B = B-O;
            R = R-G;
            Y = Y-V;

            //cout << t << B << R << Y << endl;


            if(B > R+Y || R > Y+B || Y > B+R){

                possible = false;

            }else{

                string acts = "B";
                if(R > B){
                    acts = "R";
                }

                if(acts == "R"){
                    R--;
                }else if(acts == "B"){
                    B--;
                }

                answer = acts;

                while(R+B+Y>0){
                    string newacts = "";
                    if(acts == "R"){
                        if(B >= Y){
                            newacts = "B";
                            B--;
                        }else{
                            newacts = "Y";
                            Y--;
                        }
                    }else if(acts=="B"){
                        if(R >= Y){
                            newacts = "R";
                            R--;
                        }else{
                            newacts = "Y";
                            Y--;
                        }
                    }else{
                        if(B >= R){
                            newacts = "B";
                            B--;
                        }else{
                            newacts = "R";
                            R--;
                        }
                    }
                    acts = newacts;
                    answer = answer + acts;
                }

                string addB = "B";
                for(int i = 0; i < O; i++){
                    addB = addB + "O" + "B";
                }
                string addR = "R";
                for(int i = 0; i < G; i++){
                    addR = addR + "G" + "R";
                }
                string addY = "Y";
                for(int i = 0; i < V; i++){
                    addY = addY + "V" + "Y";
                }

                if(O > 0){
                    for(int i = answer.size()-1; i >= 0; i--){
                        if(answer[i]=='B'){
                            answer.replace(i, 1, addB);
                            break;
                        }
                    }
                }
                if(G > 0){
                    for(int i = answer.size()-1; i >= 0; i--){
                        if(answer[i]=='R'){
                            answer.replace(i, 1, addR);
                            break;
                        }
                    }
                }
                if(V > 0){
                    for(int i = answer.size()-1; i >= 0; i--){
                        if(answer[i]=='Y'){
                            answer.replace(i, 1, addY);
                            break;
                        }
                    }
                }

            }
            
        }

        //special cases:
        if(B == O && B+O==N){
            possible = true;
            answer = "";
            for(int i = 0; i < O; i++){
                answer = answer + "BO";
            }
        }
        if(R== G && R+G==N){
            possible = true;
            answer = "";
            for(int i = 0; i < R; i++){
                answer = answer + "RG";
            }
        }if(V == Y && Y+V==N){
            possible = true;
            answer = "";
            for(int i = 0; i < V; i++){
                answer = answer + "VY";
            }
        }

        if(B == 1 && N == 1){
            possible = true;
            answer = "B";
        }
        if(Y == 1 && N == 1){
            possible = true;
            answer = "Y";
        }
        if(R == 1 && N == 1){
            possible = true;
            answer = "R";
        }
            

        if(possible){
            cout << "Case #" << t << ": " << answer << endl;
        }else{
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }

    }


    return 0;
}
