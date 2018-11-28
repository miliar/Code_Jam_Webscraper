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
#include <iomanip>


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

const LD pi = 3.1415926535897936;

bool cmp(ii A,ii B){
    return LL(A.first)*A.second < LL(B.first)*B.second;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("output_L","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": ";
        int N,K;
        cin>>N>>K;
        vector<ii> P;
        vector<int> R;
        for(int i=0;i<N;++i){
            int r,h;
            cin>>r>>h;
            P.push_back(ii(r,h));
            R.push_back(r);
        }
        sort(P.begin(),P.end(),cmp);
        reverse(P.begin(),P.end());
        sort(R.begin(),R.end());
        reverse(R.begin(),R.end());
        LL ans = 0;
        for(int i=0;i<N;++i){
            if(i>0 && R[i]==R[i-1]) continue;
            int tmpR = R[i];
            int k = 0, cnt = 1;
            while(k<N && P[k].first!=tmpR) ++k;
            LL tmp = LL(tmpR)*(2*P[k].second + tmpR);
            for(int j=0;j<N && cnt<K;++j){
                if(j!=k && P[j].first<=tmpR){
                    tmp += LL(2)*LL(P[j].first)*P[j].second;
                    ++cnt;
                }
            }
            if(cnt < K) break;
            ans = max(ans,tmp);
        }
        cout << fixed << setprecision(16);
        cout << pi*ans<<endl;
    }
    return 0;
}

