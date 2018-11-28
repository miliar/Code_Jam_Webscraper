#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,c=1;
    long long n,i,j,x,z,y,k;
    cin>>t;
    while(t>0)
    {
        cout<<"Case #"<<c<<": ";
        ++c;
        set<long long> s;
        set<long long>::reverse_iterator it;
        set<long long>::iterator it2;
        cin>>n>>k;
        long long hash[1000001];
        for(i=0;i<1000001;++i)
        hash[i]=0;

            s.insert(n);
            ++hash[n];
            while(k>1)
            {
                it=s.rbegin();
                s.insert((*it)/2);
                ++hash[(*it)/2];
                s.insert(*it-(*it)/2-1);
                ++hash[*it-(*it)/2-1];
                --hash[*it];
                if(hash[*it]==0)
                s.erase(*it);
                --k;
            }
            it=s.rbegin();
            x=(*it)/2;
            y=*it-(*it)/2-1;
            cout<<x<<" "<<y<<endl;

        
        --t;
    }
	return 0;
}

