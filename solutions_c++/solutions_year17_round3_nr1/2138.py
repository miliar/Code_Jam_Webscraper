#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <list>
#include <set>
#include <algorithm>
#include <iomanip>

int main( void ){
    int T;
    std::cin >> T;
    for(int t=1; t<T+1; t++){
        int d, n;
        std::cin >> d >> n;
        std::set< std::pair<int, int> > set;
        for(int i=0; i<n; i++){
            int k, s;
            std::cin >> k >> s;
            set.insert( std::make_pair(k, s) );
        }
        double last_collision_time = 0;
        while( set.size() > 1 ){
            // std::cout << "set size: " << set.size() << std::endl;
            std::pair<int, int> minimum = *(set.begin());
            double minimum_collision_time = 0;
            double new_start = 0;
            double new_speed = 0;
            std::set< std::pair<int, int> >::iterator element_to_remove;
            for(auto it = set.begin(); it != set.end(); ++it){
                if( it == set.begin() ) continue;
                double start = it->first;
                double speed = it->second;
                double collision_time = (start - minimum.first) / (minimum.second - speed);
                // std::cout << "min start = " << minimum.first << std::endl;
                // std::cout << "min speed = " << minimum.second << std::endl;
                // std::cout << "start = " << start << std::endl;
                // std::cout << "speed = " << speed << std::endl;
                // std::cout << "fb: " << (minimum.second - speed) << std::endl;
                // std::cout << "sb: " << (start - minimum.first) << std::endl;
                // std::cout << "collision time: " << collision_time << std::endl;
                if( collision_time > minimum_collision_time ){
                    minimum_collision_time = collision_time;
                    element_to_remove = it;
                    new_start = (minimum.first) + minimum_collision_time * (minimum.second);
                    new_speed = minimum.second;
                    if( speed < new_speed ) new_speed = speed;
                    // std::cout << "new_start: " << new_start << std::endl;
                    // std::cout << "new_speed: " << new_speed << std::endl;
                }
            }
            if( minimum_collision_time > 0 ){
                last_collision_time += minimum_collision_time;
                set.erase( element_to_remove );
                set.erase( set.begin() );
                set.insert( std::make_pair( new_start, new_speed ) );
            } else {
                break;
            }
        }
        // std::cout << "OK" << std::endl;
        // std::cout << "last_collision_time: " << last_collision_time << std::endl;
        double last_arrival_time = last_collision_time + ((d - set.begin()->first) / (set.begin()->second));
        // std::cout << "last_arrival_time: " << last_arrival_time << std::endl;
        double max_speed = d / last_arrival_time;
        std::cout << std::fixed;
        std::cout << std::setprecision(6);
        std::cout << "Case #" << t << ": " << max_speed << std::endl;
    }
}