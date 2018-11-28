#include <iostream>
#include <string>
#include <sstream>

using namespace std;


int main(int argc, char** argv) {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,j;
	cin>>T;
	for(j=1;j<=T;j++)
	{
	string S,D="-+"; int K=0,M,L;
	cin>>S>>M;
	int i,N=S.size();
	for(i=0;i+M<=N;i++)
		{
		 if(S[i]=='+')continue;
		 K++;
		 for(L=0;L<M;L++)
		 	S[i+L]=D[S[i+L]=='-'];
		}
	cout<<"Case #"<<j<<": ";
	if(S!=string(N,'+'))cout<<"IMPOSSIBLE"<<endl; else
	cout<<K<<endl;
	}
	
	return 0;
}
