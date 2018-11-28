#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <iomanip>
#include <deque>
#include <stdio.h>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define UNIQUE(Itr) sort((Itr).begin(),(Itr).end()); (Itr).erase(unique((Itr).begin(),(Itr).end()),(Itr).end())
#define LBOUND(Itr,val) lower_bound((Itr).begin(),(Itr).end(),(val))
#define UBOUND(Itr,val) upper_bound((Itr).begin(),(Itr).end(),(val))
#define MOD 1000000007
typedef long long ll;

int main() {

    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1B/B/Bsmallin.txt");
    int T; ifs >> T;
    REP(kai,T) {
        int N,R,O,Y,G,B,V;
        ifs >> N >> R >> O >> Y >> G >> B >> V;
        bool flag = true;
        if(N/2 < R) flag = false;
        if(N/2 < Y) flag = false;
        if(N/2 < B) flag = false;
        if(!flag) {
            cout << "Case #" << kai + 1 << ": " << "IMPOSSIBLE" << endl;
        } else {
            string ans(N,'X');
            vector< pair<int,char> > p;
            p.push_back(make_pair(R,'R'));
            p.push_back(make_pair(Y,'Y'));
            p.push_back(make_pair(B,'B'));
            sort(p.begin(),p.end());
            reverse(p.begin(),p.end());
            int cnt = 0;
            REP(i,p.size()) {
                char c = p[i].second;
                int n = p[i].first;
                REP(j,n) {
                    ans[cnt] = c;
                    cnt += 2;
                    if(cnt >= N){
                        cnt = 1;
                    }
                }
            }
            cout << "Case #" << kai + 1 << ": " << ans << endl;
        }
    }
    
    return 0;
}