#include <iostream>

using namespace std;


int main(){
    
   
    int T;
    cin >> T;

    for(int i=0; i<T; i++){
        string N;
        cin >> N;
        bool first = true;
        bool second = false;
        //cout << N << "\t";
        for(int j=0; j<N.length()-1; j++){
            if(N[j] > N[j+1]){
      
                if (first) {
                    if(N[j] != 0){
                        N[j]--;
                    }
                    int x = 1;
                    while(N[j-x] > N[j-x+1]){
       
                        if(j-x <0)
                            break;
                        N[j-x]--;
                        N[j-x+1] = char(9+'0');
                        x++;
                        second = true;
                    }
                    first=false;
                }
                N[j+1] = char(9+'0');
            }
        }
        N.erase(0, min(N.find_first_not_of('0'), N.size()-1));
        cout << "Case #"<<i+1 << ": " << N << endl;
    }


}
