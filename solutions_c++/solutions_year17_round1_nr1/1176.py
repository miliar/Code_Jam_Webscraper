//
//  main.cpp
//  R1Q1
//
//  Created by Zebo Li on 4/14/17.
//  Copyright © 2017 Zebo Li. All rights reserved.
//

#include<string>
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<numeric>
#include<deque>
#include<set>
#include<functional>
#include<queue>
#include<stack>
#include<unordered_set>
#include<unordered_map>


#define REP(i,s,n) for(int (i)=s; (i)<(int)(n);(i)++)
#define RIT(it,c) for(__typeof(c.begin()) it = c.begin();it!=c.end();it++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) (int)(x).size()
#define MSET(m,v) memset(m,v,sizeof(m))

using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<LL> vL;
typedef vector<bool> vb;
typedef unordered_set<int> ui;
typedef pair<LL,LL> pLL;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output_large","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": "<<endl;
        cerr<<"Case #"<<t<<": "<<endl;
        int R,C;
        cin>>R>>C;
        vector<string> B(R);
        for(int i=0;i<R;++i) cin>>B[i];
        map<int, map<int,char>> col;
        for(int i=0;i<R;++i){
            bool ok = true;
            for(int j=0;j<C && ok;++j) if(B[i][j] != '?') ok = false;
            if(!ok) col[i] = map<int,char>();
            for(int j=0;j<C;++j) if(B[i][j] != '?') col[i][j] = B[i][j];
        }
        int lvl = 0;
        for(auto p:col){
            int tar = p.first,start = 0;
            auto mp = p.second;
            for(auto pr:mp){
                for(int i=lvl;i<=tar;++i) for(int j=start;j<=pr.first;++j) B[i][j] = pr.second;
                start = pr.first+1;
            }
            auto pr = *(--mp.end());
            for(int i=lvl;i<=tar;++i) for(int j=pr.first;j<C;++j) B[i][j] = pr.second;
            lvl = tar+1;
        }
        auto p = *(--col.end());
        auto mp = p.second;
        int start = 0;
        for(auto pr:mp){
            for(int i=p.first;i<R;++i) for(int j=start;j<=pr.first;++j) B[i][j] = pr.second;
            start = pr.first+1;
        }
        auto pr = *(--mp.end());
        for(int i=lvl;i<R;++i) for(int j=pr.first;j<C;++j) B[i][j] = pr.second;
        for(auto s:B) cout<<s<<endl;
        for(auto s:B) cerr<<s<<endl;
        
    }
    return 0;
}

