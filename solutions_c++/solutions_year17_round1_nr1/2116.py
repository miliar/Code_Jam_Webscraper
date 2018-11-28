#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long
int main() {
	// your code goes here
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	lld test,t,n,i,j,k,r,c;
	string str;
	cin>>test;
	for(t=1;t<=test;t++){
        cin>>r>>c;
        cout<<"Case #"<<t<<":"<<endl;

        char grid[r+1][c+1];
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                cin>>grid[i][j];
            }
        }

        for(j=0;j<c;j++){
              //  cout<<j<<endl;
                char ch=' ';
                lld cq=0;
                for(i=0;i<r;i++){
                    if(grid[i][j]!='?'){
                        ch=grid[i][j];
                        for(k=i-1;k>=0;k--){
                            if(grid[k][j]=='?'){
                                grid[k][j]=ch;
                            }
                            else{
                                break;
                            }
                        }
                    }
                    else{
                        cq++;
                        if(ch!=' '){
                            grid[i][j]=ch;
                         //   cout<<"hell";
                        }
                        if(cq==r&&j!=0){
                            if(grid[i][j-1]!='?'){
                                for(k=0;k<r;k++){
                                    grid[k][j]=grid[k][j-1];
                                }
                            }
                        }
                    }
                }

        }


        for(j=c-1;j>=0;j--){
                char ch=' ';
                lld cq=0;
                for(i=0;i<r;i++){
                    if(grid[i][j]!='?'){
                        ch=grid[i][j];
                        for(k=i-1;k>=0;k--){
                            if(grid[k][j]=='?'){
                                grid[k][j]=ch;
                            }
                            else{
                                break;
                            }
                        }
                    }
                    else{
                        cq++;
                        if(ch!=' '){
                            grid[i][j]=ch;
                        }
                        if(cq==r){
                            if(grid[i][j+1]!='?'){
                                for(k=0;k<r;k++){
                                    grid[k][j]=grid[k][j+1];
                                }
                            }
                        }
                    }
                }
        }

        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                cout<<grid[i][j];
            }
            cout<<endl;
        }

	}
	return 0;
}
