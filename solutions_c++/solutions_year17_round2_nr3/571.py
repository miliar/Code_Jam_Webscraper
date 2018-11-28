//
//  main.cpp
//  roundB
//
//  Created by didi on 2017/4/22.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

ifstream in("/Users/didi/Desktop/roundB/roundB/C-large.in");
ofstream out("/Users/didi/Desktop/roundB/roundB/C-large.out");

long long D[110][110];
long long E[110];
long long S[110];
long long dist[110][110];
double min_time[110][110];

int N, Q;
/*
void get_dist(int x){
    for (int i=0; i<N; i++){
        dist[x][i] = 1e13;
    }
    dist[x][x] = 0;
    for (int i=0; i<N; i++){
        int min = 1e13;
        int id_x = -1;
        int id_y = -1;
        for (int j=0; j<N; j++){
            for (int d=0; d<N; d++){
                if (dist[x][j] + D[j][d] < min){
                    min = dist[x][j] + D[j][d];
                    id_x = j;
                    id_y = d;
                }
            }
        }
    }
}*/

void solve(int test){
    out << "Case #" << test << ": ";
    in >> N >> Q;
    for (int i=0; i<N; i++){
        in >> E[i] >> S[i];
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++) in>>D[i][j];
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            if (i==j) dist[i][i] = 0;
            else dist[i][j] = D[i][j];
        }
    }
    for (int t=0; t<N; t++){
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (dist[i][t] != -1 && dist[t][j] != -1 && (dist[i][t]+dist[t][j]<dist[i][j] || dist[i][j] == -1))
                    dist[i][j] = dist[i][t] + dist[t][j];
            }
        }
    }
    /*
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cout << dist[i][j] << " ";
        }
        cout<< endl;
    }*/
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            if (E[i] >= dist[i][j] && dist[i][j] != -1){
                min_time[i][j] = 1.0*dist[i][j]/S[i];
            }else{
                min_time[i][j] = 1e13;
            }
            //cout << min_time[i][j] << " ";
        }
        //cout << endl;
    }
    for (int t=0; t<N; t++){
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (min_time[i][t] + min_time[t][j] < min_time[i][j])
                    min_time[i][j] = min_time[i][t] + min_time[t][j];
            }
        }
    }
    for (int i=0; i<Q; i++){
        int x, y;
        in >> x >> y;
        out << fixed << setprecision(6) << min_time[x-1][y-1] << " ";
    }
    out << endl;
}


int main(int argc, const char * argv[]) {
    int test = 0,T;
    in >> T;
    while (test++<T){
        solve(test);
    }
    in.close();
    out.close();
    return 0;
}
