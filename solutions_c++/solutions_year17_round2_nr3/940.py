//
//  2017_A.cpp
//  GCJ
//
//  Created by 陶源 on 4/8/17.
//  Copyright © 2017 daisynowhere. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

ifstream in("/Users/daisy/Documents/GCJ/GCJinput/C-large.in");
ofstream out("/Users/daisy/Documents/GCJ/GCJoutput/CL.out");

void solveQA(int number){
    string S;
    int i, K, times = 0;
    bool can = true;
    in >> S >> K;
    for (i = 0; i <= S.length() - K; i ++) {
        if (S[i]=='+') {
            continue;
        }
        else{
            for (int j = 0; j < K; j ++) {
                S[i+j] = (S[i+j]=='+')?'-':'+';
            }
            times ++;
        }
    }
    for (i = int(S.length()) - K; i < S.length(); i ++) {
        if(S[i]=='-'){
            can = false;
            break;
        }
    }
    out << "Case #" << number << ": ";
    if(can)
        out << times<< endl;
    else
        out << "IMPOSSIBLE" << endl;
}

void solveQB(int number){
    string N;
    in >> N;
    int i, RB = -1, RL = -1;
    for (i = 0; i < N.length()-1; i ++) {
        if (N[i] < N[i+1]) {
            RB = i;
        }
        else if(N[i] > N[i+1]){
            RL = i;
            break;
        }
    }
    out << "Case #" << number << ": ";
    if (N.length() == 1){
        out << N << endl;
        return;
    }
    if (RL < 0){
        out << N << endl;
        return;
    }
    if (RB >= 0) {
        for (i = 0; i <= RB; i ++) {
            out << N[i];
        }
        out << char(N[RB+1]-1);
        for (i = RB+2; i < N.length(); i ++) {
            out << '9';
        }
        out << endl;
        return;
    }
    if (N[0]!='1') {
        out << char(N[0]-1);
    }
    for (i = 1; i < N.length(); i ++) {
        out << '9';
    }
    out << endl;
    return;
    
}
void solveQC(int number){
    long long N, K, i=1, L, R, min=1, max=0;
    in >> N >> K;
    long long blank = N;
    while (i < K) {
        if(blank%2){
            min = min*2+max;
        }
        else{
            max = min+max*2;
        }
        blank = (blank-1)/2;
        i = i*2+1;
    }
    i = (i-1)/2;
    K -= i;
    if (K <= max) {
        blank += 1;
    }
    L = blank/2;
    R = L;
    if(blank%2==0)
        R = L-1;
    out << "Case #" << number << ": "<< L << " " << R << endl;
    
}
void solveBA(int number){
    out << "Case #" << number << ": ";
    long long D;
    int N;
    double T = 0, time;
    in >> D >> N;
    long long K[1000], S[1000];
    for(int i = 0; i < N; i ++){
        in >> K[i] >> S[i];
    }
    for (int i = 0; i < N; i ++) {
        T = T > (D-K[i])*1.0/S[i] ? T:(D-K[i])*1.0/S[i];
    }
    time = 1.0*D/T;
    out << fixed << setprecision(6)<<time << endl;
    
}

void solveBC(int number){
    out << "Case #" << number << ": ";
    int N, Q, U, V;
    in >> N >> Q;
    long long E[100], S[100];
    long long D[100][100];
    double time[100][100];
    for (int i = 0; i < N; i ++) {
        in >> E[i] >> S[i];
    }
    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < N; j ++) {
            in >> D[i][j];
        }
    }
    for (int t = 0; t < N; t ++) {
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N; j ++){
                if(((D[i][t]+D[t][j]<D[i][j])|| D[i][j]==-1) &&D[i][t] != -1 &&D[t][j] != -1)
                    D[i][j] = D[i][t] + D[t][j];
            }
        }
    }
    for (int i = 0; i < N; i ++) {
        for (int j = 0; j < N; j ++) {
            if (E[i] >= D[i][j]&&D[i][j]!=-1) {
                time[i][j] = 1.0*D[i][j]/S[i];
            }
            else{
                time[i][j] = -1;
            }
        }
    }
    for (int t = 0; t < N; t ++) {
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N; j ++){
                if(((time[i][t]+time[t][j]<time[i][j])|| time[i][j]==-1) &&time[i][t] != -1 &&time[t][j] != -1)
                    time[i][j] = time[i][t] + time[t][j];
            }
        }
    }
    for (int i = 0; i < Q; i ++) {
        in >> U >> V;
        out << fixed << setprecision(6) << time[U-1][V-1] <<" ";
    }
    out << endl;
}
void solveAC(int number){
    out << "Case #" << number << ": ";
    int Hd, Ad, Hk, Ak, B, D, C, times;
    int Tk, Tpk;
    in >> Hd >> Ad >> Hk >> Ak >> B >> D;
    C = Hd;
    if (Ad >= Hk) {
        out << 1 << endl;
        return;
    }
    if (Ak >= Hd/2.0+D && Ad+B < Hk && 2*Ad < Hk) {
        out << "IMPOSSIBLE" << endl;
        return;
    }
    if (Ak >= Hd ) {
        out << "IMPOSSIBLE" << endl;
        return;
    }
    times = 0;
    while (Hk > 0) {
        times += 1;
        if (Hk <= Ad) {
            Hk -= Ad;
            //out << "Attack" << endl;
            break;
        }
        if (Hd <= Ak) {
            Hd = C;
            //out << "Cure" << endl;
            continue;
        }
        if (Ak != 0) {
            Tk = int((Hd-1)/Ak);
            if (Ak > D) {
                Tpk = int((Hd-1)/(Ak-D));
                if (int(Hk/(Tk*Ad))*(Tk+1)>1+int(Hk/(Tpk*Ad))*(Tpk+1)) {
                    Ak -= D;
                    //out << "Debuff" << endl;
                    continue;
                }
            }
            else if(int(Hk/(Tk*Ad))*(Tk+1)>1+int(Hk/Ad)) {
                Ak = 0;
                //out << "Debuff" << endl;
                continue;
            }
        }
        if((int((Hk+Ad-1)/Ad)) > int((Hk+Ad+B-1)/(Ad+B))+1){
            Ad += B;
            //out << "Buff" << endl;
        }
        else{
            Hk -= Ad;
            //out << "Attack"<< endl;
        }
        Hd -= Ak;
        
    }
    out << times << endl;
    
}

int main(){
    int T, t;
    in >> T;
    for (t = 1; t <= T; t ++) {
        solveBC(t);
    }
    in.close();
    out.close();
    return 0;
}