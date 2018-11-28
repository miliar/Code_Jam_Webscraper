#include<iostream>

#define MAX_N 1000

using namespace std;

class Bathroom {
    
private:

    int nPeople;
    int nStalls;
    int nOccupied;
    int stalls[MAX_N + 2];
    
    
public:

    Bathroom(int _nPeople, int _nStalls) {
        nPeople = _nPeople;
        nStalls = _nStalls;
        nOccupied = 0;
        stalls[0] = 1;
        stalls[nStalls + 1] = 1;
        for (int i = 1; i < _nStalls + 1; ++i)
            stalls[i] = 0;
    }
    
    bool isOccupied() {
        return nOccupied == nPeople;
    }
    
    
    // maintains LS and RS after a person comes in;
    void chooseStall(int* LS, int* RS) {
        
        int prevOccupied = 0;
        int i, j;
        for (i = 1; i <= nStalls + 1 && !stalls[i]; ++i);
        int nextOccupied = i;
        // cout << "Before this turn: LS = " << *LS << "  RS = " << *RS << endl; 
        // cout << "prev: " << prevOccupied << "  next: " <<nextOccupied << endl;
        
        int bestPos = 1;
        
        // cout << "scaning all the positions\n";
        for (i = 1; i <= nStalls; ++i) {
            
            // cout << "i = " << i << endl;
            // cout << "prev: " << prevOccupied << "  next: " <<nextOccupied << endl;
            
            if (stalls[i]) {
                prevOccupied = i;
                for (j = i + 1; j <= nStalls + 1 && !stalls[j]; ++j);
                nextOccupied = j;
                continue;
            }
            int LStmp = i - prevOccupied - 1;
            int RStmp = nextOccupied - i - 1;
            // cout << "Now " << LStmp << " " << RStmp << endl;
            
            if (min(LStmp, RStmp) > min(*LS, *RS) || (min(LStmp, RStmp) == min(*LS, *RS) && max(LStmp, RStmp) > max(*LS, *RS))) {
                *LS = LStmp;
                *RS = RStmp;
                bestPos = i;
                // cout << "Best pos changed to " << bestPos << endl;
            }
            // cout << "Updated " << *LS << " " << *RS << endl;
        }
        stalls[bestPos] = 1;
        // cout << "A person entered pos " << bestPos << endl;
        // cout << *LS << " " << *RS << endl;
    }
    
};

int main() {
    int T, N, K;
    cin >> T;
        
    for (int i = 0; i < T; ++i) {
        cin >> N >> K;
        // cout << N << " " << K << endl;
        Bathroom curr(K, N);
        int LS, RS;
        for (int j = 0; j < K; ++j) {
            LS = -1, RS = -1;
            curr.chooseStall(&LS, &RS);
        }
        cout << "Case #" << i + 1 << ": " << max(LS, RS) << " " << min(LS, RS) << endl;
    }
    return 0;
}