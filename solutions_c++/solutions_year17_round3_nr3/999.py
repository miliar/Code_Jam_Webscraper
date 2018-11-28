#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

#define EPS 1E-10

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int N; //Cores
        int K; //To Succeed
        cin >> N >> K;
        double U; //Training units
        cin >> U;
        vector<double> P(N); //Probabilities
        for(double &p : P)
            cin >> p;

        //Sort from highest to lowest
        sort(P.begin(), P.end(), greater<double>());
        //Take only the highest K
        P.resize(K);

        //Increase the lowest values up the the next lowest
        int num_low = 0;
        double lowest = P.back();

        while(U > EPS && P.size() > 0) {
            //Find the lowest values
            while(P.size() > 0 && P.back() - lowest < EPS) {
                num_low++;
                P.pop_back();
            }
            //cerr << "lowest=" << lowest << ", num=" << num_low;
            //Increase all the lowest values up to the next lowest
            double new_lowest = P.size() > 0 ? P.back() : 1.0;
            //cerr << ", nextl=" << new_lowest;
            //Have to limit the increase to evenly distributing all the units
            new_lowest = min(new_lowest, lowest + U / num_low);
            //cerr << ", capped;=" << new_lowest;
            //Remove the training units consumed
            U = U - (new_lowest - lowest) * num_low;
            //cerr << ", delta=" << new_lowest - lowest;
            //cerr << ", uused=" << (new_lowest - lowest) * num_low;
            //cerr << ", U=" << U;

            lowest = new_lowest;
            //cerr << endl;
        }

        double success = 1.0; //Chance that no cores fail
        //Small case, all core have to succeed
        //No cores failing
        //Lowest chance
        success = success * pow(lowest, num_low);
        //Remaining cores
        while(P.size() > 0) {
            double core = P.back();
            P.pop_back();
            success = success * core;
        }

        cout << "Case #" << (t + 1) << ": ";
        cout << success;
        cout << endl;
    }
}
