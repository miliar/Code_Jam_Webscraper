//
//  main.cpp
//  A
//
//  Created by Yuto Murashita on 15/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define INF ((int)1e9)

using namespace std;

char cake[25][25];
int R, C;
typedef pair<int,int> P;
bool used[25][25];

void read(void){
    cin >> R >> C;
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++)
            cin >> cake[r][c];
    }
}

int find_right_limit(int r, int c, char ini){
    for(int d=c+1; d<C; d++){
        if(cake[r][d]=='?'){
            cake[r][d]=ini;
            used[r][d]=true;
        }
        else return d-1;
    }
    return C-1;
}

int find_left_limit(int r, int c, char ini){
    for(int d=c-1; d>=0; d--){
        if(cake[r][d]=='?'){
            cake[r][d]=ini;
            used[r][d]=true;
        }
        else return d+1;
    }
    return 0;
}

void fill_to_up(int r, int c, int ll, int rl, char ini){
    for(int s=r-1; s>=0; s--){
        for(int d=ll; d<= rl; d++){
            if(cake[s][d]!='?') return;
        }
        for(int d=ll; d<=rl; d++){
            cake[s][d]=ini;
            used[s][d]=true;
        }
    }
}

void fill_to_down(int r, int c, int ll, int rl, char ini){
    for(int s=r+1; s<R; s++){
        for(int d=ll; d<= rl; d++){
            if(cake[s][d]!='?') return;
        }
        for(int d=ll; d<=rl; d++){
            cake[s][d]=ini;
            used[s][d]=true;
        }
    }
}

void solve(void){
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            used[r][c]=false;
        }
    }
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            char ini = cake[r][c];
            if(ini=='?') continue;
            if(used[r][c]) continue;
            int rl, ll;
            rl = find_right_limit(r, c, ini);
            ll = find_left_limit(r, c, ini);
            //cout << r << " " << c << " " << rl << " " << ll << endl;
            fill_to_up(r, c, ll, rl, ini);
            fill_to_down(r, c, ll, rl, ini);
            used[r][c]=true;
        }
    }
    for(int r=0; r<R; r++){
        for(int c=0; c<C; c++){
            cout << cake[r][c];
        }
        cout << endl;
    }
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;

    for(int t=1; t<=T; t++){
    	cout << "Case #" << t << ":" << endl;
    	read();
    	solve();	
    }

    return 0;
}
