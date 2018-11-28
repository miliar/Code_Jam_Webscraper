#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stack>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <unistd.h>

using namespace::std;

long double get_time(long double total_distance, long double current_distance, long double speed) {
    long double travel_distance = total_distance - current_distance;
    return travel_distance/speed;
}

int main() {
    freopen("/Users/udit/Downloads/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    cin>>test_cases;
    
    for (int i=1; i<=test_cases; i++) {
        long double total_distance;
        cin>>total_distance;
        
        long double num_of_horses;
        cin>>num_of_horses;
        
        long double current_distance;
        long double speed;
        long double max_time, time;
        
        cin>>current_distance>>speed;
        max_time = get_time(total_distance, current_distance, speed);
        time = max_time;
        
        for (long long int i=1;i<num_of_horses;i++) {
            cin>>current_distance>>speed;
            time = get_time(total_distance, current_distance, speed);
            
            if(time>max_time) {
                max_time = time;
            }
        }
        
        long double my_speed = total_distance/max_time;
        
        cout<<"Case #"<<i<<": ";
        printf("%.6Lf", my_speed);
        cout<<endl;
    }
    
    return 0;
}
