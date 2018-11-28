#include<bits/stdc++.h>

using namespace std;

string S;
int N;

int main()
{
	int testN;

	cin >> testN;

	for(int test=1; test<=testN; test++)
	{
		cout << "Case #" << test << ": ";

		cin >> S;
		N = S.size();

		int cur = 0;

		while(cur<N-1 && S[cur]<=S[cur+1]) 
			cur++;

		if(cur==N-1)
		{
			cout << S << endl;
			continue;
		}

		while(cur>0 && S[cur] == S[cur-1])
			cur--;

		S[cur]--;
	
		for(int i=cur+1; i<N; i++)
			S[i] = '9';


		for(int i=(S[0]=='0'); i<N; i++)
			cout << S[i];

		cout << endl;
	}
}
