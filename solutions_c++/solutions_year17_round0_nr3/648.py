#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;

int main() {
    long cases;
    ifstream in("bathroomstalls.in");
    ofstream out("bathroomstalls.out");
    in >> cases;
    
    for(long q=1; q<=cases; q++){
        map<long long, long long> mymap;
        priority_queue<long long> pq;
        long long n;
        long long k;
        in >> n >> k;
        mymap[n] = 1LL;
        pq.push(n);
        while(true){
            long long now = pq.top();
            pq.pop();
            long long val = mymap[now];
            if(val>=k){
                now--;
                long long mini = now/2LL;
                long long maxi = now/2LL + now%2LL;
                out << "Case #" << q << ": " << maxi << " " << mini << endl;
                break;
            }
            k-=val;
            now--;
            long long a = now/2LL;
            long long b = now/2LL + now%2LL;
            if(mymap.count(a)==0){
                mymap[a] = 0LL;
                pq.push(a);
            }
            if(mymap.count(b)==0){
                mymap[b] = 0LL;
                pq.push(b);
            }
            mymap[a] = mymap[a] + val;
            mymap[b] = mymap[b] + val;
        }
    }
    
    return 0;
}