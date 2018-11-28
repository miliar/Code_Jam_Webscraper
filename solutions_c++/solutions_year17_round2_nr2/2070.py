/*
 Round 1B - Question 2: Stable Neigh-bors
 @author: Christopher W. Frost
 */

#include<iostream>
#include<vector>
//#include<string>
//#include<cmath>
//#include<algorithm>
//#include<iomanip>
using namespace std;


int main(){
    int T;
    cin >> T;
    
    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        
        int numR, numY, numB;
        numR = R + O + V;
        numY = Y + O + G;
        numB = B + G + V;
        
        if(numR > N/2 || numY > N/2 || numB > N/2)
            cout << "IMPOSSIBLE\n";
        else{
            vector<char> stalls;
            while(N > 0){
                //if(O != 0 || G != 0 || V != 0){
                    if(numR >= numY && numR >= numB){
                    numRBlock: ;
                        if(!stalls.empty() && (stalls.back() == 'O' || stalls.back() == 'V' || stalls.back() == 'R')){
                            if(Y >= B)
                                goto numYBlock;
                            else{
                                goto numBBlock;
                            }
                        }

                        if(O == 0 && V == 0){
                            stalls.push_back('R');
                            R--;
                            numR--;
                        }
                        else if(O >= V){
                            int limit = (!stalls.empty() && stalls.back() == 'B') ? 1 : 2;
                            if(B >= limit){
                                if(limit == 1){
                                    stalls.push_back('O');
                                    stalls.push_back('B');
                                    O--;
                                    B--;
                                    numR--;
                                    numY--;
                                    numB--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('B');
                                    stalls.push_back('O');
                                    stalls.push_back('B');
                                    O--;
                                    B-=2;
                                    numR--;
                                    numY--;
                                    numB-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('O');
                                O--;
                                numR--;
                                numY--;
                            }
                        }
                        else{
                            int limit = (!stalls.empty() && stalls.back() == 'Y') ? 1 : 2;
                            if(Y >= limit){
                                if(limit == 1){
                                    stalls.push_back('V');
                                    stalls.push_back('Y');
                                    V--;
                                    Y--;
                                    numR--;
                                    numB--;
                                    numY--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('Y');
                                    stalls.push_back('V');
                                    stalls.push_back('Y');
                                    V--;
                                    Y-=2;
                                    numR--;
                                    numB--;
                                    numY-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('V');
                                V--;
                                numR--;
                                numB--;
                            }
                        }
                    }
                    
                    else if(numY >= numB){
                    numYBlock: ;
                        if(!stalls.empty() && (stalls.back() == 'Y' || stalls.back() == 'O' || stalls.back() == 'G')){
                            if(B >= R)
                                goto numBBlock;
                            else{
                                goto numRBlock;
                            }
                        }

                        if(O == 0 && G == 0){
                            stalls.push_back('Y');
                            Y--;
                            numY--;
                            
                        }
                        else if(O >= G){
                            int limit = (!stalls.empty() && stalls.back() == 'B') ? 1 : 2;
                            if(B >= limit){
                                if(limit == 1){
                                    stalls.push_back('O');
                                    stalls.push_back('B');
                                    O--;
                                    B--;
                                    numR--;
                                    numY--;
                                    numB--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('B');
                                    stalls.push_back('O');
                                    stalls.push_back('B');
                                    O--;
                                    B-=2;
                                    numR--;
                                    numY--;
                                    numB-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('O');
                                O--;
                                numR--;
                                numY--;
                            }
                        }
                        else{
                            int limit = (!stalls.empty() && stalls.back() == 'R') ? 1 : 2;
                            if(R >= limit){
                                if(limit == 1){
                                    stalls.push_back('G');
                                    stalls.push_back('R');
                                    G--;
                                    R--;
                                    numB--;
                                    numY--;
                                    numR--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('R');
                                    stalls.push_back('G');
                                    stalls.push_back('R');
                                    G--;
                                    R-=2;
                                    numB--;
                                    numY--;
                                    numR-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('G');
                                G--;
                                numB--;
                                numY--;
                            }
                        }
                    }
                    
                    else{
                    numBBlock: ;
                        if(!stalls.empty() && (stalls.back() == 'B' || stalls.back() == 'G' || stalls.back() == 'V')){
                            if(R >= Y)
                                goto numRBlock;
                            else{
                                goto numYBlock;
                            }
                        }

                        if(G == 0 && V == 0){
                            stalls.push_back('B');
                            B--;
                            numB--;
                        }
                        else if(G >= V){
                            int limit = (!stalls.empty() && stalls.back() == 'R') ? 1 : 2;
                            if(R >= limit){
                                if(limit == 1){
                                    stalls.push_back('G');
                                    stalls.push_back('R');
                                    G--;
                                    R--;
                                    numB--;
                                    numY--;
                                    numR--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('R');
                                    stalls.push_back('G');
                                    stalls.push_back('R');
                                    G--;
                                    R-=2;
                                    numB--;
                                    numY--;
                                    numR-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('G');
                                G--;
                                numB--;
                                numY--;
                                
                            }
                        }
                        else{
                            int limit = (!stalls.empty() && stalls.back() == 'Y') ? 1 : 2;
                            if(Y >= limit){
                                if(limit == 1){
                                    stalls.push_back('V');
                                    stalls.push_back('Y');
                                    V--;
                                    Y--;
                                    numR--;
                                    numB--;
                                    numY--;
                                    N--;
                                }
                                else{
                                    stalls.push_back('Y');
                                    stalls.push_back('V');
                                    stalls.push_back('Y');
                                    V--;
                                    Y-=2;
                                    numR--;
                                    numB--;
                                    numY-=2;
                                    N-=2;
                                }
                            }
                            else{
                                stalls.push_back('V');
                                V--;
                                numR--;
                                numB--;
                            }
                        }
                    }
                    N--;
                //}

            }
            
            if(stalls.front() == stalls.back() && stalls.size() >= 3){
                char temp = stalls.back();
                stalls.back() = stalls[stalls.size()-2];
                stalls[stalls.size()-2] = temp;
            }
            
            //PRINT RESULTS
            for (auto z : stalls)
                cout << z;
            cout << '\n';
        }
    }
}
