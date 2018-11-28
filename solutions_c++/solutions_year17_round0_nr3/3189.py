//
//  main.cpp
//  QR#3
//
//  Created by Zebo Li on 4/7/17.
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

/*
struct pt{
    long long start;
    long long length;
    friend bool operator< (const pt&p1, const pt &p2) {
        if(p1.length != p2.length) return p1.length<p2.length;
        return p1.start>p2.start;
    }
};

pLL addPeople(priority_queue<pt> &que){
    auto p = que.top();
    que.pop();
    LL n = p.length, i = p.start;
    LL l = (n-1)/2, r = n/2;
    if(l) que.push(pt{i,l});
    if(r) que.push(pt{i+l+1,r});
    return pLL(r,l);
}*/


pLL addPeople(map<LL,LL,greater<LL>> &cnt, LL &K){
    LL n = cnt.begin()->first, ct = cnt.begin()->second;
    cnt.erase(cnt.begin());
    cnt[(n-1)/2] += ct;
    cnt[n/2] += ct;
    K -= ct;
    return pLL(n/2,(n-1)/2);
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("C-large.in","r",stdin);
    freopen("output_large","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        LL N,K;
        cin>>N>>K;
        map<LL,LL,greater<LL>> cnt;
        cout<<"Case #"<<t<<": ";
        cerr<<"Case #"<<t<<": ";
        pLL ans;
        cnt[N] = 1;
        while(K>0){
            ans = addPeople(cnt,K);
        }
        cout<<ans.first<<' '<<ans.second<<endl;
        cerr<<ans.first<<' '<<ans.second<<endl;
    }

    return 0;
}
