#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>
#include <sstream>

using namespace std;

long long i,j,k;

#define fi(a,b) for(i=a;i<b;i++)
#define fj(a,b) for(j=a;j<b;j++)
#define fk(a,b) for(k=a;k<b;k++)
#define fr(a,b,c) for(i=a;i<b;i+=c);
#define rf(a,b,c) for(i=a;i>b;i-=c);
#define pb(a) push_back(a);

string to_string(long long i){ //my compiler doesn't include to_string for some reason...
	ostringstream s;
	s << i;
	return s.str();
}

string solve(long long p,long long s){
	
	long long t1 = (s-1)/2;
	long long t2 = s/2;
	
	if (p==1){
		
		return (to_string(t2) + " " + to_string(t1));
	}
	
	else if (p % 2 == 0){
		return solve(p/2,t2);
	} else {
		return solve(p/2,t1);
	}
}

int main(){
	
	long long t;
	long long p,s;
	
	cin>> t;
	
	for(i=0;i<t;i++){
		
		cin >> s >> p;
		
		cout << "Case #" << i+1 << ": ";
		cout << solve(p,s) << endl;
	}
	
	return 0;
}