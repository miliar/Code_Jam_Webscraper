#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int q;
long long n,k;
long long answ1,answ2;
map <long long,long long> mp;

int main(){
    //freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>q;
    for(int i=1;i<=q;i++){
        cin>>n>>k;
        k--;
        long long answ = n , T = n;
        mp[n]++;
        while(k > 0){
            long long x = T / 2;
            answ = x;
            k -= mp[2 * x] + (2ll) * mp[2 * x + 1] + mp[2 * x + 2];
            if(k <= 0)break;
            answ = x - 1;
            k -= mp[2 * (x - 1)] + (2ll) * mp[2 * (x - 1) + 1] + mp[2 * (x - 1) + 2];
            if(k <= 0)break;
            mp[x] += mp[2 * x] + (2ll) * mp[2 * x + 1] + mp[2 * x + 2];
            mp[x - 1] += mp[2 * (x - 1)] + (2ll) * mp[2 * (x - 1) + 1] + mp[2 * (x - 1) + 2];
            T /= 2;
        }
        mp.clear();
        if(answ % 2){
            answ1 = answ / 2;
            answ2 = answ / 2;
        }
        else{
            answ1 = answ / 2;
            answ2 = answ / 2 - 1;
        }
        cout<<"Case #"<<i<<": "<<answ1<<" "<<answ2<<endl;
    }
    return 0;
}
