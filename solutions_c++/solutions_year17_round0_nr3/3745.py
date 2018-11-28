/*
 * Ernest van Wijland
 * C++/C++11
*/
#include <bits/stdc++.h>
using namespace std;

int T;

int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        int N,K;
        scanf("%d%d",&N,&K);
        priority_queue<int> inter;
        inter.push(N);
        for(int k=0;k<K;k++) {
            int cur=inter.top();
            //cout<<cur<<endl;
            inter.pop();
            int ls,rs;
            if(cur%2==0) {
                ls=cur/2 - 1;
                rs=cur/2;
            }
            else {
                ls=cur/2;
                rs=cur/2;
            }
            if(ls)
                inter.push(ls);
            if(rs)
                inter.push(rs);
            if(k==K-1)
                cout<<"Case #"<<t<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<'\n';
        }
    }
    
    return 0;
}

































