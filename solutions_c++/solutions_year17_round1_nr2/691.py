//
//  b.cpp
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
    int N,P;
    rd(N,P);
    std::vector<int> R;
    rd(N,R);
    std::vector<std::vector<int> > Q(N);
    for (int i=0; i<N; ++i) {
        rd(P,Q[i]);
        vsort(Q[i]);
    }
    
    std::vector<std::vector<int> > r0(N,std::vector<int> (P));
    std::vector<std::vector<int> > r1(N,std::vector<int> (P));
    
    for (int i=0; i<N; ++i) {
        for (int j=0; j<P; ++j) {
            r0[i][j] = (Q[i][j]*10-1)/(11*R[i])+1;
            r1[i][j] = (Q[i][j]*10)/(9*R[i]);
        }
//         prn("r0: "); pr(r0[i]);
//         prn("r1: "); pr(r1[i]);
    }
    
    
    
    
    std::vector<int> pos(N);
    int count=0;
    
    
    while (1) {
        int m0 = r0[0][pos[0]];
        for (int i=1; i<N; ++i) {
            mxeq(m0,r0[i][pos[i]]);
        }
        bool good=1;
        for (int i=0; i<N; ++i) {
            if (r1[i][pos[i]] < m0) {
                pos[i]++;
                good=0;
                if (pos[i]==P) {
                    pr(count);
                    return;
                }
            }
        }
        if (good) {
            count++;
            for (int i=0; i<N; ++i) {
                pos[i]++;
                if (pos[i]==P) {
                    pr(count);
                    return;
                }
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
