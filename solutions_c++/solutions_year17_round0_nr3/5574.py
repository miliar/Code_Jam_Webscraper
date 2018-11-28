#include <iostream>
#include <queue>
using namespace std;

int main() {

    int t;
    cin>>t;
    for(int iteration=1; iteration<=t;iteration++)
    {
        int n, first=0,second=0;
        int k;
        cin>>n;
        cin>>k;
        std::priority_queue<int> q;
        q.push(n);
        
        for(int i=0;i<k;i++)
        {
            
            first = q.top()/2;
            second= q.top()-first-1;
            q.pop();
            q.push(second);
            q.push(first);
        }
        cout<<"Case #"<<iteration<<": ";
        cout<<std::max(first,second)<<" "<<std::min(first,second)<<"\n";
    }

	return 0;
}
