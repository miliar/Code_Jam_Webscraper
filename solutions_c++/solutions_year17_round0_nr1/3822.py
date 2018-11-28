#include <iostream>
#include <string>
using namespace std;
void solve()
{
	string S;
	cin >> S;
	int K;
	cin >> K ;
	int var=0;
	for(int i=0;i<S.length()-K+1;i++)
	{
		if(S[i]=='-' && ++var)
			for(int j=i;j<i+K;j++)
				S[j]=((S[j]=='-')?'+':'-');
	}
	for(int j=S.length()-K+1;j<S.length();j++)
	{
		if(S[j]=='-')
		{
			cout << "IMPOSSIBLE" << endl; 
			return ;
		}
	}
	cout << var << endl ;
	
}
int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}