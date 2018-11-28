/*input
1
6 1 0 2 0 3 0
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	ifstream cin("B-small-attempt10.in");
	ofstream cout("B-small-output-attempt10.txt");
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		int i, n, r, o, y, g, b, v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		char ans[n];
		if(r>n/2 || y>n/2 || b>n/2){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(n==1){
			if(r==1){
				cout<<"R"<<endl;
			}
			else if(y==1){
				cout<<"Y"<<endl;
			}
			else
				cout<<"B"<<endl;
			continue;
		}
		
		if(!r || !y || !b){
			if(y==0){
				for(i=0;i<n;i++){
					if(i&1)
						cout<<'R';
					else
						cout<<'B';
				}		
			}
			else if(r==0){
				for(i=0;i<n;i++){
					if(i&1)
						cout<<'Y';
					else
						cout<<'B';
				}
			}
			else{
				for(i=0;i<n;i++){
					if(i&1)
						cout<<'R';
					else
						cout<<'Y';
				}
			}
			cout<<endl;
		}

		else{
			string helik="";
			if(r==max(r,max(y,b))){
				helik = helik + "R";
				r--;
			}
			else if(y==max(y,max(r,b))){
				helik = helik + "Y";
				y--;
			}
			else{
				helik = helik + "B";
				b--;
			}
			for(i=1;i<n;i++){
				if(r==max(r,max(y,b))){
					if(helik[helik.size()-1]=='R'){
						if(y>b){
							helik += 'Y';
							y--;
						}
						else{
							helik += 'B';
							b--;
						}
					}
					else{
						helik = helik + "R";
						r--;
					}
				}
				else if(y==max(r,max(y,b))){
					if(helik[helik.size()-1]=='Y'){
						if(r>b){
							helik += 'R';
							r--;
						}
						else{
							helik += 'B';
							b--;
						}
					}
					else{
						helik = helik + "Y";
						y--;
					}
				}
				else{
					if(helik[helik.size()-1]=='B'){
						if(r>y){
							helik += 'R';
							r--;
						}
						else{
							helik += 'Y';
							y--;
						}
					}
					else{
						helik = helik + "B";
						b--;
					}
				}
			}
			if(helik[0]==helik[helik.size()-1]){
				swap(helik[helik.size()-2],helik[helik.size()-1]);
			}
			if(helik[0]==helik[helik.size()-1]){
				// swap(helik[helik.size()-2],helik[helik.size()-1]);
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			cout<<helik<<endl;
		}

	}
	return 0;
}