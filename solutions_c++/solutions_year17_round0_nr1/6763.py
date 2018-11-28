#include <iostream>
#include <string>
#define mas '+'
#define men '-'

using namespace std;

inline bool isMin(string cad){
    for (char a: cad)
        if (a == men) return true;
    return false;
}

inline void solveA(){
    int num_cases, num, aux, result;
    string c, cp;
    bool flag;
    cin >> num_cases;
    for (int i = 1; i <= num_cases; i++){
        result = 0;
        flag = false;
        cin >> c >> num;
        aux = c.size();
        if(num > aux){
            if(isMin(c)) {
                flag = true;
            }
        }else{
            for (int j = 0; j < aux; j++){
                if(c[j] == men ){
                   // cout << c << endl;
                    if((j+num) > c.length()){
                        flag = true;
                        break;
                    }
                    for (int k = j; k < j+ num ; k++){
                        c[k] = c[k]==mas? men: mas;
                    }
                    result ++;
                }
            }
        }
        if(!flag){
            cout << "Case #"<< i << ": "<< result << "\n";
        }else{
            cout << "Case #"<< i << ": IMPOSSIBLE" << "\n";
        }
        
    }
}


int main(){
    solveA();
    return 0;
}
