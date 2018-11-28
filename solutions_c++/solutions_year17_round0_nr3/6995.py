//Diego Uzcategui <diego.uzc@gmail.com>  d-uzc.freehostia.com

#include <iostream>
#include <string.h>
//#include <string> 
#include <sstream>

using namespace std;

int main(){

    int T, N, K;//entrada
    int j, k1, k2, libre, libre_max, inicial_max;
    int Ls, Rs;
    string banho;
    
    cin >> T;
    for(int i=1; i<= T; i++){
        cin >> N >> K;
        banho = "";
        for(j=0; j< N; j++){
            banho = banho + "0";
        }
        banho = "1" + banho + "1";
        for(k1=0; k1 < K; k1++){
            libre=0;
            libre_max=0;
            inicial_max=0;
            for(k2=0; k2 < banho.size(); k2++){
                if(banho[k2]=='0'){
                    libre++;
                }else{
                    if(libre > libre_max){
                        libre_max = libre;
                        inicial_max= (k2-(libre_max/2)-1);
//                        cout << " --- pos: "<< inicial_max <<endl;
                        if(libre_max %2 == 0){
                            Ls = libre_max/2;
                            Rs = Ls-1;
                        }else{
                            Ls = (libre_max-1)/2;
                            Rs = Ls;
                        }
                    }
//                    cout <<" ** cant: " << libre<< " "<<Ls<<" "<<Rs<<endl;
                    libre = 0;
                }
            }
            banho[inicial_max] = '1';
//            cout<<"---#"<<i<<": "<< banho << " "<<Ls<<" "<<Rs<<endl;
        }
//        cout<<"Case #"<<i<<": "<< banho << " "<<Ls<<" "<<Rs<<endl;
        cout<<"Case #"<<i<<": "<< " "<<Ls<<" "<<Rs<<endl;
    }
    
    return 0;
}