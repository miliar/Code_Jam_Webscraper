#include <bits/stdc++.h>
using namespace std;

vector <unsigned long long> possibilities;

int findLevel(unsigned long long k){
	return(log(k)/log(2));
}

unsigned long long lookPosition(int level,unsigned long long k){
	return(k-(unsigned long long)(pow(2, level)));
}

void lookPossibilities(int level, unsigned long long n){
	if(level==0)
		possibilities.push_back(n);
	else{
		unsigned long long l= (unsigned long long)(n/2);
		lookPossibilities(level-1,l);
		unsigned long long r= (unsigned long long)((n-1)/2);
		lookPossibilities(level-1,r);
	}
}

int main(){
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		unsigned long long n,k;
		cin>>n;
		cin>>k;
		cout<<"Case #"<<test<<": ";
		possibilities.clear();

		if(k>= 0.7*n){
			cout<<0<<" "<<0<<endl;
			continue;
		}
		int level= findLevel(k);
		unsigned long long pos= lookPosition(level,k);

		lookPossibilities(level,n);
		sort(possibilities.begin(),possibilities.end(),greater<unsigned long long>());
		unsigned long long emptySequence = possibilities[pos];
		cout<<emptySequence/2<<" ";
		if(emptySequence!=0)
			cout<<(emptySequence-1)/2<<endl;
		else
			cout<<0<<endl;
	}
	return 0;
}
