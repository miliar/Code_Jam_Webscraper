#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	long long n,k;
	cin>>t;
	for (int i = 1; i <= t; ++i){
		cin>>n>>k;
		long long cnt = 0LL;
		long long x,y,izq, der;
		map<long long,long long, greater<long long> > M;
		M[n] = 1LL;
		bool FLAG = 0;
		while(!FLAG){
			 long long sum = 0LL;
			 for(auto X: M){
			 	sum += X.second;
			 }
		     if(k <= cnt + sum){
		     	for(auto X: M){
		     	    x = X.first;
		     	    y = X.second;
		     	    if(k <= cnt+y){
		     	      	if(x&1){
		     	   	        der = izq = x/2;
		     	        }else{
		     	   	      izq = (x-1)/2;
		     	   	      der = x/2;
		     	        }
		     	        FLAG = 1;
		     	        break;
		     	    }else cnt += y;
		     	}
		     }else{
		     	map<long long, long long> M1;
		     	for(auto X: M){
		     		x = X.first;
		     		y = X.second;
		     		cnt += y;
		     		if(x&1){
		     		   	 M1[x/2] += 2LL*y;
		     		}else{
		     		   	 M1[x/2] += y;
		     		   	 M1[(x-1LL)/2] += y;
		     		}
		     	}
		     	M.clear();
		     	for(auto X: M1){
		     		M.insert(X);
		     		x = X.first;
		     		y = X.second;
		     	}
		     }
		}
		cout<<"Case #"<<i<<": "<<der<<" "<<izq<<endl;
	}

}