#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <bitset>
#define ull unsigned long long
#define ll long long
#define inf 10000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;


int main(int argc, char *argv[]){
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/in.txt");
    output.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/out.txt");
    
    int tests;
    input>>tests;
    
    priority_queue<ll, vector<ll>, less<ll>> pq;
    ll stalls, people, minn, maxx;
    
    for (int test=1;test<=tests;test++){
        output<<"Case #"<<test<<": ";
        while (pq.size()){
            pq.pop();
        }
        input>>stalls>>people;
        pq.push(stalls);
        for (int i=0;i<people;i++){
            stalls = pq.top()-1;
            pq.pop();
            minn = stalls/2;
            maxx = minn + (stalls % 2);
            if (minn) pq.push(minn);
            if (maxx) pq.push(maxx);
        }
        output<<maxx<<" "<<minn;
        
        output<<"\n";
    }
    
    return 0;
}
