//
//  main.cpp
//  BathroomStall
//
//  Created by Anirudh Mendiratta on 4/8/17.
//  Copyright © 2017 anirudh. All rights reserved.
//


/*
 
 A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.
 
 Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.
 
 K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.
 
 When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
 
 */
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdlib.h>     /* abs */

using namespace std;

typedef unsigned long long uint64;

struct Stall
{
    bool isOccupied;
    uint64 ls;
    uint64 rs;
    uint64 index;
};

struct Compare
{
    // Returns true if s1 < s2
    bool operator()(const Stall& s1, const Stall& s2)
    {
        uint64 minlsrs1, minlsrs2;
        uint64 maxlsrs1, maxlsrs2;
        uint64 index1, index2;
        
        minlsrs1 = min(s1.ls, s1.rs);
        minlsrs2 = min(s2.ls, s2.rs);
        
        maxlsrs1 = max(s1.ls, s1.rs);
        maxlsrs2 = max(s2.ls, s2.rs);
        
        index1 = s1.index;
        index2 = s2.index;
        
        if(minlsrs1 == minlsrs2 && maxlsrs1 == maxlsrs2)
        {
            return index1 > index2;
        }
        else if(minlsrs1 == minlsrs2)
        {
            return maxlsrs1 < maxlsrs2;
        }
        
        return minlsrs1 < minlsrs2;
    }
};

void printStalls(vector<Stall> stalls)
{
    for(size_t i=0; i<stalls.size(); i++)
    {
        cout << "ls = " << stalls[i].ls << ", rs = "
        << stalls[i].rs << ", index = " << stalls[i].index;
        if(stalls[i].isOccupied)
        {
            cout << ", Occupied";
        }
        else{
            cout << ", Not Occupied";
        }
        cout << endl;
    }
}


vector<Stall> initializeStalls(uint64 N)
{
    vector<Stall> outVector(N+2);
    outVector[0] = {.isOccupied=true, .ls=0, .rs=N, .index=0};
    for(uint64 i=1; i<N+1; i++)
    {
        outVector[i] = {.isOccupied=false, .ls=i-1, .rs=N-i, .index=i};
    }
    outVector[N+1] = {.isOccupied=true, .ls=N, .rs=0, .index=0};
    return outVector;
}

uint64 findBestStall(const vector<Stall>& stalls)
{
    Stall currentMax = stalls[1];
    for(size_t i=2; i<stalls.size()-1; i++)
    {
        if(currentMax.isOccupied)
        {
            currentMax = stalls[i];
        }
        if(!stalls[i].isOccupied)
        {
            currentMax = max(currentMax, stalls[i], Compare());
            //cout << "Current best stall = " << currentMax.index << endl;
        }
    }
    if(!currentMax.isOccupied)
    {
        return currentMax.index;
    }
    return 0;
}

void updateStalls(vector<Stall>& stalls, uint64 newStallIndex)
{
    stalls[newStallIndex].isOccupied = true;
    for(size_t i=newStallIndex-stalls[newStallIndex].ls-1;
        i<newStallIndex; i++)
    {
        //cout << "Updating stall " << i << " which is occupied = "
        ///<< stalls[i].isOccupied << endl;
        stalls[i].rs = newStallIndex-i-1;
    }
    for(size_t i=newStallIndex+1; i<newStallIndex + stalls[newStallIndex].rs + 1; i++)
    {
        //cout << "Updating stall " << i << " which is occupied = "
        ///<< stalls[i].isOccupied << endl;
        stalls[i].ls = i-newStallIndex-1;
    }
}

vector<Stall> insertAllPeople(uint64 N, uint64 K, uint64* lastStallIndex)
{
    vector<Stall> stalls = initializeStalls(N);
    //printStalls(stalls);
    uint64 bestStall = 0;
    for(size_t i=0; i<K; i++)
    {
        bestStall = findBestStall(stalls);
        // cout << "Person " << i << " goes to stall " << bestStall << endl;
        updateStalls(stalls, bestStall);
        //printStalls(stalls);
    }
    *lastStallIndex = bestStall;
    // printStalls(stalls);
    
    return stalls;
}

void getMinAndMax(const Stall& stall, uint64* minlsrs, uint64* maxlsrs)
{
    *minlsrs = min(stall.ls, stall.rs);
    *maxlsrs = max(stall.ls, stall.rs);
}


int main(int argc, const char * argv[]) {

    size_t numTestCases;
    cin >> numTestCases;
    
    vector<uint64> N(numTestCases);
    vector<uint64> K(numTestCases);
    
    
    for(size_t i=0; i<numTestCases; i++)
    {
        cin >> N[i] >> K[i];
    }
    
    cout << endl << endl;
    for(size_t i=0; i<numTestCases; i++)
    {
        uint64 min, max, lastStallIndex;
        cout << "Case #" << i+1 << ": ";
        
        vector<Stall> stalls = insertAllPeople(N[i], K[i], &lastStallIndex);
        getMinAndMax(stalls[lastStallIndex], &min, &max);
        
        cout << max << " " << min << endl;
    }
    cout << endl << endl;
    
    return 0;
}
