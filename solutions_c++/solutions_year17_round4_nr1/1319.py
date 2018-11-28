#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>
#define VS vector<string>
#define VVS vector<VS>

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/round2/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/round2/A_output2.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		int N,P;
		cin>>N>>P;
		int ans = 0;
		VI a(4,0);
		for(int i=0;i<N;i++){
			int x;
			cin>>x;
			a[x%P]++;
		}
		if(P == 2){
			ans = a[0] + (a[1]+1)/2;
		}
		else if(P == 3){
			ans = a[0];
			while(a[1] > 0 and a[2] > 0){
				ans++;
				a[1]--; a[2]--;
			}
			int tmp = a[1] + a[2];
			ans += (tmp+2)/3;
		}
		else{
			ans = a[0];
			while(a[1] > 0 and a[3] > 0){
				ans++;
				a[1]--; a[3]--;
			}
			while(a[2] > 1){
				ans++;
				a[2] -= 2;
			}

			int idx;
			if(a[1] == 0)
				idx = 3;
			else
				idx = 1;

			if(a[2] == 0){
				ans += (a[idx] + 3)/4;
			}
			else{
				if(a[idx] >= 2){
					ans += 1 + (a[idx]+1)/4;
				}
				else{
					ans += 1;
				}
			}
		}
		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}

	return 0;
}
