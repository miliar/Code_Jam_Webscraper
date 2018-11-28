#include <iostream>
#include <algorithm>    // std::sort
#include <vector>
#include <map>
using namespace std;
bool myfunction(int i,int j){
    return(i>j);
}
int main() {
	// your code goes here
	
	int test;
	cin>>test;
	for(int t = 1;t<=test;t++){
	    long long n,k;
	    cin>>n>>k;
	    vector<long long> dat;
	    map<long long,long long> ct_map;
	    ct_map[n] = 1;
	    dat.push_back(n);
	    int st = 0;
	    long long ct = 0;
	    long long ans = -1;
	    while(true){
	        int t_st = dat.size();
	        for(int i=st;i<t_st;i++){
	            
	            long long val = dat[i];
	            long long add_ct = ct_map[val];
	            //cout<<dat[i]<<" "<<add_ct<<" ";
	            if((ct+add_ct)>=k){
	                ans = val;
	                break;
	            }else{
	                ct += add_ct;
	            }
	            int l_s = val/2;
	            int r_s = val/2;
	            if(val%2==0){
	                l_s--;
	            }
	            if(ct_map.find(l_s) == ct_map.end()){
	                ct_map[l_s] = ct_map[val]; 
	                dat.push_back(l_s);
	            }else{
	                ct_map[l_s] += ct_map[val];
	            }
	            if(ct_map.find(r_s) == ct_map.end()){
	                ct_map[r_s] = ct_map[val];
	                dat.push_back(r_s);
	            }else{
	                ct_map[r_s] += ct_map[val];
	            }
	            
	        }
	        //cout<<endl;
	        if(ans!=-1)
	            break;
	        sort (dat.begin()+t_st, dat.end(), myfunction);
	        st = t_st;
	    }
	    int left = ans/2;
	    int right = ans/2;
	    if(ans%2==0){
	        left --;
	    }
	    cout<<"Case #"<<t<<": "<<right<<" "<<left<<endl; 
	}
	return 0;
}
