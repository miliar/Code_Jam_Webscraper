/*
 Round 1C - Question 3:
 @author: Christopher W. Frost
 */

#include<iostream>
#include<vector>
//#include<string>
#include<cmath>
//#include<algorithm>
#include<iomanip>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        
        int N, K;
        double U;
        double P = 0.0;
        cin >> N >> K;
        cin >> U;
        
        vector<double> values;
        for(int j = 0; j < N; j++){
            cin >> P;
            values.push_back(P);
        }
        //Bubble sort to find K smallest P values
        for(int k = 0; k < K; k++){
            for(int l = N-1; l >= 1; l--){
                if(values[l] < values[l-1]){
                    double temp = values[l-1];
                    values[l-1] = values[l];
                    values[l] = temp;
                }
            }
        }
        
        double minValue = values[0];
        int count = 1;
        
        
        
        for(int k = 0; k < K-1; k++){
            if(((k+1)*(values[k+1]-values[k])) <= U){
                U -= ((k+1)*(values[k+1]-values[k]));
                minValue = values[k+1];
                count++;
            }
            else{
                break;
            }
        }
        if(U != 0)
            minValue += U/count;
        
        double answer;
        if(N == K){
            //small dataset 1
            answer = pow(minValue, count);
            K -= count;
            while(K > 0){
                answer*=values[count];
                count++;
                K--;
            }
        }
        else{
            //small dataset 2
            
        }
        cout << setprecision(6) << fixed << answer << '\n';
        
        
    }
}
