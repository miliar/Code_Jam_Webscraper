#include<iostream>
#include <limits>
#include <algorithm>
#include<vector>
#include<iomanip>
#include<string>
#include<unordered_map>
#include<stack>
#include <queue>
#include <deque>
#include <chrono>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <random>
#define forn(i,n) for(int i=0;i<n;++i)
#define mp std::make_pair
#define pii std::pair<int, int>
#define pll std::pair<long long, long long>
using std::cin;
using std::cout;



int main(){
    //freopen("A.in", "rt", stdin);
    int T;
    cin>>T;
    int D,N;
    forn(k,T){
        cin>>D>>N;
        std::vector<pii > horses(N);
        forn(i,N){
            cin>>horses[i].first>>horses[i].second;
        }
        std::sort(horses.rbegin(),horses.rend());
        double time;
        forn(t,N){
            if(t-1>=0){
                if(horses[t].second<=horses[t-1].second){
                    time=((double)(D-horses[t].first))/(horses[t].second);
                }else{
                   double tim = ((double)(D-horses[t].first))/(horses[t].second);
                   if(tim>=time){
                        time=tim;
                   }
                }
            }else{
                time=((double)(D-horses[t].first))/(horses[t].second);
            }
        }

        cout<<"Case #"<<k+1<<": ";
        cout<<std::setprecision(8)<<D/time<<"\n";
    }
    return 0;
}
