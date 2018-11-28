#include<bits/stdc++.h>
using namespace std;
void execute()
{
	string S;
	vector<char> digit;
	cin>>S;
	for(int i=0; i+1<S.size(); i++)
		if(S[i]>S[i+1])
		{
			// decrease at i by 1
			// might cause further problems
			// so
			S[i]--;
			while(i && S[i] < S[i-1])
			{
				i--;
				S[i]--;
			}
			for(int j=i+1; j<S.size(); j++) S[j] = '9';
			break;
		}
	int i=0;
	while(S[i]=='0') i++;
	for(; i<S.size(); i++) printf("%c",S[i]); printf("\n");
}
int main()
{
	freopen("B.inp","r",stdin);
	freopen("B.out","w",stdout);
	int test;
	scanf("%d", &test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
