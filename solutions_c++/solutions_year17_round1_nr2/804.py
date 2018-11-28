//
//  main.cpp
//  B
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

int N, P;
int R[50];
int Q[50][50];
int used[50];

void read(void){
    cin >> N >> P;
    for(int n=0; n<N; n++)
        cin >> R[n];
    for(int n=0; n<N; n++){
        for(int p=0; p<P; p++){
            cin >> Q[n][p];
        }
    }
}

int min_pn(int Q, int R){
    int res = (int)Q/(1.1*R) -1;
    while(res*R*1.1<Q) res++;
    return res;
}

int max_pn(int Q, int R){
    int res = (int)Q/(0.9*R) +1;
    while(res*R*0.9>Q) res--;
    return res;
}

/*
bool find(int *min, int *max, int n){
    for(int p=used[n]+1; p<=P; p++){
        int tmp_min, tmp_max;
        tmp_min = min_pn(Q[n][p], R[n]);
        tmp_max = max_pn(Q[n][p], R[n]);
        if(*min < tmp_min) *min = tmp_min;
    }
    return false;
}
 */

bool dfs(int min, int max, int n){
    for(int p=used[n]+1; p<P; p++){
        int tmp_min, tmp_max;
        tmp_min = min_pn(Q[n][p], R[n]);
        tmp_max = max_pn(Q[n][p], R[n]);
        if(tmp_min>max || tmp_max<min) continue;
        if(min > tmp_min) tmp_min = min;
        else if(max > tmp_max) tmp_max = max;
        if(tmp_min>tmp_max) continue;
        if(n==N-1){
            used[n] = p;
            return true;
        }
        if(dfs(tmp_min, tmp_max, n+1)){
            used[n] = p;
            return true;
        }
    }
    return false;
}


void solve(void){
    memset(used, -1, sizeof(used));
    for(int n=0; n<N; n++){
        sort(Q[n], Q[n]+P);
    }
    
    int num_p=0;
    for(int p=0; p<P; p++){
        int min, max;
        min = min_pn(Q[0][p], R[0]);
        //cout << min << " ";
        max = max_pn(Q[0][p], R[0]);
        //cout << max << endl;
        if(min>max) continue;
    
        bool flag=dfs(min, max, 1);
        if(N==1) flag=true;
        if(flag) num_p++;
    }
    cout << num_p << endl;
    
    /*
    for(int n=0; n<N; n++){
        for(int p=0; p<P; p++){
            cout << Q[n][p] << " ";
        }
        cout << endl;
    }
    */
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;

    for(int t=1; t<=T; t++){
    	cout << "Case #" << t << ": ";
    	read();
    	solve();	
    }

    return 0;
}
