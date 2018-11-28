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
int main(){
    freopen("B-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, tc = 1;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        for(int i=(int)s.size()-2; i>=0; i--){
            if(s[i]>s[i+1]){
                for(int j=i+1; j<s.size(); j++) s[j]='9';
                s[i]--;
            }
        }
        if(s[0]=='0') s.erase(0,1);
        cout<<"Case #"<<tc++<<": "<<s<<endl;
    }
}
