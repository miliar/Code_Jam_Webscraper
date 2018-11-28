#include<bits/stdc++.h>
using namespace std;
#define endl '\n'

int main(){
//	ios_base::sync_with_stdio(0);cin.tie(NULL);
	int t,r,c,x,y,x1,x2,y1,y2,z,l,i,j,i1,j1;
	char c1;
	queue<int> X, Y;
	queue<char> CH;
	cin>>t;
	for(l=1; l<=t; l++){
		cin>>r>>c;
		cout<<"Case #"<<l<<":"<<endl;
		string cad[r];
		for(i=0; i<r; i++){
			cin>>cad[i];
		}
		for(i=0; i<r; i++){
			for(j=0; j<c; j++){
				if(cad[i][j]!='?'){
					X.push(j);
					Y.push(i);
					CH.push(cad[i][j]);
				}
			}
		}
		while(!X.empty()){
			x= X.front();
			y= Y.front();
			c1= CH.front();
			X.pop();
			Y.pop();
			CH.pop();
			x1=0;
			for(j=x-1; j>=0; j--){
				if(cad[y][j]!='?'){
					x1= j+1;
					break;
				}
			}
			x2=c-1;
			for(j=x+1; j<c; j++){
				if(cad[y][j]!='?'){
					x2= j-1;
					break;
				}
			}
			y1=0;
			for(i=y-1; i>=0; i--){
				for(j=x1; j<=x2; j++){
					if(cad[i][j]!='?')
					break;
				}
				if(j<=x2){
					y1= i+1;
					break;
				}
			}
			y2=r-1;
			for(i=y+1; i<r; i++){
				for(j=x1; j<=x2; j++){
					if(cad[i][j]!='?')
					break;
				}
				if(j<=x2){
					y2= i-1;
					break;
				}
			}
			for(i=y1; i<=y2; i++){
				for(j=x1; j<=x2; j++){
					cad[i][j]= c1;
				}
			}
		}
		for(i=0; i<r; i++){
			for(j=0; j<c; j++){
				cout<<cad[i][j];
			}
			cout<<endl;
		}
	}
}
