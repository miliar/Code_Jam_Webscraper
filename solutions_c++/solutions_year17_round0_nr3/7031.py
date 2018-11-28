#include <iostream>
#include <string>
#include <vector>

using namespace::std;

// 1. compute Ls/Rs for each stall
// 2. compute min(Ls/Rs) for each stall, grab the max from these mins. if there is a tie then:
// 3. compute the max(Ls/Rs) for each stall, grab the max from these maxes. if there is a tie then:
// 4. grab the leftmost stall from the tie

class Stall {
    public:
        bool isOccupied = false;
        int Ls=0;
        int Rs=0;
        int min=0;
        int max=0;
};

pair<int, int> findStallSolution(vector<Stall*> stalls) {
    
    int left=0;
    // calculate Ls for each stall
    for(int i=0;i<stalls.size();i++) {
        auto s = stalls[i];
        if(!s->isOccupied) {
            s->Ls = left;
            left++;
        } else {
            left=0;
        }
    }
    
    int right=0;
    // calculate Rs for each stall
    for(int i=stalls.size()-1;i>=0;i--) {
        auto s = stalls[i];
        if(!s->isOccupied) {
            s->Rs = right;
            right++;
        } else {
            right=0;
        }
    }
    
    // calc min and max for each stall
    for(auto s: stalls) {
        if(!s->isOccupied) {
            s->min = min(s->Ls, s->Rs);
            //cout << "Smin: " << s->min << endl;
            s->max = max(s->Ls, s->Rs); 
            //cout << "Smax: " << s->max << endl;
        }
    }
    
    
    int max = -1, min = -1;
    vector<int> tieIndices;
    // find maxest min
    for(int i=0;i<stalls.size();i++) {
        auto s = stalls[i];
        if(!s->isOccupied) {
            if(s->min > min) {
                tieIndices.clear();
                min = s->min;
                tieIndices.push_back(i);
            } else if (s->min == min) {
                // found a tie
                tieIndices.push_back(i);
            }
        }
    }
    
    
    int finalStallIndex = -1;
    max = -1;
    // calc max of maxes for the tied stalls
    for(auto index: tieIndices) {
        auto s = stalls[index];
        if(s->max > max) {
            finalStallIndex = index;
            max = s->max;
        }
    }
    
    auto stallToBeOccupied = stalls[finalStallIndex];
    stallToBeOccupied->isOccupied = true;
    
    return make_pair(stallToBeOccupied->max,stallToBeOccupied->min);
    
}

int main()
{
    int t, numStalls, people;
    vector<Stall*> stalls;
    vector<pair<int,int>> cases;
    cin >> t;
    for (int i=1; i <= t; i++) {
        cin >> numStalls >> people;
        cases.push_back(make_pair(numStalls, people));
    }
    
    int i=1;
    for(auto p: cases) {
        
        stalls.clear();
        
        auto guardStall = new Stall;
        guardStall->isOccupied = true;
        
        // setup the stall scenario
        stalls.push_back(guardStall);    // zero indicates a person. init with people on either side of line of stalls
        for(int j=0;j<p.first;j++) {
            stalls.push_back(new Stall);
        }
        stalls.push_back(guardStall);
        
        cout << "Case #" << i << ": ";
        
        pair<int, int> results;
        for(int j=1;j<=p.second;j++) {
            results = findStallSolution(stalls);
        }
        cout << results.first << " " << results.second << endl;
        i++;
    }
}