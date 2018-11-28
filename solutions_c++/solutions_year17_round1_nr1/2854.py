#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
#define ull unsigned long long
#define lll long long
char arr[100][100];
int nana[100];
int r,c;

int sol(int pos,int que){
	if(que==0){
//		cout<<"hehe";
		return 1;
	}
	if(pos>=r*c){
		return 0;
	}
	int x=pos/c;
	int y=pos%c;
	for(int k=0;x+k<r;k++){
		for(int l=0;y+l<c;l++){
			int cou=0,a,b;
			char ch;
			for(int i=x;i<=x+k;i++){
					for(int j=y;j<=y+l;j++){
							if(arr[i][j]!='?'){
								cou++;
								a=i;
								b=j;
								ch=arr[i][j];
							}
					}
			}
			if(cou!=1 || nana[ch-'A']>1){
				continue;
			}
			for(int i=x;i<=x+k;i++){
				for(int j=y;j<=y+l;j++){
					arr[i][j]=ch;
					nana[ch-'A']++;
					que--;
				}
			}
			que++;
			nana[ch-'A']--;
//			cout<<"got "<<pos<<" "<<ch<<" "<<x<<" "<<y<<" "<<k<<endl;
//			for(int i=0;i<r;i++){
//				for(int j=0;j<c;j++){
//					cout<<arr[i][j];
//				}cout<<endl;
//			}cout<<endl;
			if(sol(pos+1,que)){
				return true;
			}
			nana[ch-'A']++;
			for(int i=x;i<=x+k;i++){
				for(int j=y;j<=y+l;j++){
					arr[i][j]='?';
					nana[ch-'A']--;
					que++;
				}
			}
			que--;
			arr[a][b]=ch;
		}
	}
	return sol(pos+1,que);
}

void solve(int test_case_no){
	cin>>r>>c;
	for(int i=0;i<100;i++){
		nana[i]=0;
	}
	int que=0;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cin>>arr[i][j];
			if(arr[i][j]!='?'){
				nana[arr[i][j]-'A']++;
			}
			else{
				que++;
			}
		}
	}
	sol(0,que);
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cout<<arr[i][j];
		}
		cout<<endl;
	}
}

int main(){
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		cout<<"Case #"<<tt<<": "<<endl;
		solve(tt);
	}
	return 0;
}
