#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
//#include<pair>

using namespace std;

int main() {

    int t, d, k, s, n;
    cin >> t;
    //vector< pair<int, int> >v(1001);
    pair<int, int>p;
    
    double time, temp;
    long long int dist, speed, tdist, tspeed;
    
    for (int x = 0; x < t; x++) {
        
        cin >> d >> n;
        vector< pair<int, int> >v(n);
        for (int i = 0; i < n; i++) {
            cin >> k >> s;
            p.first = d-k;
            p.second = s;
            v.push_back(p);
        }
        
        sort(v.rbegin(), v.rend());
        
        time = (v[0].first*1.0)/v[0].second;
        //dist = v[0].first;
        //speed = v[0].second;
        
        for (int i = 1; i < n; i++) {
            
            
            
            temp = (v[i].first*1.0)/v[i].second;
            if (temp > time) time = temp;
        }
        
        //cout << time << endl;
        std::cout << std::fixed;
        cout << "Case #" << x + 1 << ": " << d*1.0/time << endl;
    }             
    
    return 0;
}             
            
        
        
        
