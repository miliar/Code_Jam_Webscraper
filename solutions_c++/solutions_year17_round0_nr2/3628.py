/*
 * Ernest van Wijland
 * C++/C++11
*/
#include <bits/stdc++.h>
using namespace std;

bool tidy(long long N) {
    vector<int> l;
    vector<int> m;
    while(N) {
        l.insert(l.begin(),N%10);
        m.insert(m.begin(),N%10);
        N/=10;
    }
    sort(m.begin(),m.end());
    for(int i=0;i<(int)l.size();i++)
        if(m[i]!=l[i])
            return false;
    return true;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        long long N;
        cin>>N;
        while(!tidy(N))
            N--;
        cout<<"Case #"<<t<<": "<<N<<'\n';
    }
    
    return 0;
}
