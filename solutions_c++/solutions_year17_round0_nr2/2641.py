#include <iostream>
#include <string>


using namespace std;
int main() {
	freopen ("output1.txt","w",stdout);
	freopen ("B-large.txt","r",stdin);
	int t;
	cin >> t;
	string s[t];
	int n[19];
	for(int i=0;i<t;i++){
		cin>>s[i];
	}
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<19;j++){
			n[j]=0;
		}
		for(int j=0;j<s[i].length();j++){
			n[19-s[i].length()+j]=int(s[i][j]-'0');
		}
		bool first=false;
		int find=0;
		for(int j=0;j<19;j++){
			if(!first && n[j]==0){
				continue;
			}else{
				if(!first){
					first=true;
					find=j;
				}
				bool fgood=true;
				int r=j;
				while(fgood){
					if(r==19){
						break;
					}
					if(n[j]>n[r]){
						fgood=false;
						break;
					}
					if(n[j]<n[r]){
						break;
					}
					r++;
				}
				if(fgood){
					cout<<n[j];
				}else{
					if(n[j]==1 && j==find){
						for(int r=j+1;r<19;r++){
							cout<<9;
						}
						break;
					}
					if(n[j]>0){
						cout<<n[j]-1;
						for(int r=j+1;r<19;r++){
							cout<<9;
						}
						break;
					}
				}
			}
		}
		cout<<endl;
		
	}
	return 0;
}
