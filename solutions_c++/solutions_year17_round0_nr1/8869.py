#include <iostream>
#include <string.h>
using namespace std;

 
string test(char  in[], int k){
    int count = 0;
    for(int i=0; i<= strlen(in) - k; i++){
        if(in[i] == '+' ){
            continue;
        }
        if(in[i] == '-') {
            in[i] = '+';
            for(int p=i+1; p<k+i; p++){
                if(in[p] == '-'){
                    in[p] = '+';
                    continue;
                }

                if(in[p] == '+'){
                    in[p] = '-';
                    continue;
                }

            }
            count++;
        }
    }

    for(int j= strlen(in)-k ; j < strlen(in) ; j++){
       if( '-' == in[j]){

           return "IMPOSSIBLE";
       }
    }    

    return std::to_string(count);

}
 
int main() {
  


  long t, k;
  cin >> t;
  string str;
  for (int i = 1; i <= t; ++i) {
    
    cin >> str >> k ;  
    cout << "Case #" << i << ": " << test(&str[0u],k) <<  endl;
  }
  return 0;
}
