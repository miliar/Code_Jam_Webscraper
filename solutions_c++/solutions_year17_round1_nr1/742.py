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
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/1a/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/1a/A_output2.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		int R,C;
		cin>>R>>C;
		string* a = new string[R];
		for(int i=0;i<R;i++){
			cin>>a[i];
		}

		bool vis[26];
		for(int i=0;i<26;i++)
			vis[i] = 0;

		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(a[i][j] != '?' and vis[a[i][j]-'A'] == false){
					int ell = j-1;
					while(ell >= 0 and a[i][ell] == '?')
						ell--;
					ell++;
					int arr = j+1;
					while(arr < C and a[i][arr] == '?')
						arr++;
					arr--;

					int up = i-1;
					while(up >= 0){
						bool good = true;
						for(int k = ell; k <= arr; k++){
							if(a[up][k] != '?'){
								good = false;
								break;
							}
						}
						if(good)
							up--;
						else
							break;
					}
					up++;

					int down = i+1;
					while(down < R){
						bool good = true;
						for(int k = ell; k <= arr; k++){
							if(a[down][k] != '?'){
								good = false;
								break;
							}
						}
						if(good)
							down++;
						else
							break;
					}
					down--;

					//printf("left = %d right = %d up = %d down = %d\n", ell, arr, up, down);
					for(int x = up; x <= down; x++){
						for(int y = ell; y <= arr; y++){
							a[x][y] = a[i][j];
						}
					}
					vis[a[i][j] - 'A'] = true;
				}
			}
		}
		cout<<"Case #"<<casenum<<":"<<endl;
		for(int i=0;i<R;i++)
			cout<<a[i]<<endl;
	}

	return 0;
}
