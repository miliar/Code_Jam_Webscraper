#include <iostream>
#include <string>
using namespace std;


void Flip(string &S, int beg, int K){
	for (int i = beg; i < beg+K; i++)	S[i] = ( S[i]=='-' )? '+' : '-' ;
}

int greedyFlip(string& S, int K){
	int res=0;

	for (int i = 0; i < S.size()-K+1; i++)
	{
		if(S[i]=='-'){
			Flip(S,i,K);
			res++;
		}
	}

	for(int i = S.size()-K+1; i < S.size();i++)
		if(S[i]=='-') res = -1;

	return res;
}
int main(){
	int T,K;
	string S;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin>>S>>K;
		int aux =greedyFlip(S,K);
		cout << "Case #"<<i+1<<": ";
		if( aux == -1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<aux<<endl;
	}
	return 0;
}