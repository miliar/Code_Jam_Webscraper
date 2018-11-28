#include<iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(auto t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        string state;
        cin >> state;
        int K;
        cin >> K;
        int len = state.size();
        int count_current = 0, count_total = 0, count[1001] {0};
//        cout << "\n" << state << K << len << "\n";
        for( auto i = 0; i < len; i++){
//            cout << count[i] << "\n";
            count_current += count[i];
            if( i <= (len - K) ){
                if(((state[i] == '+') && (count_current%2 != 0)) 
                    || ((state[i] == '-') && (count_current%2 == 0))){
                    count_current++;
                    count_total++;
                    count[i+K] = -1;
                    
                }
            }
            else if( count_total != -1 ){
                if((state[i] == '+') && (count_current%2 != 0))
                    count_total = -1;
                else if((state[i] == '-') && (count_current%2 == 0))
                    count_total = -1;
            }
        }
        if(count_total == -1)
            cout << "IMPOSSIBLE";
        else
            cout << count_total;
        cout <<"\n";  
    }
    return 0;
}
