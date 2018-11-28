#include <iostream>
#include <string>
using namespace std;
int solve()
{

	string S;
	cin >> S;
	int j=1000;
	for(int i=0;i<S.length()-1;i++)
	{
		if(S[i]>S[i+1])
		{
			S[i]--;
			j=i+1;
			break;
			
		}
	}
	for(int k=j;k<S.length();k++)
		S[k]='9';
	--j;
	while(j>0&& j<S.length())
	{
		if(S[j]<S[j-1])
			S[j]='9',S[--j]--;
		else break;
	}
	long long Z=0;
	for(int i=0;i<S.length();i++)
		Z=Z*10+(S[i]-'0');
	cout << Z << endl ;
	return Z;
}
int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}
