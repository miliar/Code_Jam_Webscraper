#include <iostream>
#include <iomanip>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t=0; t<T; ++t){
        int N, K;
        cin >> N; cin >> K;

        vector<pair<double, double> > v(N);
        for(int n=0; n<N; ++n){
            double r, h;
            cin >> r; cin >> h;
            v[n] = make_pair(r, h);
        }
        
        sort(v.begin(), v.end());

        double mm = 0;
        for(int m=0; m<=N-K; m++){
            double sum=0;
            double r1=v[N-1-m].first;
            double h1=v[N-1-m].second;
            sum += (2*M_PI*r1*h1)+(M_PI*r1*r1);
            
            vector<double> vk(N-m);
            for(int i=N-1-m-1; i>=0; --i){
                double r=v[i].first;
                double h=v[i].second;
                vk.push_back(2 * M_PI * r * h);
            }
            sort(vk.begin(), vk.end(), greater<double>());
            for(int i=0; i<K-1; ++i){
                sum+=vk[i];
            }            
            mm = max(mm, sum);
        }
        
        cout << "Case #" << t+1 << ": " << fixed << setprecision(10) << mm << endl;
    }
    
    return 0;
}
