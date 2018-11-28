#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
char G[50][50];
char G2[50][50];
int R,C;
void cp2(){
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			G[i][j]=G2[i][j];
		}
	}
}
void cp(){
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			G2[i][j]=G[i][j];
		}
	}
}
void pr(){
	cout << endl;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cout << G[i][j];
		}
		if(i!=R-1)
		cout << endl;
	}
}
void main2(){
	cin >> R >> C;
	int mnI[256];
	int mxI[256];
	int mnJ[256];
	int mxJ[256];
	for(int i=0;i<256;i++){
		mnI[i]=mnJ[i]=100;
		mxI[i]=mxJ[i]=-100;
	}
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cin >> G[i][j];
			char c = G[i][j];
			if(c=='?')continue;
			mnI[c]=min(mnI[c],i);
			mnJ[c]=min(mnJ[c],j);
			mxI[c]=max(mxI[c],i);
			mxJ[c]=max(mxJ[c],j);
		}
	}
	for(int k='A';k<='Z';k++){
		if(mnI[k]==100)continue;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(mnI[k] <= i && i <= mxI[k] && mnJ[k] <= j && j <= mxJ[k]){
					G[i][j]=k;
				}
			}
		}
	}
	cp();
	// pr();
	for(int k=0;k<3;k++){
		for(int i=1;i<R;i++){
			set<char> notOK;
			for(int j=0;j<C;j++){
				if(G2[i-1][j]=='?')continue;
				G2[i][j]=G2[i-1][j];
				if(G[i][j]!='?'){
					notOK.insert(G2[i-1][j]);
				}
			}
			for(int j=0;j<C;j++){
				if(notOK.find(G2[i][j])!=notOK.end())continue;
				G[i][j]=G2[i][j];
			}
			cp();
		}
		for(int i=R-2;i>=0;i--){
			set<char> notOK;
			for(int j=0;j<C;j++){
				if(G2[i+1][j]=='?')continue;
				G2[i][j]=G2[i+1][j];
				if(G[i][j]!='?'){
					notOK.insert(G2[i+1][j]);
				}
			}
			for(int j=0;j<C;j++){
				if(notOK.find(G2[i][j])!=notOK.end())continue;
				G[i][j]=G2[i][j];
			}
			cp();
		}
		for(int j=1;j<C;j++){
			set<char> notOK;
			for(int i=0;i<R;i++){
				if(G2[i][j-1]=='?')continue;
				G2[i][j]=G2[i][j-1];
				if(G[i][j]!='?'){
					notOK.insert(G2[i][j-1]);
				}
			}
			for(int i=0;i<R;i++){
				if(notOK.find(G2[i][j])!=notOK.end())continue;
				G[i][j]=G2[i][j];
			}
			cp();
		}
		for(int j=C-2;j>=0;j--){
			set<char> notOK;
			for(int i=0;i<R;i++){
				if(G2[i][j+1]=='?')continue;
				G2[i][j]=G2[i][j+1];
				if(G[i][j]!='?'){
					notOK.insert(G2[i][j+1]);
				}
			}
			for(int i=0;i<R;i++){
				if(notOK.find(G2[i][j])!=notOK.end())continue;
				G[i][j]=G2[i][j];
			}
			cp();
		}
	}
	pr();
}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}

