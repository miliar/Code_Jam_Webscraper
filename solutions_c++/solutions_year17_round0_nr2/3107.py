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
    //freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-large.in", "rt", stdin);
    freopen("B-large_output.txt", "wt", stdout);
    int T;
    std::string N;
    cin>>T;
    int wall;
    long long res;

    forn(i,T){
        cin>>N;
       // cout<<N<<std::endl;
        wall=N.length()-1;
        for(int j=N.length()-1;j>=0;j--){
            if(j+1<N.length()){
                if(N[j]>N[j+1]){
                    N[j]=(char)((N[j]-'0')-1 + '0');
                    for(int k=j+1;k<=wall;k++){
                        N[k]='9';
                    }
                    wall=j;
                }
            }
        }
        int k=0;
        while(N.length()>1 && N[k]=='0')k++;
        cout<<"Case #"<<i+1<<": " ;
        cout<<N.substr(k,N.length()-k)<<'\n';
    }

    return 0;
}
