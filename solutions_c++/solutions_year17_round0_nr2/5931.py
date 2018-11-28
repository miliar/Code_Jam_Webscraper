
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
#include <sstream>

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



template <class T>
inline std::string to_string (const T& t){
    std::stringstream ss;
    ss << t;
    return ss.str();
}

ULL solve(ULL n){
    string s = to_string(n);
    if(s.length() == 1) return n;
    ULL ans = 0;
    string ss = "";
    for(unsigned int i = 0; i < s.length()-1; i++){
        if(s[i] > s[i+1]){
            if(i == 0){
                s[i] = s[i] - 1;
                i++;
                while(i < s.length()){s[i] = '9'; i++;};
                break;
            }
            for(unsigned int j = i; j >= 0; j--){
                if(j == 0) {
                        s[j] = s[j] - 1;
                        j++;
                        while(j < s.length()){s[j] = '9'; j++;};
                        break;
                }
                else {
                    if(s[j]-1 >= s[j-1]){
                        s[j] = s[j] - 1;                    
                        j++;
                        while(j < s.length()){s[j] = '9'; j++;};
                        break;
                    }
                }
            }
        }
    }
    if(s[0] == '0'){
        unsigned int len = s.length() - 1;
        while(len--) ss += '9';
    }
    else ss = s;
    ULL base = 1;
    for(int i = ss.length()-1; i >= 0; i--){
        ans += (ss[i] - '0') * base;
//        cout<<i<<" "<<ans<<endl;
        base *= 10;
    }
//    cout<<ans<<endl;
    return ans;
}

int main()
{
    freopen("b-large-out.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    int t;
    cin>>t;
    for(int m = 1; m <= t; m++){
        ULL n;
        cin>>n;
        cout<<"Case #"<<m<<": ";
        cout<<solve(n)<<endl;
    }
    return 0;
}
