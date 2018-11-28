#include <string>
#include <fstream>
#include <iostream>
#include <vector>

//std::ifstream cin("large_input.in");
//std::ofstream cout("large_output.out");

using std::string;
using std::cout;
using std::vector;
using std::cin;

int main() {
    int T;
    int R,C;
    string row;
    cin >> T;
    int x,y;
    char pred;
    for(int e=1;e<=T;++e){
        cin >> R >> C;
        vector<string> cake(R);
        for(int i=0;i<R;++i){
            cin >> row;
            cake[i]=row;
        }


        for(int i=0;i<R;++i){
            for(int j=0;j<C;++j){
                    if(cake[i][j]!='?'){
                        pred=cake[i][j];
                    }else if(pred!=0){
                        cake[i][j]=pred;
                    }

            }
            pred=0;
        }

        for(int i=0;i<R;++i){
            for(int j=C-1;j>=0;--j){
                    if(cake[i][j]!='?'){
                        pred=cake[i][j];
                    }else if(pred!=0){
                        cake[i][j]=pred;
                    }

            }
            pred=0;
        }

        for(int i=1;i<R;++i){
            for(int j=0;j<C;++j){
                    if(cake[i][j]=='?'){
                        cake[i][j]=cake[i-1][j];
                    }
            }
        }

        for(int i=R-2;i>=0;--i){
            for(int j=0;j<C;++j){
                    if(cake[i][j]=='?'){
                        cake[i][j]=cake[i+1][j];
                    }
            }
        }

        cout <<"Case #"<<e<<":\n";
        for(int i=0;i<R;++i){
                for(int j=0;j<C;++j){
                    cout << cake[i][j];
                }
                cout<<"\n";
        }


    }

    return 0;
}




