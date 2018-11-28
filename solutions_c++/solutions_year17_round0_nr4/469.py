//
//  main.cpp
//  GCJ_QR_D
//
//  Created by Yuto Murashita on 08/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct model{
    char k;
    int r, c;
};

class board{
    vector<pair<int, int> > cross;
    vector<pair<int, int> > plus;
    int N, M;
    vector<model> added_cross, added_plus, added;
public:
    int ini_n_cross, ini_n_plus;
    int n_added_cross, n_added_plus, n_added;
    board(int n, int m){
        N=n; M=m;
        char k;
        int r, c;
        for(int i=0; i<M; i++){
            cin >> k >> r >> c;
            pair<int,int> p;
            p.first = r; p.second = c;
            if(k=='x' || k=='o')
                cross.push_back(p);
            if(k=='+' || k=='o')
                plus.push_back(p);
        }
        ini_n_cross = (int)cross.size();
        ini_n_plus = (int)plus.size();
        n_added_cross = 0;
        n_added_plus = 0;
    }
    bool is_cross(pair<int,int> p){
        for(int n=0; n<(int)cross.size(); n++)
            if(cross[n]==p) return true;
        return false;
    }
    bool is_plus(pair<int,int> p){
        for(int n=0; n<(int)plus.size(); n++)
            if(plus[n]==p) return true;
        return false;
    }
    bool is_cross_in_row(int r){
        pair<int,int> p;
        p.first = r;
        for(p.second=1; p.second<=N; p.second++)
            if(is_cross(p)) return true;
        return false;
    }
    bool is_cross_in_col(int c){
        pair<int,int> p;
        p.second = c;
        for(p.first=1; p.first<=N; p.first++)
            if(is_cross(p)) return true;
        return false;
    }
    int find_no_cross_col(void){
        for(int c=1; c<=N; c++)
            if(!is_cross_in_col(c)) return c;
        exit(1);
    }
    void fill_cross(void){
        model mod;
        pair<int,int> p;
        for(mod.r=1; mod.r<=N; mod.r++){
            if(!is_cross_in_row(mod.r)){
                mod.c = find_no_cross_col();
                p.first=mod.r; p.second=mod.c;
                if(is_plus(p)) mod.k='o';
                else mod.k='x';
                cross.push_back(p);
                added_cross.push_back(mod);
            }
        }
        n_added_cross = (int) added_cross.size();
    }
    bool is_plus_in_sum(int sum){
        pair<int,int> p;
        for(int r=max(1,sum-N); r<=min(sum,N); r++){
            p.first=r; p.second=sum-r;
            if(is_plus(p)) return true;
        }
        return false;
    }
    bool is_plus_in_sub(int sub){
        pair<int,int> p;
        for(int r=max(1,1+sub); r<=min(N,sub+N); r++){
            p.first=r; p.second=r-sub;
            if(is_plus(p)) return true;
        }
        return false;
    }
    int n_ud_plus(void){
        int tmp=0;
        for(int i=0; i<plus.size(); i++)
            if(plus[i].first==1 || plus[i].first==N) tmp += 1;
        return tmp;
    }
    int n_lr_plus(void){
        int tmp=0;
        for(int i=0; i<plus.size(); i++)
            if(plus[i].second==1 || plus[i].second==N) tmp += 1;
        return tmp;
    }
    void add_plus(model mod){
        pair<int,int> p;
        if((!is_plus_in_sum(mod.r+mod.c)) && (!is_plus_in_sub(mod.r-mod.c))){
            p.first=mod.r; p.second=mod.c;
            if(is_cross(p)) mod.k='o';
            else mod.k='+';
            added_plus.push_back(mod);
        }
    }
    void fill_ud_plus(void){
        model mod;
        pair<int,int> p;
        mod.r=1;
        for(mod.c=1; mod.c<=N; mod.c++)
            add_plus(mod);
        mod.r=N;
        for(mod.c=2; mod.c<=N-1; mod.c++)
            add_plus(mod);
    }
    void fill_lr_plus(void){
        model mod;
        pair<int,int> p;
        mod.c=1;
        for(mod.r=1; mod.r<=N; mod.r++)
            add_plus(mod);
        mod.c=N;
        for(mod.r=2; mod.r<=N-1; mod.r++)
            add_plus(mod);
    }
    void fill_plus(void){
        if(n_ud_plus()>=n_lr_plus()) fill_ud_plus();
        else fill_lr_plus();
        n_added_plus = (int)added_plus.size();
    }
    int score(void){
        return ini_n_plus+ini_n_cross+n_added_plus+n_added_cross;
    }
    void combine_added(void){
        added = added_plus;
        for(int i=0; i<n_added_cross; i++){
            bool overlap=false;
            for(int j=0; j<n_added_plus; j++){
                if(added_plus[j].r==added_cross[i].r && added_plus[j].c==added_cross[i].c){
                    overlap = true;
                    added[j].k = 'o';
                    break;
                }
            }
            if(!overlap) added.push_back(added_cross[i]);
        }
        n_added = (int)added.size();
    }
    void print_added(void){
        for(int i=0; i<(int)added.size(); i++)
            cout << added[i].k << " " << added[i].r << " " << added[i].c << endl;
    }
};

int main(int argc, const char * argv[]) {
    int T, N, M;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N >> M;
        board b(N, M);
        b.fill_cross();
        b.fill_plus();
        b.combine_added();
        cout << "Case #" << t << ": " << b.score() << " " << b.n_added << endl;
        b.print_added();
    }
    return 0;
}
