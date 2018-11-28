
#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

int main()
{
    freopen("a-large-out.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++){
        string s;
        int k;
        cin>>s>>k;
        int ans = 0;
        for(unsigned int j = 0; j < s.length(); j++){
            if(s[j] == '-'){
                ans++;
                if(j+k-1 >= s.length()){
                    ans = -1;
                    break;
                }
                for(unsigned int m = j; m < j+k; m++){
                    if(s[m] == '+') s[m] = '-';
                    else s[m] = '+';
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        if(ans < 0) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
