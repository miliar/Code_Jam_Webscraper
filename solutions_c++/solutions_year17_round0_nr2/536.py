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

LL ones[20];

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/B_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/B_output2.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	ones[1] = 1;
	for(int i=2;i<=18;i++)
		ones[i] = 10LL * ones[i-1] + 1LL;

	for(int casenum=1;casenum<=cases;casenum++){
		LL N;
		cin>>N;

		int bumps = 0;
        LL res = 0LL;
        for(int i=18;i>=1 and bumps < 9;i--){
			while(ones[i] <= N){
				res += ones[i];
				N -= ones[i];
				bumps++;
				if(bumps == 9)
					break;
			}
		}
		cout<<"Case #"<<casenum<<": "<<res<<endl;
	}

	return 0;
}
