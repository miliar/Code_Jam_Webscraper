#include <bits/stdc++.h>
using namespace std;
typedef long long ull;

ull mx, mn;
void solve(ull k, priority_queue<ull> &queue) {
    int i=0;
    for(; i<k; i++) {
        if(queue.size() == 0) {
            mx=mn=0;
            break;
        }
        ull n = queue.top();
        queue.pop();
        if(n%2==1) {
            mx=mn=n/2;
            if(mx!=0) queue.push(mx);
            if(mn!=0) queue.push(mn);
        } else {
            mx = n/2;
            mn = n/2-1;
            if(mx!=0) queue.push(mx);
            if(mn!=0) queue.push(mn);
        }
    }
}

int main(int argc, char *argv[])
{
    int Q;
    ifstream infile;
    ofstream outfile;
    infile.open("C-small-2-attempt0.in");
    outfile.open("output.txt");
    infile>>Q;
    for(int i=1;i<=Q;i++) {
        ull n,k;
        infile>>n>>k;
        mx=mn=0;
        priority_queue<ull> queue;
        queue.push(n);
        solve(k, queue);
        outfile<<"Case #"<<i<<": "<<mx<<" "<<mn<<endl;
    }

    return 0;
}
