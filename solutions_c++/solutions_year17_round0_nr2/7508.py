#include <iostream>
#include <string>
#include <sstream>

using namespace std;

unsigned long long LtoS(string x)
{
 stringstream SS(x);
 unsigned long long P;
 SS>>P;
 return P;
}

int main(int argc, char** argv) {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,j;
	cin>>T;
	for(j=1;j<=T;j++)
	{
	string S;
	cin>>S;
	int i,N=S.size();
	for(i=N-2;i>=0;i--)
	if(S[i]>S[i+1]){
		S[i]--; S=S.substr(0,i+1)+string(N-i-1,'9');
			}
	cout<<"Case #"<<j<<": ";
	cout<<LtoS(S)<<endl;
	}
	
	return 0;
}
