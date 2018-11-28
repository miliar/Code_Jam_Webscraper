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
#define FILL(Itr,n) fill((Itr).begin(),(Itr).end(),n)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define UNIQUE(Itr) sort((Itr).begin(),(Itr).end()); (Itr).erase(unique((Itr).begin(),(Itr).end()),(Itr).end())
#define LBOUND(Itr,val) lower_bound((Itr).begin(),(Itr).end(),(val))
#define UBOUND(Itr,val) upper_bound((Itr).begin(),(Itr).end(),(val))
#define MOD 1000000007
typedef long long ll;
typedef pair<int,int> P;

vector<ll> to_digit(ll n){
    vector<ll> ret;
    while(n != 0){
        ret.push_back(n%10);
        n /= 10;
    }
    reverse(ret.begin(),ret.end());
    return ret;
}

int main(){
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/B/Blargein.txt");
    int T; ifs >> T;
    
    REP(kai,T){
        ll N; ifs >> N;
        vector<ll> digits = to_digit(N);
        REP(ii,20){
            ll t = digits[0];
            REP(i,digits.size()){
                if(digits[i] < t){
                    digits[i-1]--;
                    for(int j = i; j < digits.size(); j++) digits[j] = 9;
                    goto finish;
                } else {
                    t = digits[i];
                }
            }
        finish:;
        }
        for(int i = (int)digits.size()-1; i >= 1; i--){
            if(digits[i] == -1){
                digits[i] = 9;
                digits[i-1]--;
            }
        }
        while(digits[0] == 0) digits.erase(digits.begin());
        cout << "Case #" << kai+1 << ": ";
        REP(i,digits.size()) cout << digits[i];
        cout << endl;
    }
    
    return 0;
}
