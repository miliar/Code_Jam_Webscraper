#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iomanip>

#define LL long long
#define LD long double

using namespace std;

const int MAXN = 1001000;

int T;
int N, K;
int ansl, ansr;

void solve(){
    priority_queue<int> q;
    q.push(N);
    for(int i=0; i<K; i++){
        int x = q.top();
        q.pop();
        x--;
        ansl = x/2;
        ansr = x - ansl;
        q.push(ansl);
        q.push(ansr);
    }
}
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0_out.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> N >> K;
        solve();
        cout << "Case #" << i << ": " << ansr << " " << ansl << endl;
    }

    return 0;
}
