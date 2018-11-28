#include<bits/stdc++.h>
using namespace std;

int main()
{
    fstream input("tidynumbers.txt",std::ios_base::in);
    ofstream output;
    output.open("output2.txt");
    int T;input>>T;
    for(int t=0;t<T;t++)
    {
        priority_queue<int> q;
        int n,k;input>>n>>k;
        q.push(n);
        for(int i=0;i<k-1;i++)
        {
            int t=q.top();
            t--;
            q.pop();
            q.push(t/2);
            q.push(t-t/2);
        }
        int val=q.top();val--;
        output<<"Case #"<<t+1<<": "<<val-val/2<<" "<<val/2<<"\n";
    }
}
