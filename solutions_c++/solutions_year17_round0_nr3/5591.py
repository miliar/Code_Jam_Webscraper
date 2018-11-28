#include <iostream>
#include <vector>
#include <cmath>
#include <tuple>

using uint_t = uint64_t;
using tuple_t = std::tuple<uint_t, uint_t, uint_t>;




struct Position {
       
    bool occupied;
    uint_t left_neighbor;
    uint_t right_neighbor;
    
    void set(uint_t occ, uint_t left, uint_t right) {
        occupied = occ;
        left_neighbor = left;
        right_neighbor = right;
    }
    
};


struct Bathroom {
    uint_t n_positions;
    std::vector<Position> p;
    
    Bathroom(uint_t N) : n_positions(N+2) {
        p.resize(n_positions);
        Position& left = p.front();
        left.set(true, 0, N+1);
        Position& right = p.back();
        right.set(true, 0, N+1);
        for (uint_t i = 1; i < n_positions-1; ++i) {
            Position& pos = p[i];
            pos.set(false, 0, N+1);
        }
    }
    
    tuple_t max_distances() {
        uint_t min_value = 0;
        uint_t max_value = 0;
        uint_t index = 0;

        uint_t left_distance, right_distance, min_distance, max_distance;
        for (uint_t i = 0; i < p.size(); ++i) {
            if (p[i].occupied ==  false) {
                left_distance = i - p[i].left_neighbor-1;
                right_distance = p[i].right_neighbor - i-1;
                min_distance = std::min(left_distance, right_distance);
                max_distance = std::max(left_distance, right_distance);
                if (min_distance > min_value || (min_distance ==  min_value && max_distance > max_value)) {
                    min_value = min_distance;
                    max_value = max_distance;
                    index = i;
                }
            }
        }
        return std::make_tuple(index, min_value, max_value);
    }
    
    void add_customer() {
        
        uint_t index, min_value, max_value;
        std::tie(index, min_value, max_value) = max_distances();
        
        p[index].occupied = true;
        if (index != n_positions) {
            for (uint_t i = index+1; p[i].occupied == false && i < p.size(); ++i) {
                p[i].left_neighbor = index;
            }
        }
        if (index != 0) {
            for (uint_t i = index-1; p[i].occupied == false && i >= 0; --i) {
                p[i].right_neighbor = index;
            } 
        }
       
    }
    

};


void print(std::vector<Position> v) {
    for (auto& element : v) std::cout << element.occupied << " ";
    std::cout << std::endl;
}




int main() {
    
    uint_t T;
    std::cin >> T;
    
    for (uint_t t = 1; t <= T; ++t) {
        uint_t N, K;
        std::cin >> N >> K;
        Bathroom b(N);
        for (uint_t i = 0; i < K-1; ++i) {
            b.add_customer();
        }
        
        uint_t index, min_distance, max_distance;
        std::tie(index, min_distance, max_distance) = b.max_distances();
        
        
        std::cout << "Case #" << t << ": " << max_distance << " " << min_distance << std::endl;
    }
    
    return 0;
}
