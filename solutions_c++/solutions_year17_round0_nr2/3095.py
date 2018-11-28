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

LL comb(LL r,LL n){
    LL ans = 1;
    for(LL k=n,i=2;k>n-r;--k){
        ans *= k;
        while(ans%i==0 && i<=r){
            ans /= i;
            ++i;
        }
    }
    return ans;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("B-large.in","r",stdin);
    freopen("output_large","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        string N;
        cin>>N;
        cout<<"Case #"<<t<<": ";
        N = N.substr(N.find_first_not_of("0"));
        int i = 0;
        while(i<N.size()-1){
            if(N[i]>N[i+1]) break;
            ++i;
        }
        if(i==N.size()-1){
            cout<<N<<endl;
            continue;
        }
        while(i>0 && N[i]==N[i-1]) --i;
        string ans = N.substr(0,i);
        ans += char(N[i]-1);
        ans += string(N.size()-i-1,'9');
        ans = ans.substr(ans.find_first_not_of("0"));
        cout<<ans<<endl;
    }
    return 0;
}
