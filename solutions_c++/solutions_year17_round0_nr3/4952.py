//
//  main.cpp
//
//
//  Created by Zain Sheikh on 08/04/2017.
//  Copyright © 2017 Zain sheikh. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <deque>
#include <math.h>
using namespace std;
#define ll long long

int main(int argc, const char * argv[]) {
    ll cno=0;
    ll tt;
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    fin>>tt;
    while(tt--) {
        cno++;
        ll n,p;
        fin>>n>>p;
        ll min,max;
        while (p!=0) {
            n--;
            if (p==1) {
                min=n/2;
                max=n-min;
                break;
            }
            else if(p%2==0){
                ll t=n/2;
                n=n-t;
                p/=2;
            }
            else{
                n/=2;
                p/=2;
            }
        }
        fout<<"Case #"<<cno<<": "<<max<<' '<<min<<endl;
    }
    
    return 0;
}
