//Diego Uzcategui <diego.uzc@gmail.com>  d-uzc.freehostia.com

#include <iostream>
#include <string.h>
//#include <string> 
#include <sstream>

using namespace std;

int main(){

    int T, N;//entrada
    int j;
    int ordenado;
    cin >> T;
    for(int i=1; i<= T; i++){
        cin >> N;
        for(j=N; j>0; j--){
            string str;          //The string
            ostringstream temp;  //temp as in temporary
            temp<<j;
            str=temp.str();      //str is temp as string
//            cout<<" ** "<< str<<endl;
            char a = str[0];
            ordenado = true;
            for(int k=1; k < str.size(); k++){
                if(a > str[k]){
                    ordenado = false;
                    break;
                }else{
                    a = str[k];
                }
            }
            if(ordenado == true) break;
        }
        
        cout<<"Case #"<<i<<": "<< j <<endl;
    }
    
    return 0;
}