//
//  main.cpp
//  Alphabet Cake
//
//  Created by Rugen Heidbuchel on 15/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef std::vector<int> vi;
typedef std::pair<int, int> ii;
typedef std::vector<ii> vii;
typedef std::set<int> si;
typedef std::map<std::string, int> msi;

// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

#include <vector>
#include <iostream>
#include <initializer_list>
#include <cmath>

template<class T>
class Array2D{
public:
    // x is the amount of rows and y the amount of columns
    Array2D(std::size_t x, std::size_t y, T default_value = T()):
    X_{x}, Y_{y}, values_(x*y, default_value){
    }
    
    Array2D(std::initializer_list<T> init):
    X_{0}, Y_{0}, values_(init) {
        X_ = Y_ = static_cast<std::size_t>(std::sqrt(init.size()));
    }
    
    virtual ~Array2D() = default;
    
    T& at(std::size_t x, std::size_t y) {
        return values_[x*Y_ + y];
    };
    
    T at(std::size_t x, std::size_t y) const{
        return values_[x*Y_ + y];
    };
    
    template <class S>
    bool is_within_bounds(S x, S y) const {
        return x >= 0 && y >= 0 && static_cast<std::size_t>(x) < this->x() && static_cast<std::size_t>(y) < this->y();
    }
    
    template <class S>
    T get(S x, S y, const T& def) const {
        if (is_within_bounds(x, y)) {
            return at(x, y);
        }
        
        return def;
    }
    
    std::size_t x() const {
        return X_;
    }
    
    std::size_t y() const {
        return Y_;
    }
    
    typename std::vector<T>::iterator begin() {
        return values_.begin();
    }
    
    typename std::vector<T>::iterator end() {
        return values_.end();
    }
    
protected:
    std::size_t X_;
    std::size_t Y_;
    std::vector<T> values_;
    
    template <class S>
    friend std::ostream& operator<<(std::ostream&, const Array2D<S>&);
};

template <class T>
std::ostream& operator<<(std::ostream& os, const Array2D<T>& a) {
    for (std::size_t x = 0; x < a.X_; ++x) {
        os << "|";
        for (std::size_t y = 0; y < a.Y_; ++y) {
            os << a.at(x, y) << ((y != a.Y_ - 1) ? ", " : "");
        }
        os << "|\n";
    }
    return os;
}




#pragma mark - MAIN

size_t T;
int R, C;

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ":\n";
        
        std::cin >> R >> C;
        Array2D<char> cake(R, C, '?');
        std::set<char> used;
        
        for (int i = 0; i < R; i++) {
            std::string S;
            std::cin >> S;
            for (int j = 0; j < C; j++) {
                cake.at(i, j) = S[j];
            }
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                char c = cake.at(i, j);
                if (used.find(c) != used.end()) continue;
                used.insert(c);
                int li = i, hi = i, lj = j, hj = j;
                for (int k = li+1; k < R; k++) {
                    bool expandable = true;
                    for (int l = lj; l <= hj; l++) {
                        if (cake.at(k, l) != '?') {
                            expandable = false;
                            break;
                        }
                    }
                    if (expandable) {
                        hi = k;
                        for (int l = lj; l <= hj; l++) {
                            cake.at(k, l) = c;
                        }
                    } else {
                        break;
                    }
                }
                for (int k = li-1; k >= 0; k--) {
                    bool expandable = true;
                    for (int l = lj; l <= hj; l++) {
                        if (cake.at(k, l) != '?') {
                            expandable = false;
                            break;
                        }
                    }
                    if (expandable) {
                        li = k;
                        for (int l = lj; l <= hj; l++) {
                            cake.at(k, l) = c;
                        }
                    } else {
                        break;
                    }
                }
                for (int k = lj+1; k < C; k++) {
                    bool expandable = true;
                    for (int l = li; l <= hi; l++) {
                        if (cake.at(l, k) != '?') {
                            expandable = false;
                            break;
                        }
                    }
                    if (expandable) {
                        hj = k;
                        for (int l = li; l <= hi; l++) {
                            cake.at(l, k) = c;
                        }
                    } else {
                        break;
                    }
                }
                for (int k = lj-1; k >= 0; k--) {
                    bool expandable = true;
                    for (int l = li; l <= hi; l++) {
                        if (cake.at(l, k) != '?') {
                            expandable = false;
                            break;
                        }
                    }
                    if (expandable) {
                        lj = k;
                        for (int l = li; l <= hi; l++) {
                            cake.at(l, k) = c;
                        }
                    } else {
                        break;
                    }
                }
            }
        }
        
        for (size_t i = 0; i < R; i++) {
            for (size_t j = 0; j < C; j++) {
                std::cout << cake.at(i, j);
            }
            std::cout << "\n";
        }
    }
    
    return 0;
}
