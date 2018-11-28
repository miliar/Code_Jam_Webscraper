
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>

#define ll long long

using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		int r,c;
		cin>>r>>c;
		char arr[30][30];
		for (int i=0;i<r;i++){
			cin>>arr[i];
		}

		int done[26]={0};

		
		for (int j=0;j<c;j++){
			for (int i=0;i<r;i++){
				
				if (arr[i][j]=='?'){
					continue;
				}

				char ch=arr[i][j];
				if (done[ch-'A']==1){
					continue;
				}
				
				done[ch-'A']=1;
				
				int u,d,l;
				u=i-1;
				while (u>=0){
					if (arr[u][j]!='?'){
						break;
					}
					u--;
				}
				u++;
				d=i+1;
				while (d<r){
					if (arr[d][j]!='?'){
						break;
					}
					d++;
				}
				d--;
				l=j-1;
				while (l>=0){
					if (arr[i][l]!='?'){
						break;
					}
					l--;
				}
				l++;
				//cout<<"hello"<<u<<l<<d<<i<<j<<endl;


				for (int x=u;x<=d;x++){
					for (int y=l;y<=j;y++){
						arr[x][y]=ch;
					}
				}

				

				


			}
		}
		
				
		int i=0;

		for (i=0;i<c;i++){
			if (arr[0][i]=='?'){
				break;
				
			}
			
		}
		if (i!=c){
			while (i!=c){
				
				
				
				for (int j=0;j<r;j++){
					char def='A';
					if (i>0){
						def=arr[j][i-1];
					}
					arr[j][i]=def;

				}
				i++;
			}
		}
		cout<<endl;
		for (int i=0;i<r;i++){
			for (int j=0;j<c;j++){
				cout<<arr[i][j];
			}
			cout<<endl;
		}
		// My code

		

	}
	
	return 0;
}
