#include <iostream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char** argv){
    int ncases;
    cin >> ncases >> ws;
    for(int c=0; c<ncases; c++){
        int s, p;
        cin >> s >> ws >> p >> ws;
        int rr, ll;
        priority_queue<int> q;
        q.push(s);
        for(; p >0; p--){
            int f = q.top();
            q.pop();
            int l = f/2 - (f%2 == 0);
            int r = f/2;
            q.push(l);
            q.push(r);  
            rr = max(l,r);
            ll = min(l,r);
        }
        cout << "Case #" << c + 1 << ": " << rr << " " << ll << " " << endl;
    }
    return 0;
}