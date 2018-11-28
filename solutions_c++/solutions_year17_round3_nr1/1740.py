#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
using namespace std;

struct Pancake {
    double R;
    double H;
    
    
};

bool comp1(const Pancake &p1, const Pancake &p2) 
{
    return p1.R < p2.R;
}


const double PI = 3.141592653589793238462643383279;
double solve() {
    int N,K;
    cin >> N >> K;
    double R,H;
    
    vector<Pancake> v;
    
    for(int i = 0; i < N; i++) {
        v.push_back(Pancake());
        cin >> v[i].R >> v[i].H;
    }
    sort(v.begin(), v.end(), comp1);
    
    
    //for(int i = 0; i < N; i++) {
    //    cout << v[i].R << " " << v[i].H << endl;
    //}
    //cout << endl << endl;
    
    double ch = 0;
    priority_queue<double, vector<double>, greater<double> > pq;
    double tmp;
    for(int k = 0; k < K - 1; k++) {
        tmp = v[k].R * v[k].H;
        ch += tmp;
        pq.push(tmp);
    }

    double mch = 0;
    double tmp2;
    
    
    for(int i = K-1; i < N; i++) {
        tmp = v[i].R * v[i].H;
        
        tmp2 = (ch + tmp) * PI * 2.0 + v[i].R*v[i].R*PI;
        if (tmp2 > mch) mch = tmp2;
        
        if (K != 1)
        {
            if ( ch < (ch - pq.top() + tmp) ) {
            ch = ch - pq.top() + tmp;
            pq.pop();
            pq.push(tmp);
            }
        }       
    }
    
    return mch;
}


int main() {
    int T; cin >> T;
    for(int t = 0; t < T; t++) {
     
        double ans = solve();
        printf("Case #%d: %.9f\n", t + 1, ans);
        //cout << "Case #" << t+1 << ": " << ans << endl;
    }
    return 0;
}