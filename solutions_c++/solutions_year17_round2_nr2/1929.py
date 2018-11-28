//
//  main.cpp
//  googlecodejam2017
//
//  Created by Yoshioka Tsuneo on 2017/04/08.
//  Copyright © 2017年 Yoshioka Tsuneo. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <sstream>
#include <queue>
#include <stdexcept>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cassert>
#include <unistd.h>
#include <string.h>

#include <stack>
#include <iterator>

// #define MULTI_THREAD

#ifdef MULTI_THREAD
#include <thread>
#endif

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

#define EPS 0.000001
using namespace std;

typedef long long ll;


string testcase_itr(int N, int R, int O, int Y, int G, int B, int V)
{
    // solution start
    string result;
    vector<int> ryb = {R, Y, B};
    vector<int> ogv = {O, G, V};
    vector<char> rybchars = {'R', 'Y', 'B'};
    vector<char> ogvchars = {'O', 'G', 'V'};


    int i =0;
    int prevrybc = -1;
    int firstrybc = -1;
    while(i<N){
        int rybc = (int)distance(ryb.begin(), max_element(ryb.begin(), ryb.end()));
        if(ryb[rybc] ==0){
            return "";
        }
        if(prevrybc == 0){
            if(ryb[1] > ryb[2]){
                rybc = 1;
            }else if(ryb[1] == ryb[2] && firstrybc == 1){
                rybc = 1;
            }else{
                rybc = 2;
            }
        }
        if(prevrybc == 1){
            if(ryb[2] > ryb[0]){
                rybc = 2;
            }else if(ryb[2] == ryb[0] && firstrybc == 2){
                rybc = 2;
            }else{
                rybc = 0;
            }
        }
        if(prevrybc == 2){
            if(ryb[0] > ryb[1]){
                rybc = 0;
            }else if(ryb[0] == ryb[1] && firstrybc == 0){
                rybc = 0;
            }else{
                rybc = 1;
            }
        }
        if(ryb[rybc] ==0){
            return "";
        }
        if(i==0){
            firstrybc = rybc;
        }
        result.push_back(rybchars[rybc]);
        ryb[rybc]--;
        i++;
        prevrybc = rybc;
        
        int ogvc = (rybc + 1) % 3;
        while(ogv[ogvc] > 0){
            result.push_back(ogvchars[ogvc]);
            ogv[ogvc]--;
            i++;
            if(i==N){
                break;
            }
            if(ryb[rybc] == 0){
                return "";
            }
            result.push_back(rybchars[rybc]);
            ryb[rybc]--;
            i++;
            if(i==N){
                break;
            }
        }
    }
    if(result[0] == result.back()){
        return "";
    }
    if(result[0] == 'R' && (result.back() == 'O' || result.back() == 'V')){
        return "";
    }
    if(result[0] == 'Y' && (result.back() == 'G' || result.back() == 'O')){
        return "";
    }
    if(result[0] == 'B' && (result.back() == 'V' || result.back() == 'G')){
        return "";
    }
    
    
    // solution end
    
    return result;
}
void testcase(istream &in)
{
    int T;
    in >> T;
    for(int i=0;i<T;i++){
        int N, R, O, Y, G, B, V;
        in >> N >> R >> O >> Y >> G >> B >> V;
        auto ret = testcase_itr(N, R, O, Y, G, B, V);
        if(ret == ""){
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
            
        }else{
            cout << "Case #" << i+1 << ": " << ret << endl;
        }
    }
}

#ifdef MULTI_THREAD
void testcase_multi(istream &in);
#endif

int main(int argc, const char * argv[])
{
    // sleep(1000);
    // insert code here...
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    string fname = "/dev/stdin";
    if(argc>=2){
        fname = argv[1];
        ifstream in(fname, ifstream::in);
        if(!in){
            cout << "File open error:" << fname << endl;
            exit(1);
        }
#ifdef MULTI_THREAD
        testcase_multi(in);
#else
        testcase(in);
#endif
        /*
         int result = testcase(in);
         cout << result << endl;
         */
    }else{
#ifdef MULTI_THREAD
        testcase_multi(cin);
#else
        testcase(cin);
#endif
        /*
         int result = testcase(cin);
         cout << result << endl;
         */
        
    }
    return 0;
}

#ifdef MULTI_THREAD
class semaphore{
private:
    mutex mtx;
    condition_variable cv;
    int count;
    
public:
    semaphore(int count_ = 0):count(count_){;}
    void notify()
    {
        unique_lock<mutex> lck(mtx);
        ++count;
        cv.notify_one();
    }
    void wait()
    {
        unique_lock<mutex> lck(mtx);
        
        while(count == 0){
            cv.wait(lck);
        }
        count--;
    }
};
semaphore sem(6);
vector< pair<bool, double> > g_results;

void testcase_for_multithread(int t, int M, int N, vector<string> X)
{
    g_results[t].second = testcase_itr(C, F, X);
    g_results[t].first = true;
    // sleep(rand()/(RAND_MAX/3.0));
    sem.notify();
}

void testcase_multi(istream &in)
{
    int T;
    in >> T;
    
    vector<thread> threads;
    g_results.resize(T);
    int cur_result = 0;
    for(int t=0;t<T;t++){
        sem.wait();
        while(g_results[cur_result].first == true){
            cout << "Case #" << cur_result+1 << ": " << g_results[cur_result].second << endl;
            cur_result++;
        }
        
        int M, N;
        in >> M >> N;
        vector<string> ma;
        for(int i=0;i<M;i++){
            string line;
            in >> line;
            ma.push_back(line);
        }
        threads.push_back(thread(testcase_for_multithread, t, M, N, ma ));
        
    }
    while(cur_result<T){
        sem.wait();
        while(g_results[cur_result].first == true){
            cout << "Case #" << cur_result+1 << ": " << g_results[cur_result].second << endl;
            cur_result ++;
        }
    }
    for(int t=0;t<T;t++){
        threads[t].join();
    }
    
}
#endif

