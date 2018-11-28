#include <iostream>
#include <unordered_map>
#include <queue>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t;
    long int n,k;
    cin>>t;
    for(int tt=1;tt<=t;tt++) {
        cin>>n>>k;
        cout << "Case #"<<tt<<": ";

        priority_queue<long int> pq;
        unordered_map<long int, long int> m;
        pq.push(n);
        m[n]=1;
        long int top, val;
        long int i=0;
        while(i<k-1) {
            if(pq.empty()) break;
            top = pq.top();
            val = m[top];

            i+=val;
            if(i>k-1) break;
            m.erase(top);
            pq.pop();
            
            if(top==1) {
                continue;
            }
            else if(top==0) {
                i--;
                continue;
            }

            long int temp = top/2;
            if(temp!=1) {
                if(m.find(temp)==m.end()) pq.push(temp);
                m[temp]+=val;

                if(top%2==0) {
                    if(m.find(temp-1)==m.end()) pq.push(temp-1);
                    m[temp-1]+=val;
                }
                else {
                    if(m.find(temp)==m.end()) pq.push(temp);
                    m[temp]+=val;
                }
            }
        }

        if(pq.empty()) {cout <<"0 0\n"; continue;}
        top = pq.top();
        
        long int l,r;

        if(top%2==1) { l=top/2; r=top/2; }
        else { r=top/2-1; l=top/2; }
        cout << l << " " << r << "\n";

    }
    return 0;
}
