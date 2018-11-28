//
//  main.cpp
//  QR#1
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


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output_large","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        int K,i = 0, flip = 0;
        string s;
        cin>>s>>K;
        vb f(s.size());
        for(int i=0;i<s.size();++i) f[i] = (s[i]=='-');
        while(i+K<=s.size()){
            if(f[i]){
                flip++;
                for(int j=i;j<i+K;++j) f[j] = !f[j];
            }
            ++i;
        }
        bool ok = true;
        while(i<s.size() && ok) {
            if(f[i]) ok = false;
            ++i;
        }
        cout<<"Case #"<<t<<": ";
        if(ok) cout<<flip<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}


