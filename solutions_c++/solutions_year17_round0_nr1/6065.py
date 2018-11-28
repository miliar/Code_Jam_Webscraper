#include <iostream>
#include <string>
using namespace std;

int T;
int K;
string inp;
int S;

void flip(int index)
{
	for(int i=index;i<K+index;++i){
		if(inp[i] == '-'){
			inp[i] = '+';
		}
		else{
			inp[i] = '-';
		}
	}
}

long long solve()
{
	int val = 0;

	for(int i=0; i<=(S-K); ++i){
		if(inp[i] == '-'){
			flip(i);
			++val;
		}
	}

	int OK = 1;
	for(int i=0; i<S; ++i){
		if(inp[i] =='-'){
			OK = 0;
			break;
		}
	}
	if(OK)
		return val;
	else
		return -1;
}



int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		
		cin>>inp>>K;
		S=inp.size();
		long long ret = solve();
		if(ret<0){
			cout<<"Case #"<<xx<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<xx<<": "<<ret<<endl;
		}
	}
	return 0;
}
