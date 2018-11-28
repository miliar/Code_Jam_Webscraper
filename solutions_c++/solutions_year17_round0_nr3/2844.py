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
    freopen("C-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, tc = 1;
    cin>>t;
    while(t--){
        ll n, k;
        cin>>n>>k;
        while(k!=1){
            if(n%2==0 && k%2) n=n/2-1;
            else n/=2;
            k/=2;
        }
        if(n%2==0) cout<<"Case #"<<tc++<<": "<<n/2<<" "<<max(n/2-1,0ll)<<endl;
        else cout<<"Case #"<<tc++<<": "<<n/2<<" "<<n/2<<endl;
    }
}
