#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl '\n'
typedef long long ll;
using namespace std;

int main(){
	// ios_base::sync_with_stdio(false);
	// cin.tie(0);
	int T;
	cin>>T;
	for (int tc=0; tc<T; tc++){
		int R,C;
		cin>>R>>C;
		vector<string>grid(R);
		for (int i = 0; i < R; ++i)
		{
			cin>>grid[i];
		}
		for (int x=0; x<R; x++){
			for (int y=0; y<C; y++){
				if (grid[x][y]!='?'){
					char c=grid[x][y];
					int cy=y-1;
					while(cy>=0){
						if (grid[x][cy]=='?')
							grid[x][cy]=c;
						else
							break;
						cy--;
					}
					cy=y+1;
					while(cy<C){
						if (grid[x][cy]=='?')
							grid[x][cy]=c;
						else{
							y=cy-1;
							break;
						}
						cy++;
					}
				}
			}
		}
		// for (int i = 0; i < R; ++i)
		// {
		// 	cout<<grid[i]<<endl;
		// }
		for (int x=0; x<R-1; x++){
			int ind=x+1;
			if (grid[x][0]=='?'){
				while(grid[ind][0]=='?'){
					ind++;
					if (ind>=R)
						break;
				}
				if (ind>=R)
					break;
				for (int t=x; t<ind; t++){
					for (int y=0; y<C; y++){
						grid[t][y]=grid[ind][y];
					}
				}
			}
		}
		for (int x=R-1; x>0; x--){
			int ind=x-1;
			if (grid[x][0]=='?'){
				while(grid[ind][0]=='?'){
					ind--;
					if (ind<0)
						break;
				}
				if (ind<0)
					break;
				for (int t=ind+1; t<=x; t++){
					for (int y=0; y<C; y++){
						grid[t][y]=grid[ind][y];
					}
				}
			}
		}
		cout<<"Case #"<<tc+1<<": "<<endl;
		for (int i = 0; i < R; ++i)
		{
			cout<<grid[i]<<endl;
		}
	}
}