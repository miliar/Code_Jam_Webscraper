#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    FILE *fin = freopen("C-small-2-attempt1.in", "r", stdin);
    FILE *fout = freopen("C-small-2.out", "w", stdout);
    unsigned long long int i,j=0,t,n,k,l,r;
    cin>>t;
    while(t--){
        priority_queue<int> spaces;
        j++;
        cin>>n>>k;
        spaces.push(n);
        for(i=1; i<=k; i++){
            n = spaces.top();
            spaces.pop();
            if(n%2 == 0){
                l = (n/2)-1;
                r = n/2;
            } else{
                l = n/2;
                r = l;
            }
            spaces.push(l);
            spaces.push(r);
        }
        cout<<"Case #"<<j<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
    }
    return 0;
}
