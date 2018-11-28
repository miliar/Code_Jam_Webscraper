#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
# define M_PI           3.14159265358979323846  /* pi */
int main(){
    	int T;
    	cin>>T;
    	for(int cases=1;cases<=T;cases++){
    		ll N,K;
    		cin>>N>>K;
    		vector<pair<double ,pair<long long ,long long > > > v;
    		for(int i=0;i<N;i++){
    			ll h,r;
    			cin>>r>>h;
    			v.push_back(make_pair(r*h,make_pair(r,h)));
    			}
    		double tans = -1;
    		for(int j=0;j<N;j++){
  
	    		double ans = M_PI*v[j].second.first*v[j].second.first+2*M_PI*v[j].second.first*v[j].second.second;
	    		vector<pair<long long ,pair<long long ,long long > > > vn;
	    		for(int i=0;i<v.size();i++){
	    			if(i==j)continue;
	    			ll h,r;
	    			h = v[i].second.second;
	    			r = v[i].second.first;
	    			vn.push_back(make_pair(h*r,make_pair(r,h)));
	    		}
	    		sort(vn.begin(),vn.end());
	    		reverse(vn.begin(),vn.end());
	    		long long arsum=0;
	    		for(int i=0;i<K-1;i++){
	    			arsum+=vn[i].first;
	    		}
	    		ans+=2*M_PI*arsum;
	    		tans=max(ans,tans);
    		}
    		
    		cout<<fixed<<setprecision(10);
    		cout<<"Case #"<<cases<<": "<<tans<<endl;
    	


    	}

		
	    
        return 0;
}