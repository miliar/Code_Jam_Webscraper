//
//  d.cpp
//
// c++11

#include <cstdlib>
#include <stdint.h>
#include <iostream>
#include <iomanip>
#include <utility>
#include <functional>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <math.h>

//#include <boost/multiprecision/cpp_int.hpp>  // www.boost.org/
//using namespace boost::multiprecision;
// cpp_int


#define int int64_t

// globals

std::ifstream inFile;

// utility functions

// read one scalar from text file inFile
template <typename T>
void rd(T & x) {inFile >> x;}

// read scalars from text file inFile
template <typename T, typename ...Ts>
void rd(T & x, Ts & ...xs) {inFile >> x; rd(xs...);}

template <typename T>
void rdhelp(std::vector <T> & v) {T elt; inFile >> elt; v.push_back(elt);}

template <typename T, typename ...Ts>
void rdhelp(std::vector <T> & v, std::vector <Ts> & ...vs)
{T elt; inFile >> elt; v.push_back(elt); rdhelp(vs...);}

// read vectors from text file
template <typename T, typename ...Ts>
void rd(int const N, std::vector <T> & v, std::vector <Ts> & ...vs)
{for (int i=0; i<N; i++) {rdhelp(v, vs...);}}

void prhelp() {std::cout << "\n";}

template <typename T, typename ...Ts>
void prhelp(const T & x, const Ts & ...xs) {std::cout << " " << x; prhelp(xs...);}

// print newline
void pr() {std::cout << "\n";}

// print scalars separated by spaces, followed by a newline
template <typename T, typename ...Ts>
void pr(const T & x, const Ts & ...xs) {std::cout << x; prhelp(xs...);}

// print vector to std::cout
template <typename T>
void pr(std::vector<T> const & v)
{for (int i=0; i<(int)v.size(); i++) {
    if (i>0) std::cout << " ";
    std::cout << v[i];}
std::cout << "\n";}

// print set to std::cout
template <typename T>
void pr(std::set<T> const & s)
{for (auto it=s.begin(); it!=s.end(); ++it) {
    if (it!=s.begin()) std::cout << " ";
    std::cout << *it;}
std::cout << "\n";}

// print map to std::cout
template <typename T, typename S>
void pr(std::map<T,S> const & m)
{for (auto it=m.begin(); it!=m.end(); ++it) {
    std::cout << it->first << " " << it->second << "\n";}}

// print scalars NOT separated by spaces, followed by a newline
void prshelp() {std::cout << "\n";}

template <typename T, typename ...Ts>
void prshelp(const T & x, const Ts & ...xs) {std::cout << x; prshelp(xs...);}

template <typename T, typename ...Ts>
void prs(const T & x, const Ts & ...xs) {std::cout << x; prshelp(xs...);}

// print vector to std::cout, WITHOUT separating spaces
template <typename T>
void prs(std::vector<T> const & v)
{for (int i=0; i<(int)v.size(); i++) {std::cout << v[i];} std::cout << "\n";}

// print scalars separated by spaces, NOT followed by a newline
void prnhelp() {}

template <typename T, typename ...Ts>
void prnhelp(const T & x, const Ts & ...xs) {std::cout << " " << x; prnhelp(xs...);}

template <typename T, typename ...Ts>
void prn(const T & x, const Ts & ...xs) {std::cout << x; prnhelp(xs...);}

// print vector to std::cout, NOT followed by a newline
template <typename T>
void prn(std::vector<T> const & v)
{for (int i=0; i<(int)v.size(); i++) {
    if (i>0) std::cout << " ";
    std::cout << v[i];}}

// print scalars NOT separated by spaces, NOT followed by a newline
void prnshelp() {}

template <typename T, typename ...Ts>
void prnshelp(const T & x, const Ts & ...xs) {std::cout << x; prnshelp(xs...);}

template <typename T, typename ...Ts>
void prns(const T & x, const Ts & ...xs) {std::cout << x; prnshelp(xs...);}

// print vector to std::cout, WITHOUT separating spaces, NOT followed by a newline
template <typename T>
void prns(std::vector<T> const & v)
{for (int i=0; i<(int)v.size(); i++) {std::cout << v[i];}}

// Has effect of m = std::max(m,v)
template <typename T>
const T & mxeq(T & m, const T & v) {m = std::max(m,v); return m;}

// Has effect of m = std::min(m,v)
template <typename T>
const T & mneq(T & m, const T & v) {m = std::min(m,v); return m;}

// Maximum value in a nonempty vector
template <typename T>
const T & vmax(const std::vector<T> & v) {return *std::max_element(v.begin(),v.end());}

// Minimum value in a nonempty vector
template <typename T>
const T & vmin(const std::vector<T> & v) {return *std::min_element(v.begin(),v.end());}

// sort vector (ascending order)
template <typename T>
void vsort(std::vector<T> & v) {std::sort(v.begin(), v.end());}

// sort vector in descending order
template <typename T>
void vsortd(std::vector<T> & v){std::sort(v.begin(), v.end(), std::greater<T>());}

// other stuff

// functions

void setup()
{
}


void processCase()
{
    int N,M;
    rd(N,M);
    
    std::vector<std::vector<int> > oplus(N, std::vector<int> (N));
    std::vector<std::vector<int> > plus(N, std::vector<int> (N));
    std::vector<std::vector<int> > ox(N, std::vector<int> (N));
    std::vector<std::vector<int> > x(N, std::vector<int> (N));
    std::vector<int> xc(N);
    std::vector<int> xr(N);
    
    for (int i=0; i<M; ++i) {
        char mod;
        int R,C;
        rd(mod, R, C);
        if (mod=='+' || mod=='o') {
            oplus[R-1][C-1]=1;
        }
        if (mod=='x' || mod=='o') {
            ox[R-1][C-1]=1;
            xc[C-1]=1;
            xr[R-1]=1;
        }
    }
    
//     pr();
//     for (int i=0; i<N; ++i) {
//         prs(plus[i]);
//     }
//     pr();
//     for (int i=0; i<N; ++i) {
//         prs(x[i]);
//     }
    
    x=ox;
    plus=oplus;
    
    int row=0;
    int col=0;
    while (1) {
        while (col<N && xc[col]) {
            col++;
        }
        while (row<N && xr[row]) {
            row++;
        }
        if (col<N) {
            x[row][col]=1;
            row++;
            col++;
        } else {
            break;
        }
    }
    
    //
//     for (int i=0; i<N; ++i) {
//         plus[0][i]=1;
//     }
//     for (int i=1; i<N-1; ++i) {
//         plus[N-1][i]=1;
//     }
    
    std::vector<std::vector<int> > f(N, std::vector<int> (N));
    
    for (int i=0; i<N; ++i) {
        for (int j=0; j<N; ++j) {
            if (plus[i][j]) {
                for (int c=0; c<N; ++c) {
                    int r = i+j-c;
                    if (r>=0 && r<N) {
                        f[r][c]=1;
                    }
                    r = i-j+c;
                    if (r>=0 && r<N) {
                        f[r][c]=1;
                    }
                }
            }
        }
    }
    
    while (1) {
        std::vector<int> d1(2*N-1);
        std::vector<int> d2(2*N-1);
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                if (f[i][j]==0) {
                    d1[i+j]++;
                    d2[i+N-j]++;
                }
            }
        }
        
        int best=N+1;
        int besti, bestj;
        
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                if (f[i][j]==0) {
                    if (d1[i+j]<best) {
                        best = d1[i+j];
                        besti=i;
                        bestj=j;
                    }
                    if (d2[i+N-j]<best) {
                        best = d2[i+N-j];
                        besti=i;
                        bestj=j;
                    }
                }
            }
        }
        if (best==N+1) break;
        
        plus[besti][bestj]=1;
        for (int c=0; c<N; ++c) {
            int r = besti+bestj-c;
            if (r>=0 && r<N) {
                f[r][c]=1;
            }
            r = besti-bestj+c;
            if (r>=0 && r<N) {
                f[r][c]=1;
            }
        }
        
        
    }
    
    
    
    //
    
    int score=0;
    int mc=0;
    for (int i=0; i<N; ++i) {
        for (int j=0; j<N; ++j) {
            score += plus[i][j]+x[i][j];
            mc += (plus[i][j]!=oplus[i][j] || x[i][j]!=ox[i][j]);
        }
    }
    pr(score, mc);
    for (int i=0; i<N; ++i) {
        for (int j=0; j<N; ++j) {
            if (plus[i][j]!=oplus[i][j] || x[i][j]!=ox[i][j]) {
                pr(".+xo"[plus[i][j]+2*x[i][j]], i+1, j+1);
            }
        }
    }
    
}


// main

#undef int
int main(int argc, char const * argv[])
{
    // make sure filename is provided
    if (argc != 2) {std::cerr << "Expected one argument\n"; std::exit(0);}
    
    // open input file and get number of cases
    int T; inFile.open(argv[1]);
    if (inFile.fail()) {std::cerr << "Failed to open file\n"; std::exit(0);}
    rd(T);    
    
    setup();
    
    std::cout << std::setprecision(9);
    
    for (int caseIndex=1; caseIndex<=T; caseIndex++) {
        std::cout << "Case #" << caseIndex << ": "; processCase();}
    return 0;
}
