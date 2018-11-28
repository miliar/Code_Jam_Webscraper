#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

int nc, nj;
pair<int, int> ac[201];
pair<int, int> aj[201];

#define DAY_L (60*24)

char day[DAY_L];

bool comp(pair<int,int> a, pair<int, int> b) {
    return a.second-a.first < b.second-b.first;
}

int main()
{
    int t;
    cin >> t;
    for(int caso=1; caso<=t; caso++) {
        cin >> nc >> nj;
        for(int i=0; i<DAY_L; i++) day[i] = '?';
        int totc=0, totj=0;
        for(int i=0; i<nc; i++) {
            cin >> ac[i].first >> ac[i].second;
            totc += ac[i].second - ac[i].first;
            for(int j=ac[i].first; j<ac[i].second; j++) day[j] = 'c';
        }
        for(int i=0; i<nj; i++) {
            cin >> aj[i].first >> aj[i].second;
            totj += aj[i].second - aj[i].first;
            for(int j=aj[i].first; j<aj[i].second; j++) day[j] = 'j';
        }
        
        cout << "Case #" << caso << ": ";
        
        if(!nc && !nj) {
            cout << 2 << endl;
            continue;
        }
        // cout << "alskdjalsjd\n";
    
    
        sort(ac, ac+nc);
        sort(aj, aj+nj);
        // cout << "alskdjalsjd\n";
        
        vector< pair<int,int> > bc;
        vector< pair<int,int> > bj;
        
        for(int i=0; i<nc; i++) {
            bc.push_back(make_pair(ac[i].second, ac[(i+1)%nc].first));
        }
        for(int i=0; i<nj; i++) {
            bj.push_back(make_pair(aj[i].second, aj[(i+1)%nj].first));
        }
        sort(bc.begin(), bc.end(), comp);
        sort(bj.begin(), bj.end(), comp);
        
        
        // vector< pair<int,int> > b;
        // char chosen;
        // int budget;
        // if(nc > nj) {
        //     chosen = 'c';
        //     budget = 720-totc;
        //     for(int i=0; i<=nc; i++) {
        //         b.push_back(make_pair(ac[i].second, ac[(i+1)%nc].first));
        //     }
        // } else {
        //     chosen = 'j';
        //     budget = 720-totj;
        //     for(int i=0; i<=nj; i++) {
        //         b.push_back(make_pair(aj[i].second, aj[(i+1)%nj].first));
        //     }
        // }
        // sort(b.begin(), b.end(), comp);

        // Case C
        int budgetc = 720-totc;
        for(int i=0; i<bc.size(); i++) {
            int start = bc[i].first;
            int end = bc[i].second;
            int duration = (end > start) ? (end-start) : (end+DAY_L-start);
            if(duration == 0) continue;
            // if(duration > budgetc) break;
            bool ok=true;
            for(int j=0; j<duration; j++) {
                if(day[(start+j)%DAY_L] == 'j') {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                if(budgetc >= duration) {
                    budgetc -= duration;
                    for(int j=0; j<duration; j++) day[(start+j)%DAY_L] = 'c';
                } else {
                    day[start%DAY_L] = 'j'; // at least one exchange
                }
            }
        }
        
        // Case J
        int budgetj = 720-totj;
        for(int i=0; i<bj.size(); i++) {
            int start = bj[i].first;
            int end = bj[i].second;
            int duration = (end > start) ? (end-start) : (end+DAY_L-start);
            if(duration == 0) continue;
            // if(duration > budgetj) break;
            bool ok=true;
            for(int j=0; j<duration; j++) {
                if(day[(start+j)%DAY_L] == 'c') {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                if(budgetj >= duration) {
                    budgetj -= duration;
                    for(int j=0; j<duration; j++) day[(start+j)%DAY_L] = 'j';
                } else {
                    day[start%DAY_L] = 'c'; // at least one exchange
                }
            }
        }
        
        
        char first = '?';
        char current = '?';
        int res = 0;
        for(int i=0; i<DAY_L; i++) {
            if(current == '?' && day[i] != '?') {
                current = day[i];
                first = day[i];
            } else if(day[i] != '?' && current != day[i]) {
                current = day[i];
                res++;
            }
        }
        if(current != first) res++;
        
        cout << res << endl;
    }
}
