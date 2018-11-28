#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <time.h>
#include <assert.h>
#define MAXN 10000000
using namespace std;

int t;



int main(){
    freopen("/Users/Masoud/Desktop/C-large.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        long long n,k;
        scanf("%lld %lld", &n, &k);
        map<long long, long long> mp;
        priority_queue<long long> pq;
        unordered_set<long long> vis;
        pq.push(n);
        mp[n] = 1;
        long long mx =0, mn = 0;
        while(!pq.empty()){
            long long sub_problem_size = pq.top();
            pq.pop();
            if(mp[sub_problem_size] >= k){
                mx = mn = sub_problem_size / 2;
                if(!(sub_problem_size&1)){
                    mn--;
                }
                break;
            }else{
                long long right = sub_problem_size / 2;
                long long left = right;
                if (!(sub_problem_size&1)) {
                    left--;
                }
                mp[left]+= mp[sub_problem_size];
                mp[right]+= mp[sub_problem_size];
                if(!vis.count(left)){
                    pq.push(left);
                    vis.insert(left);
                }
                
                if(!vis.count(right)){
                    pq.push(right);
                    vis.insert(right);
                }
                k-=mp[sub_problem_size];                
            }
        }
        printf("Case #%d: %lld %lld\n", ca++, mx, mn);
    }
    return 0;
}




