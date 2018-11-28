#include <iostream>
#include <map>
using namespace std;

typedef  long long int typ;

int onecase()
{
	map<typ, typ> data;
	data.clear();
	
	typ K,N;
	cin>>N>>K;
	//cerr<<"Input:"<<N<<":"<<K<<endl;

	data[N]=1;
	typ rspace=-1;
	typ lspace=-1;

	while(K>0){
		pair<typ,typ> ptr=*data.rbegin();
		typ maxsp=ptr.first;
		typ krep=ptr.second;
		data.erase(maxsp);


		maxsp-=1;
		rspace=maxsp/2;
		lspace=maxsp-rspace;

		data[rspace]=data[rspace]+krep;
		data[lspace]=data[lspace]+krep;
		
		K-=krep;
		//cerr<<"Minus:"<<krep<<" remaining:"<<K<<endl;
	}
	cout<<lspace<<" "<<rspace<<endl;

	return 0;
	/*
	priority_queue<unsigned long long int> q;

	unsigned long long int K,N;
	cin>>N>>K;
	q.push(N);

	for(int i=0;i<K-1;i++){
		unsigned long long int space=q.top(); q.pop();
		space-=1;
		unsigned long long int rspace=space/2;
		q.push(rspace);
		q.push(space-rspace);
	}
	//last seq
	unsigned long long int lastspace=q.top();
	lastspace-=1;
	unsigned long long int rspace=lastspace/2;
	unsigned long long int lspace=lastspace-rspace;
	cout<<lspace<<" "<<rspace<<endl;

	return 0;*/
}

int main(){
	//onecase();return 0;
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cerr<<"Case:"<<t<<endl;
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}