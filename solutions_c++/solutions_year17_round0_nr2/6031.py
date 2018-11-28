#include <iostream>
#include <string>
using namespace std;

int T;
int K;
string inp;
int S;


string solve()
{
	string inp_bkp = inp;
	bool firstUntidyOver=false;
	int firstUntidyIndex = -1;
	for(int i=0; i<S-1; ++i){
		if(inp[i] > inp[i+1]){
			//detected first untidy
			firstUntidyOver = true;
			firstUntidyIndex = i;
			for(int j=i+1; j<S; ++j){
				inp[j] = '9';
			}
			inp[i] -= 1;
			break;
		}
	}

	if(firstUntidyOver){
		for(int i=firstUntidyIndex; i>0; --i){
			if(inp[i-1] > inp[i]){
				inp[i] = '9';
				inp[i-1] -= 1;
			}
			else{
				break;
			}
		}
	}

	for(int i=0;i<S;++i){
		if(inp[i] != '0'){
			return inp.substr(i);
		}
	}
	return inp;
}



int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		
		cin>>inp;
		S=inp.size();
		string ret = solve();
		cout<<"Case #"<<xx<<": "<<ret<<endl;
	}
	return 0;
}
