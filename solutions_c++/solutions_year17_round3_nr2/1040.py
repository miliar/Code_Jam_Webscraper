#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>
#include <cassert>
//#include <unordered_map>

#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>
#define PLDD pair<ld,ld>

using namespace std;

unsigned char dp[1450][730][730][2];
bool busy[2][1440];


unsigned char min(unsigned char a, unsigned char b)
{
    return a>b?b:a;
}

int main()
{
    ifstream cin("a.in");
    ofstream cout("a.out");
    ios::sync_with_stdio(0);
    int T;cin>>T;
    FOR(_,1,T+1) {
        CLR(dp, 230);
        CLR(busy, 0);
        cout << "Case #" << _ << ": ";
        int A[2];
        cin >> A[0] >> A[1];
        FR(_, 2) {
            FR(i, A[_]) {
                int a, b;
                cin >> a >> b;
                FOR(i, a, b) busy[_][i] = true;
            }
        }

        dp[1440][720][720][0] = 0;
        dp[1440][720][720][1] = 0;
        for(int i = 1439; i>= 0; i--)
        {
            for(int s = max(0,i-720); s <= min(720, i);s++)
            {
                int f = i-s;
                if(f < 0 || f > 720) continue;
                if(f == 720){
                    if(!busy[1][i]) {
                        dp[i][f][s][0] = dp[i + 1][f][s + 1][1] + 1;
                        dp[i][f][s][1] = dp[i + 1][f][s + 1][1];
                    }
                }
                else if(s == 720)
                {
                    if(!busy[0][i]) {
                        dp[i][f][s][1] = dp[i + 1][f + 1][s][0] + 1;
                        dp[i][f][s][0] = dp[i + 1][f + 1][s][0];
                    }
                }
                else {
                    if(busy[0][i]) dp[i][f][s][0] = dp[i+1][f][s+1][1]+1;
                    else {
                        dp[i][f][s][0] = dp[i+1][f+1][s][0];
                        if(!busy[1][i])
                        {
                            dp[i][f][s][0] = min(dp[i][f][s][0], dp[i+1][f][s+1][1]+1);
                        }
                    }
                    if(busy[1][i]) dp[i][f][s][1] = dp[i+1][f+1][s][0]+1;
                    else {
                        dp[i][f][s][1] = dp[i+1][f][s+1][1];
                        if(!busy[0][i])
                        {
                            dp[i][f][s][1] = min(dp[i][f][s][1], dp[i+1][f+1][s][0]+1);
                        }
                    }
                }
            }
        }


        int ans = (int)min(dp[0][0][0][0], dp[0][0][0][1]);
        if(ans%2==1) ans++;
        cout<<ans<<endl;
    }
}