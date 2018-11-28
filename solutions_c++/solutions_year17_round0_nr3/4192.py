#include <iostream>
#include <vector>
#include <string.h>
#include <string>
#include <map>
#include <stdio.h>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#define fs first
#define sc second
#define mp make_pair
#define sqr(x) (x)*(x)
#define pll pair<long long, long long>
#define ONLINE_JUDGE
using namespace std;
typedef long long ll;

int t,it;
int k,n;

pll Solve(int n, int k){
    int val;
    priority_queue<int> heap;
    heap.push(n);
    while(k-- && !heap.empty()){
        val = heap.top();
        heap.pop();
        if ((val-1)/2 > 1) heap.push((val-1)/2);
        if (val/2 > 1) heap.push(val/2);
//        heap.push(val/2);
//        heap.push((val-1)/2);
//        printf("%d\n%d\n", val/2,(val-1)/2);
    }
    if (k>=0) val = 1;
    return mp((val-1)/2, val/2);
}

int main(){
    freopen("input.txt", "r", stdin);
    #ifdef ONLINE_JUDGE
        freopen("C.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    ios_base::sync_with_stdio(false);
    cin>>t;
    while (t--){
        cin>>n>>k;
        cout<<"Case #"<<++it<<": ";
        pll ans = Solve(n,k);
        cout<<max(ans.fs, ans.sc)<<" "<<min(ans.fs, ans.sc)<<endl;
    }
    #ifdef ONLINE_JUDGE
        fclose(stdout);
    #endif // ONLINE_JUDGE
    return 0;
}


