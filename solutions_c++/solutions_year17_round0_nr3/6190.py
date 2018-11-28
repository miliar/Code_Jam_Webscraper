#include <bits/stdc++.h>
using namespace std;

vector <unsigned long long> possibilities;

int findLevel(unsigned long long k){
	return(log(k)/log(2));
}

unsigned long long findPosition(int level,unsigned long long k){
	return(k-(unsigned long long)(pow(2, level)));
}

void findPossibilities(int level, unsigned long long n){
	if(level==0)
		possibilities.push_back(n);
	else{
		unsigned long long l= (unsigned long long)(n/2);
		findPossibilities(level-1,l);
		unsigned long long r= (unsigned long long)((n-1)/2);
		findPossibilities(level-1,r);
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
//		possibilities.push_back(n);
		if(k>= 0.7*n){
			cout<<0<<" "<<0<<endl;
			continue;
		}
		int level= findLevel(k);
		unsigned long long position= findPosition(level,k);
//		cout<<"L: "<<level<<" "<<position;
		findPossibilities(level,n);
		sort(possibilities.begin(),possibilities.end(),greater<unsigned long long>());
		unsigned long long emptySequence = possibilities[position];
		cout<<emptySequence/2<<" ";
		if(emptySequence!=0)
			cout<<(emptySequence-1)/2<<endl;
		else
			cout<<0<<endl;
	}
	return 0;
}
