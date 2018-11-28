//#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<assert.h>

using namespace std;

ifstream cin("/Users/naginahas/Downloads/C-Large.in");
ofstream cout("/Users/naginahas/Downloads/Ctttt.txt");

long long solve(long long N,long long K ){
    map <long long, long long> mp;
    long long cur = N;
    mp[cur] = 1;
    while(cur>1){
        cur = (cur-1)/2;
        long long a=0 ,b=0;
        if(mp.count(2*cur+1) !=0) a = mp[2*cur+1];
        if(mp.count(2*cur+2)!=0) b = mp[2*cur+2];
        
        mp[cur] = 2*a + b;
        a = b = 0;
        long long cur2 = cur+1;
        if(mp.count(2*cur2+1) !=0) a = mp[2*cur2+1];
        if(mp.count(2*cur2)!=0) b = mp[2*cur2];
        mp[cur2] = 2*a + b;
        //check special case of interaval of length 1 or avoid it

    }
    long long sum =0;
    long long length = -1;
    while(sum<K){
        length = (*mp.rbegin()).first;
        if(length ==1) break;
        sum +=mp.rbegin()->second;
        mp.erase(length);
        
    }
    return length;
    
    
    
    
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    long long N,K;
    for(int t=0;t<T;t++){
        cin >> N >> K;
        long long z = solve(N,K);
        cout << "Case #" << t+1 << ": " << z/2 << " " << (z-1)/2 << endl;
        
    }

    return 0;
}
