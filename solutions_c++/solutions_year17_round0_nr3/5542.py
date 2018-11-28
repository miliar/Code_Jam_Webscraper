#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <bitset>
#include <set>
#include <map>
#include <sstream>
#include <queue>

using namespace std;
typedef pair<int,int> pii;

struct Interval{
    int a,
        b;

    bool operator<(const Interval &rhs) const{
        if(rhs.b - rhs.a == b-a){
            return rhs.a < a;
        }
        else return (rhs.b - rhs.a > b - a);
    }
};

int64_t T, K, N;



int main()
{
    /**
    priority_queue<Interval> test;
    Interval a = {1,2};
    Interval b = {2,3};
    Interval c = {4,7};
    Interval d = {0,3};
    test.push(a);
    test.push(b);
    test.push(c);
    test.push(d);
    while(!test.empty()){
        Interval cur = test.top();
        test.pop();
        cout << cur.a << " " << cur.b << endl;
    }
    **/
    cin >> T;
    int cnt = 0;
    while(T--){
        cnt++;
        cin >> N;
        cin >> K;
        vector<bool> S (N+2);
        S[0] = true;
        S[N+1] = true;
        priority_queue<Interval> Q;
        Interval p = {1,N};
        Q.push(p);
        int k = 0;

        while(!Q.empty() & k < K-1){
            //cout << k << endl;
            k++;
            Interval cur = Q.top();
            Q.pop();
            int a = cur.a,
                b = cur.b,
                place = (b + a) / 2;
            if(S[place]) continue;
            S[place] = true;
            //cout << "Placed on " << place << " as number " << k << " with " << a << "," << b << endl;
            Q.push({place+1,b});
            Q.push({a,place-1});
        }
        vector<int> L (N+2);
        vector<int> R (N+2);
        int l = 0;
        for(int i = 1; i < N+1; i++){
            if(S[i]) l = 0;
            L[i] = l;
            if(!S[i])l++;
        }
        int r = 0;
        for(int i = N; i >= 1; i--){
            if(S[i]) r = 0;
            R[i] = r;
            if(!S[i])r++;
        }
        int bestmin = 0;
        int bestmax = 0;
        for(int i = 1; i < N+1; i++){
          //  cout << "(" << L[i] << ", " << R[i] << ")" << endl;
        }
        for(int i = 1; i < N+1; i++){
            if(S[i]) continue;
            if( min(L[i],R[i]) > bestmin ){
                bestmin = min(L[i],R[i]);
                bestmax = max(L[i],R[i]);
            } else if ( min(L[i],R[i]) == bestmin ){
                if( max(L[i],R[i]) > bestmax ){
                    bestmax = max(L[i],R[i]);
                }
            }
        }
        cout << "Case #" << cnt << ": ";
        cout << bestmax << " " << bestmin << endl;
    }
    return 0;
}
