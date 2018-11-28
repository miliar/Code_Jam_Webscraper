#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int r,c;cin>>r>>c;
		vector<string> grid(r);
		for(auto& x: grid) cin>>x;
		for(int i=0;i<r;i++){
			char current='?';
			for(int j=0;j<c;j++){
				if(grid[i][j]!='?') current=grid[i][j];
				else if(current!='?') grid[i][j]=current;
			}
			current='?';
			for(int j=c-1;j>=0;j--){
				if(grid[i][j]!='?') current=grid[i][j];
				else if(current!='?') grid[i][j]=current;
			}
			if(grid[i][0]=='?' && i>0 && grid[i-1][0]!='?'){
				for(int j=0;j<c;j++) grid[i][j]=grid[i-1][j];
			}
		}
		for(int i=r-1;i>=0;i--){
			if(grid[i][0]=='?' && i<r-1 && grid[i+1][0]!='?'){
				for(int j=0;j<c;j++) grid[i][j]=grid[i+1][j];
			}
		}
		cout<<"Case #"<<t<<":"<<endl;
		for(const auto& x: grid) cout<<x<<endl;
	}
	return 0;
}