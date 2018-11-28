//
//  main.cpp
//  R1Q2
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
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": ";
        int N,P;
        cin>>N>>P;
        vi ref(N);
        for(int i=0;i<N;++i) cin>>ref[i];
        vector<vector<ii>> G(N,vector<ii>(P));
        for(int i=0;i<N;++i) for(int j=0;j<P;++j) {
            int l = 0, r = 0, g;
            cin >> g;
            r = (10*g)/(9*ref[i]);
            if((10*g)%(11*ref[i])==0) l = (10*g)/(11*ref[i]);
            else l = (10*g)/(11*ref[i])+1;
            G[i][j] = ii(l,r);
        }
        int ans = 0;
        if(N==1){
            for(int i=0;i<P;++i) if(G[0][i].first <= G[0][i].second) ans++;
            cout<<ans<<endl;
            cerr<<ans<<endl;
            continue;
        }
        vi ind(P);
        for(int i=0;i<P;++i) ind[i] = i;
        do{
            int tmp = 0;
            for(int i=0;i<P;++i){
                if(max(G[0][i].first,G[1][ind[i]].first) <= min(G[0][i].second,G[1][ind[i]].second)) tmp++;
            }
            ans = max(ans,tmp);
        }while(next_permutation(ind.begin(),ind.end()));
        cout<<ans<<endl;
        cerr<<ans<<endl;
    }
    return 0;
}
