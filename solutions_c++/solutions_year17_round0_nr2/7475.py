
#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef long long ll;

ll largeTidy(ll n){
    vector<int> digits;
    while( n> 0){
        digits.push_back(n%10);
        n/=10;
    }
    reverse(digits.begin(), digits.end());
    for(int i=digits.size() - 1;i>=1;i--){
        if(digits[i] < digits[i-1]){
            digits[i-1]--;
            for(int j = i;j<digits.size();j++)
                digits[j] = 9;
        }
    }
    if(digits[0] == 0){
        digits.erase(digits.begin());
    }
    stringstream result;
    copy(digits.begin(), digits.end(), std::ostream_iterator<int>(result,""));
    return stoll(result.str());
}

int main(){
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        ll n;
        cin >> n;
        cout << "Case #" << i << ": ";
        cout << largeTidy(n) << endl;
    }
    return 0;
}