#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int i,t,j,k,w,l;
    long long int n,tmp,L,R,ma,mi;
	cin>>t;
	for(j=1;j<=t;j++){
	    cin>>n>>k;
	    typedef vector<int> vec;
	    typedef vec::iterator it;
	    vec s;
	    it m,ip;
	    s.push_back(-1);
	    s.push_back(n);
	    s.push_back(-1);
	    l=-2;
	    while(k--){
	        m=max_element(s.begin(),s.end());
            w=distance(s.begin(),m);
            tmp=*m;
	        s.erase(s.begin()+w);
	        s.insert(s.begin()+w,tmp/2);
	        s.insert(s.begin()+w,l--);
	        s.insert(s.begin()+w,(tmp-1)/2);
	    }
	    
	        m=min_element(s.begin(),s.end());
            w=distance(s.begin(),m);
            L=R=0;
            i=w-1;
            while(s[i]>=0){
                L+=s[i];
                i--;
            }
            i=w+1;
            while(s[i]>=0){
                R+=s[i];
                i++;
            }
            if(L>R){
            ma=L;
            mi=R;
            }
            else{
                ma=R;
                mi=L;
            }
            cout<<"Case #"<<j<<": "<<ma<<" "<<mi<<endl;
	}
	return 0;
}
