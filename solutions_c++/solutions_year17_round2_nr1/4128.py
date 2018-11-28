#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

struct Horse {
    int K;
    int S;
    Horse(int K, int S):K(K),S(S) {
    }
    bool operator < (const Horse& horse) const {
        return K < horse.K;
    }
};

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int N;
    cin>>N;
    for (int aa=0;aa<N;aa++) {
        int D;
        int N;
        cin>>D;
        cin>>N;
        double t = 0;
        vector<Horse> horses;
        for (int i=0;i<N;i++) {
            int K;
            int S;
            cin>>K;
            cin>>S;
            horses.push_back(Horse(K,S));
        }
        horses.push_back(Horse(D,0));
        sort(horses.begin(), horses.end());
        double currSpeed = horses[0].S;
        double distanceTravelled = horses[0].K;
        for (int i=0;i<horses.size()-1 && distanceTravelled < D;i++) {
            if (currSpeed > horses[i+1].S) {
                double d;
                if (horses[i+1].S == 0) {
                   d = 0;
                } else {
                   d = (horses[i+1].K - distanceTravelled)/((double(currSpeed)/horses[i+1].S)-1);
                }
                if ((d + horses[i+1].K) >= D) {
                    // pass destination before intersecting
                    t += (D - distanceTravelled)/currSpeed;
                    break;
                } else {
                    t += (d+horses[i+1].K-distanceTravelled)/currSpeed;
                    distanceTravelled=d+horses[i+1].K;
                }
                currSpeed = horses[i+1].S;
                //cout<<distanceTravelled<<" "<<t<<endl;
            } else {
                horses.erase(horses.begin()+i);
                i--;
                continue;
            } 
        }
        printf("Case #%d: %.7f\n", aa+1, D/double(t));
    }
    fclose(stdin);
    fclose(stdout);
}
