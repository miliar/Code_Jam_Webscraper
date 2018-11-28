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
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/A_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		string a;
		int K;
		cin>>a>>K;
		int L = a.size();
        int flips = 0;
		int i = 0;
		while(i <= L-K){
			if(a[i] == '+'){
				i++;
			}
			else{
				flips++;
				for(int j=i;j<i+K;j++){
					if(a[j] == '+')
						a[j] = '-';
					else
						a[j] = '+';
				}
			}
		}
		bool done = true;
		for(int j=L-K+1;j<L;j++){
			if(a[j] == '-')
				done = false;
		}
		if(done)
			cout<<"Case #"<<casenum<<": "<<flips<<endl;
		else
			cout<<"Case #"<<casenum<<": IMPOSSIBLE"<<endl;
	}

	return 0;
}
