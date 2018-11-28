#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("a.out");

int ca=0;

void doit(){
	int n,m;
	cin>>n>>m;
	char a[n][m];
		int cou = 0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>a[i][j];
			if(a[i][j]!='?'){
				cou++;
			}
		}
	}
	while(cou != n*m){
		//up
		for(int k=0;k<n;k++)
		for(int i=1;i<n;i++){
			for(int j=0;j<m;j++){
				if((a[i][j]!='?')&&(a[i-1][j]=='?')){
				//	cout<<"one over "<<i<<" "<<j<<endl;
					a[i-1][j] = a[i][j];
					cou++;
				}
			}
		}
		//down
				for(int k=0;k<n;k++)
		for(int i=0;i<n-1;i++){
			for(int j=0;j<m;j++){
				if((a[i][j]!='?')&&(a[i+1][j]=='?')){
					//					cout<<"one under "<<i<<" "<<j<<endl;
					a[i+1][j] = a[i][j];
					cou++;
				}
			}
		}
		//left
				for(int k=0;k<n;k++)
		for(int i=0;i<n;i++){
			for(int j=1;j<m;j++){
				if((a[i][j]!='?')&&(a[i][j-1]=='?')){
					//					cout<<"one left of "<<i<<" "<<j<<endl;
					a[i][j-1] = a[i][j];
					cou++;
				}
			}
		}
		//right
				for(int k=0;k<n;k++)
		for(int i=0;i<n;i++){
			for(int j=0;j<m-1;j++){
				if((a[i][j]!='?')&&(a[i][j+1]=='?')){
					//					cout<<"one right "<<i<<" "<<j<<endl;
					a[i][j+1] = a[i][j];
					cou++;
				}
			}
		}
	}
	ca++;
	cout<<"Case #" << ca << ":"<<endl;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<a[i][j];
		}
		cout<<endl;
	}
}

int main(){
	int t;
	cin>>t;
	while(t--){
		doit();		
	}
}
