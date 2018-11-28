#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define ll long long
int main(){
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, tc = 1;
    cin>>t;
    while(t--){
        int n, i=0, ans=0;
        bool flag=0;
        string s; cin>>s>>n;
        while(i+n<=s.size()){
            if(s[i]=='+') i++;
            else{
                int count=1;
                while(i+count-1<s.size() && count<=n){
                    if(s[i+count-1]=='-') s[i+count-1]='+';
                    else s[i+count-1]='-';
                    count++;
                }
                ans++;
                i++;
            }
        }
        for(int i=0; i<s.size(); i++) if(s[i]=='-') flag=1;
        if(flag) cout<<"Case #"<<tc++<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<tc++<<": "<<ans<<endl;
    }
}
