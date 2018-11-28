#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

//Source: stackoverflow

int solve(vector<int> bits, int N) {
	queue<int> flips;
	int moves = 0;

	for (int i = 0; i < bits.size(); ++i) {
		if (!flips.empty() && flips.front() <= i - N)
			flips.pop();

		if ((bits[i] ^ (flips.size() % 2 == 0)) == 1) {
			if (i > bits.size() - N)
				return -1;

			moves++;
			flips.push(i);
		}
	}

	return moves;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++) {
		string S;
		int K;
		cin>>S>>K;
		int len = S.length();
		int a[len];
		for(int i = 0; i < len; i++)
			a[i] = S[i] == '+' ? 1 : 0;


		vector<int> bits(a, a + sizeof(a) / sizeof(a[0]));
		//cout<<bits.size()<<endl;

		// for(int i = 0; i < bits.size(); i++) {
		// 	cout<<bits[i]<<" ";
		// }
		// cout<<endl;

		int ans = solve(bits, K);

		if(ans!=-1)
		cout<<"Case #"<<t<<": "<<ans<<endl;
		else
		cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
