#include <bits/stdc++.h>
#define PB push_back
using namespace std;

vector<long long> x(1,0);
int it=0;
const long long max_num=100000000000000000;

int main()
{
    while(it<x.size()) {
        long long akt=x[it];
        it++;
        for(long long j=akt%10;j<10;j++) {
            if(akt*10+j>0 && akt<max_num) {
                x.PB(akt*10+j);
            }
        }
    }
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=0;tc<t;tc++) {
        long long n;
        cin>>n;
        int b1=0;
        int b2=x.size()-1;
        while(b1!=b2) {
            int mid=(b1+b2+1)/2;
            if(x[mid]<=n) {
                b1=mid;
            }
            else {
                b2=mid-1;
            }
        }
        cout<<"Case #"<<tc+1<<": "<<x[b1]<<endl;
    }
    return 0;
}
