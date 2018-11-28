#include <iostream>
#include <cstdio>  
#include <iostream>  
#include <string>  
#include <iterator>  
#include <algorithm>  
#include <vector>  
#include <cstring>  
#include <array>  
#include <queue>  
#include <set>  
#include <map>  
#include <utility>
using namespace std;

typedef long long ll;


// struct comp{
//     bool operator() (pair<ll, ll> a, pair<ll, ll> b){
//         return (ll)(a.second - a.first) < (ll)(b.second - b.first);
//     }
// };

pair<ll, ll> solve(ll N, ll K) {
    while(K != 1) {
        if(K % 2 == 0) {
            N /= 2;
            K /= 2;
        }
        else {
            N = (N - 1) / 2;
            K /= 2;
        }
    }
    return make_pair(N / 2, (N - 1) / 2);
}


int main()  
{  
    freopen("C-large.in.txt", "r", stdin);  
    //freopen("in.txt", "r",stdin);  
    freopen("out.txt", "w", stdout);  
    int t;  
    scanf("%d", &t);  
    for (int i = 1; i<= t; i++)  
    {  
        ll N, K;
        cin>>N>>K;
        printf("Case #%d: ", i);  
        pair<ll, ll> res = solve(N, K);
        cout<<res.first<<" "<<res.second<<endl;
    }  
    return 0;  
}  