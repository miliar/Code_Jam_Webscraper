#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main() {
    ifstream infile("C-small-2-attempt0.in");
    ofstream outfile("C-small-2-attempt0.out");

    int T;
    infile>>T;
    for(int t=1;t<=T;++t){
        long long int n, k;
        infile>>n>>k;
        priority_queue<long long int> q;
        q.push(n);
        while(--k){
            long long int x = q.top();
            if(x==1) break;
            q.pop();
            if(x&1){
                q.push(x/2);
                q.push(x/2);
            }
            else{
                q.push(x/2);
                q.push(x/2-1);
            }
        }
        long long int x = q.top();
        if(x==1){
            outfile<<"Case #"<<t<<": "<<0<<' '<<0<<endl;
        }
        else{
            if(x&1) outfile<<"Case #"<<t<<": "<<x/2<<' '<<x/2<<endl;
            else outfile<<"Case #"<<t<<": "<<x/2<<' '<<x/2-1<<endl;
        }
    }

    infile.close();
    outfile.close();
    return 0;
}