//
//  main.cpp
//  Problem-C_Bathroom Stalls
//
//  Created by Akram AbdAlAziz on 4/8/17.
//  Copyright © 2017 Akram AbdAlAziz. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct Position {
    unsigned long long pos;
    unsigned long long Ls;
    unsigned long long Rs;
    unsigned long long max;
    unsigned long long min;
    bool occupied;
} stallInfo;

inline unsigned long long max(unsigned long long Ls, unsigned long long Rs);
inline unsigned long long min(unsigned long long Ls, unsigned long long Rs);

int main() {
    // insert code here...
    string line;
    unsigned long long noOfStalls, people, lastStallMax, lastStallMin;
    vector<stallInfo> stalls, maxMinStalls, maxMaxStalls;
    
    int caseN = 1;
    
    ifstream in("input.in");
    ofstream out("output.out");
    
    getline(in, line);
    cout << "trials = " << line << endl;
    
    int i = stoi(line);
    for (; i > 0 ; i--)
    {
        stallInfo stall, occupiedStall;
        
        stalls.clear();
        
        getline(in, line, ' ');
        noOfStalls = stoll(line);
        
        getline(in, line);
        people = stoll(line);
        
        cout << noOfStalls << ' ' << people << "    ";
        
        unsigned long long ls = 0, rs = noOfStalls - 1;
    
        stall.pos = 0;
        stall.Ls = 0;
        stall.Rs = 0;
        stall.max = 0;
        stall.min = 0;
        stall.occupied = true;
        stalls.push_back(stall);
        
        for (int j = 1; j <= noOfStalls ; j++) {
            stall.pos = j;
            stall.Ls = ls;
            stall.Rs = rs;
            stall.max = max(ls,rs);
            stall.min = min(ls,rs);
            stall.occupied = false;
            stalls.push_back(stall);
            ls++;
            rs--;
        }
        
        stall.pos = noOfStalls + 1;
        stall.Ls = 0;
        stall.Rs = 0;
        stall.max = 0;
        stall.min = 0;
        stall.occupied = true;
        stalls.push_back(stall);
        
        while (1)
        {
            maxMaxStalls.clear();
            maxMinStalls.clear();
            
            // get max of min(ls,rs) vector
            for (int j = 0; j < (noOfStalls + 2); j++) {
                if ( !stalls[j].occupied ) {
                    if ( maxMinStalls.empty() )
                        maxMinStalls.push_back(stalls[j]);
                    else if ( maxMinStalls[0].min < stalls[j].min )
                    {
                        maxMinStalls.clear();
                        maxMinStalls.push_back(stalls[j]);
                    }
                    else if ( maxMinStalls[0].min == stalls[j].min )
                        maxMinStalls.push_back(stalls[j]);
                }
            }
            
            // if maxVector size > 1 -> get max of max(ls, rs) vector
            if ( maxMinStalls.size() > 1 ) {
                for (int j = 0; j < maxMinStalls.size(); j++) {
                    if ( maxMaxStalls.empty() )
                        maxMaxStalls.push_back(maxMinStalls[j]);
                    else if ( maxMaxStalls[0].max < maxMinStalls[j].max )
                    {
                        maxMaxStalls.clear();
                        maxMaxStalls.push_back(maxMinStalls[j]);
                    }
                    else if ( maxMaxStalls[0].max == maxMinStalls[j].max )
                        maxMaxStalls.push_back(maxMinStalls[j]);
                }
                // if maxVector size > 1 -> occupied stall will be the leftmost
                // else make this stall as occupied and recalculate the ls and rs for each stall
                occupiedStall = maxMaxStalls[0];
            }
            // else make this stall as occupied and recalculate the ls and rs for each stall
            else
                occupiedStall = maxMinStalls[0];
            
            // set lastStallMax and lastStallMin
            
            stalls[occupiedStall.pos].occupied = true;

            lastStallMax = occupiedStall.max;
            lastStallMin = occupiedStall.min;
            
            stalls[occupiedStall.pos].min = 0;
            stalls[occupiedStall.pos].max = 0;
            
            int j = 1;
            while(!stalls[occupiedStall.pos + j].occupied) {
                stalls[occupiedStall.pos + j].Ls -= (occupiedStall.Ls + 1);
                stalls[occupiedStall.pos + j].max = max(stalls[occupiedStall.pos + j].Ls, stalls[occupiedStall.pos + j].Rs);
                stalls[occupiedStall.pos + j].min = min(stalls[occupiedStall.pos + j].Ls, stalls[occupiedStall.pos + j].Rs);
;
                j++;
            }
            j = 1;
            while(!stalls[occupiedStall.pos - j].occupied) {
                stalls[occupiedStall.pos - j].Rs -= (occupiedStall.Rs + 1);
                stalls[occupiedStall.pos - j].max = max(stalls[occupiedStall.pos - j].Ls, stalls[occupiedStall.pos - j].Rs);
                stalls[occupiedStall.pos - j].min = min(stalls[occupiedStall.pos - j].Ls, stalls[occupiedStall.pos - j].Rs);
                j++;
            }
            
            people--;
            
            if(people == 0)
                break;
        }
        
        cout << "Case #" << caseN << ": " << lastStallMax << " " << lastStallMin << endl;
        out << "Case #"<< caseN <<": " << lastStallMax << " " << lastStallMin << endl;
        
        caseN++;
    }
    
    in.close();
    out.close();
    return 0;
}


inline unsigned long long max(unsigned long long Ls, unsigned long long Rs)
{
    unsigned long long diff = (Ls > Rs)? (Ls - Rs) : (Rs - Ls) ;
    return ( 0.5 * ( Ls + Rs + diff ) );
}
inline unsigned long long min(unsigned long long Ls, unsigned long long Rs)
{
    unsigned long long diff = (Ls > Rs)? (Ls - Rs) : (Rs - Ls) ;
    return ( 0.5 * ( Ls + Rs - diff ) );
}

