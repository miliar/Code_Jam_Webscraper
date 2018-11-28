/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 15, 2017, 2:38 AM
 */

#include <cstdlib>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <limits>
typedef std::numeric_limits< double > dbl;
using namespace std;

/*
 * 
 */
struct Pancake { 
    long index;
    long radius;
    long sideArea;
    long topArea;
};

struct by_topArea { 
    bool operator()(Pancake const &a, Pancake const &b) { 
        return a.topArea > b.topArea;
    }
};

struct by_sideArea { 
    bool operator()(Pancake const &a, Pancake const &b) { 
        return a.sideArea > b.sideArea;
    }
};

int main(int argc, char** argv) {
    cout.precision(100);
    long T;
    cin>>T;
    for (long t = 0; t < T; t++) {
        long N;  
        cin>>N;
        long K;
        cin>>K;
        vector<long> radius(N);
        vector<long> heights(N);
        for(long i=0;i<N;i++) {
            cin>>radius[i];
            cin>>heights[i];            
        }
        vector<long> sideAreas(N);
        vector<long> topAreas(N);
        
        vector<Pancake> pancakesBySide;
        vector<Pancake> pancakesByTop;
        vector<Pancake> pancakes;
       
        for(long i=0;i<N;i++) {
            sideAreas[i]= radius[i] * heights[i];
            topAreas[i]= radius[i] * radius[i];
            Pancake p;
            p.topArea = topAreas[i];
            p.sideArea = sideAreas[i];
            p.index = i;
            p.radius = radius[i];
            pancakesBySide.push_back(p);
            pancakesByTop.push_back(p);
            pancakes.push_back(p);
        }
        sort(pancakesByTop.begin(), pancakesByTop.end(), by_topArea());
        sort(pancakesBySide.begin(), pancakesBySide.end(), by_sideArea());
        double bestArea = 0;
        //select starter
        for(long i=0;i<N;i++) {
            long count = 1;
            long topArea = pancakesByTop[i].topArea;
            long sideArea = pancakesByTop[i].sideArea;
            //get best sideArea with good radius
            for(long j=0;j<N && count<K;j++) {
                if(pancakesBySide[j].index!=pancakesByTop[i].index && pancakesBySide[j].radius<=pancakesByTop[i].radius) {
                    sideArea+=pancakesBySide[j].sideArea;
                    count++;
                }
            }
            double total = 2 * M_PI * sideArea+ M_PI * topArea;
            if(total>bestArea) {
                bestArea = total;
            }
        }
        cout << "Case #" << t + 1 << ": "<< bestArea << endl;
    }
    return 0;
}

