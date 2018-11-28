/*
    Round 1B - Question 1: Steed 2: Cruise Control
    @author: Christopher W. Frost
*/

#include<iostream>
//#include<vector>
//#include<string>
//#include<cmath>
//#include<algorithm>
#include<iomanip>
using namespace std;

class Horse{
private:
    double K, S, D;
    double destTime; //Time to destination
public:
    Horse(double k, double s, double d) : K(k), S(s), D(d) {
        destTime = calcDestTime();
    }
    double calcDestTime(){
        return (D-K)/S;
    }
    double getDestTime(){
        return destTime;
    }
    
};

int main(){
    int T;
    int N;
    double D, K, S;
    cin >> T;
    
    
    
    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        
        double speed;
        double slowest = 0;
        
        cin >> D >> N;
        for(int j = 0; j < N; j++){
            cin >> K >> S;
            Horse temp(K, S, D);
            if(temp.getDestTime() > slowest)
                slowest = temp.getDestTime();
        }
        speed = D / slowest;
        cout << setprecision(6) << fixed << speed << '\n';
    }
}
