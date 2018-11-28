#include<iostream>
#include<string>
#include<queue>
#include<stdio.h>
using namespace std;

typedef struct elem{
	string state;
	long long moves;
	long long flip_pos;
} element;

long long get_id(element e){
	long long id=0;
	long long p=1;
	for(size_t i=0;i<e.state.size();++i){
		if(e.state[i]=='+')
			id+=p;
		p=p*2;
	}
	return id;
}

bool is_happy(element e){
	bool happy=true;
	for(size_t i=0;i<e.state.size() && happy;++i)
		happy=(e.state[i]=='+');

	return happy;
}

element flip(element e, size_t pos, long long K){
	element n;
	n.state.assign(e.state);
	n.moves = e.moves+1;
	n.flip_pos=pos+1;

	for(size_t i=pos;i<pos+K;++i){
		if(n.state[i]=='-')
			n.state[i]='+';
		else
			n.state[i]='-';
	}
	return n;
}

int main(){
  long long t,T,ans;
	string S;
	long long K;
  cin >> T;
  for(t=1;t<=T;++t){
		cin >> S;
		cin >> K;
		queue<element> q;

		element e;
		e.state.assign(S);
		e.moves=0;
		e.flip_pos=0;

		q.push(e);
		ans=-1;
		while(!q.empty()){
			e = q.front();
			q.pop();
			if(is_happy(e)){
				ans=e.moves;
				break;
			}
			bool all_positive=true;
			for(size_t i=0;i<e.flip_pos && all_positive;++i){
				all_positive=e.state[i]=='+';
			}
			for(size_t i=e.flip_pos;i<=e.state.size()-K && all_positive;++i){
				element n = flip(e,i,K);
				q.push(n);
			}
		}
		if(ans>=0)
			cout << "Case #"<<t<<": "<<ans<<endl;
		else
			cout << "Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	return 1;
}

