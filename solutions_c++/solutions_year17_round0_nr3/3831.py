#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int T; cin>>T;
    for(int t=1; t<=T; ++t) {
        int n, k; cin>>n>>k;
        priority_queue<int> q;
        q.push(n);
        int x, y;
        while (k--) {
            int p=q.top();
            q.pop();
            if (p%2==0) {
                x=p/2;
                y=p/2-1;
            }
            else {
                x=y=p/2;
            }
            q.push(x);
            q.push(y);
        }
        cout<<"Case #"<<t<<": "<<x<<" "<<y<<"\n";
    }
}
