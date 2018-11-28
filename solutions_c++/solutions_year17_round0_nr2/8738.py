#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;


bool istidy(int a){
	
	int z, k = 10;
	
	while(a){
		z = a%10;
		if(z>k)
			return false;
		k = z;
		a/=10;
		
	}
	
	return true;
	
}


int main(){
	freopen ("abbb.in","r",stdin);
	freopen ("myff","w",stdout);
	int i,q,k,t,j,l;
	
	cin>>t;
	string c, x;
	for(q = 1; q<=t; q++){
		
		int rr;
		
		cin>>k;
		
		for(i = 1; i <=k; i ++)
			if(istidy(i))
				rr=i;
		
		cout<<"Case #"<<q<<": "<<rr<<endl;
		
	}
	
	
	
	return 0;
	
}
