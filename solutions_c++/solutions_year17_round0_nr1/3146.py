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
#define mp make_pair
#define pii std::pair<int, int>
using std::cin;
using std::cout;



int main(){
    //freopen("small_input.txt", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("A-large_output.txt", "wt", stdout);
    int T,k,res;
    std::string pancake;

    bool exist=0;

    cin>>T;
    int pos;
    forn(i,T){
        res=0;
        pos=1;
        cin>>pancake>>k;
        forn(j,pancake.length()){
            if(pancake[j]=='-'){
                if(j+k>pancake.length()){
                    pos=0;
                    break;
                }
                res++;
                for(int ii=j;ii<j+k;++ii)
                    pancake[ii]= pancake[ii] == '-' ? '+' : '-';
            }
        }
        if(pos){
           cout<<"Case #"<<i+1<<": "<<res<<"\n" ;
        }else{
           cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
        }

    }

    return 0;
}
