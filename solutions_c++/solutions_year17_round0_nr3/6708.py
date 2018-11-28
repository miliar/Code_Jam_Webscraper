/* 
 * File:   bathroom_stalls.cpp
 * Author: hanv2
 *
 * Created on April 8, 2017, 1:53 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;
/*
 * 
 */
void brute_force_bathroom(unsigned long long &max, unsigned long long &min, const unsigned long long k, const unsigned long long n);
void smart_bathroom(unsigned long long &max, unsigned long long &min, const unsigned long long k, const unsigned long long n);

int main(int argc, char** argv) {
//    ios_base::sync_with_stdio(false);
//    cin.tie(nullptr);
        
    std::ifstream in;
//  redirect to stdin if necessary   
//    std::streambuf *cinbuf = std::cin.rdbuf(); 
    std::ofstream out;
//  redirect to stdout if necessary    
//    std::streambuf *coutbuf = std::cout.rdbuf(); 
    if (argc > 1){
        stringstream ssInput;
        ssInput << argv[1] << ".in";
        in = std::ifstream(ssInput.str().c_str());
        std::cin.rdbuf(in.rdbuf());

        stringstream ssOutput;
        ssOutput << argv[1] << ".out";
        out = std::ofstream(ssOutput.str().c_str());
        std::cout.rdbuf(out.rdbuf()); 
    }
    
    int t;
    cin >> t;
    for (int i = 1;i <= t;++i){
        unsigned long long n;
        unsigned long long k;
        cin >> n >> k;
        //debug input
//        cout << "\nn: "<<n;
//        cout << "\nk: "<<k<<"\n";       
            
        //solve
        unsigned long long min;
        unsigned long long max;
        brute_force_bathroom(max, min, k,n);
        
        //print result 
        cout << "Case #" << i << ": " <<  max << " " << min << "\n";
        
        //double check by brute force
//        unsigned long long min1;
//        unsigned long long max1;
//        brute_force_bathroom(max1, min1, k,n);       
//        if (max1 == max && min1 == min){
//            cout << "Check case #" << i << ":OK\n\n";
//        } else {
//            cout << "Check case #" << i << ":ERRRRR\n";            
//            cout << "Case #" << i << ": " <<  max1 << " " << min1 << "(brute force)\n\n";
//        }
    }
    return 0;
}

void smart_bathroom(unsigned long long &max, unsigned long long &min, const unsigned long long inp_k, const unsigned long long inp_n){
    unsigned long long n = inp_n;
    unsigned long long k = inp_k;
    vector<unsigned long long> path;
    path.push_back(k);
    while (k >>= 1) 
    {  
        path.push_back(k);
    }
    
    unsigned int path_size = path.size(); 
//        bool odd_original = false;
    bool odd = false;
    for (;path_size > 0;--path_size){
        if (n%2 == 1){
            odd = true;
        } else {
            odd = false;
        }

        n >>= 1;
        if (!odd && (path_size <= 1 || (path[path_size-2] % 2 == 1))){
            --n;
        }
    }
    cout << "Case #" << "#" << ": odd" <<  odd << "\n";
    if (odd){
        min = n;
        max = n;
    } else {
        min = n;
        max = n+1;        
    }
    
}
void brute_force_bathroom(unsigned long long &inp_max, unsigned long long &inp_min, const unsigned long long k, const unsigned long long n){

//    debug input
//    cout << "n: "<<n;
//    cout << "\nk: "<<k<<"\n";
    if (n==k){
        inp_max = 0;
        inp_min = 0;
        return;
    }
    unsigned long long btree[1000001];
    btree[0] = n;
    for (int i = 1; i < n*2+3; ++i) // ...initialize it
    {
        btree[i] = 0;
    }
    
    for (int i = 0; i < k; ++i){
        int firstMaxIndex = -1;
        unsigned long long max = 0;
        for (int j = 0; j < n; ++j){
            if (btree[2*j+1] <= 0 && btree[2*j+2] <= 0) {
                if (btree[j] > max){
                    firstMaxIndex = j;
                    max = btree[j];
                }
            } else {
                
            }
        }   
//        if (n==2){
//            cout << "firstMaxIndex: "<<firstMaxIndex;
//            cout << "\nmax: "<<max<<"\n";
//        }
        if (firstMaxIndex >= 0){
            if (max % 2 == 0){
                btree[2*firstMaxIndex+1] = max/2-1;
                btree[2*firstMaxIndex+2] = max/2;
            } else {
                btree[2*firstMaxIndex+1] = max/2;
                btree[2*firstMaxIndex+2] = max/2;            
            }
        }
        if (i == k-1){
            inp_min = btree[2*firstMaxIndex+1] < btree[2*firstMaxIndex+2] ? btree[2*firstMaxIndex+1] : btree[2*firstMaxIndex+2];
            inp_max = btree[2*firstMaxIndex+1] > btree[2*firstMaxIndex+2] ? btree[2*firstMaxIndex+1] : btree[2*firstMaxIndex+2];
        
           
        }
    }
    
}

