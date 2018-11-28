#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define ALL(x) x.begin(),x.end()

#define DEB(args...) fprintf(stderr,args)

#define PB push_back
#define MP make_pair
#define ST first
#define ND second 

const int INF = 0x3f3f3f3f;
const int N = 1010;


vector<int> us[N];
vector<int> pas;

multiset<int> st;

int pos[N][N];
int pref[N],val[N];


int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 0; cas < t; cas++){
        st.clear();
        int n, m, c;
        scanf("%d%d%d", &n, &c, &m);
        for(int i = 1; i <= c; i++){
            us[i].clear();
        }
        pas.clear();
        for(int i = 0; i < n; i++){
            pref[i]=0;
            val[i]=0;
        }
        for(int i = 0; i < m; i++){
            int a, b;
            scanf("%d%d",&a,&b);
            us[b].push_back(a);
            pas.push_back(a);
            val[a]++;
        }
        for(int i = 1;i <= n; i++){
            pref[i]=pref[i-1]+val[i];
        }
        int mn = 0;
        for(int i = 1; i <= c; i++){
            mn = max(mn, (int)us[i].size());
        }
        for(int i = 1; i <= n; i++){
            mn = max(mn, pref[i]/(i));
        }
        //size of mn

        sort(pas.begin(),pas.end());

        for(int i = 1; i <= n; i++){
            for(int j = 0; j < mn; j++){
                st.insert(i);
            }
        }
        long long ans = 0;
        for(int i = 0; i < m; i++){
            if(st.find(pas[i])!=st.end()){
                //printf("find %d\n",*st.find(pas[i]));
                st.erase(st.find(pas[i]));
            }
            else{
                st.erase(st.begin());
                ans++;
            }
        }
        printf("Case #%d: %d %lld\n", cas+1, mn,ans);
    }
    
}
