#include <iostream>
#include <string>

using namespace std;
int main() {
	freopen ("output.txt","w",stdout);
	freopen ("A-large.txt","r",stdin);
	int t;
	cin >> t;
	int r[t];
	int c[t];
	for (int i = 0;i<t;i++) {
		cin >> r[i]>>c[i];
		char cake[r[i]][c[i]];
		char ans[r[i]][c[i]];
		bool empt[r[i]];
		for(int ir=0;ir<r[i];ir++){
			for(int ic=0;ic<c[i];ic++){
				cin>>cake[ir][ic];
			}
		}
		
		for(int ir=0;ir<r[i];ir++){
			bool empt=false;
			for(int ic=0;ic<c[i];ic++){
				if(cake[ir][ic]=='?' && !empt){
					ans[ir][ic]='?';
					continue;
				}
				if(cake[ir][ic]!='?' && !empt){
					empt=true;
					for(int icc=0;icc<=ic;icc++){
						ans[ir][icc]=cake[ir][ic];
					}
				}else{
					if(cake[ir][ic]=='?' && empt){
						ans[ir][ic]=ans[ir][ic-1];
					}
					if(cake[ir][ic]!='?' && empt){
						ans[ir][ic]=cake[ir][ic];
					}
				}
			}
		}
		

		
		for(int ic=0;ic<c[i];ic++){
			bool empt2=false;
			for(int ir=0;ir<r[i];ir++){
				if(ans[ir][ic]!='?' && !empt2){
					empt2=true;
					for(int irr=0;irr<=ir;irr++){
						ans[irr][ic]=ans[ir][ic];
					}
				}else{
				
					if(ans[ir][ic]=='?' && empt2){
						ans[ir][ic]=ans[ir-1][ic];
					}
				}
				
			}
		}
		
		cout<<"Case #"<<i+1<<":"<<endl;
		for(int ir=0;ir<r[i];ir++){
			for(int ic=0;ic<c[i];ic++){
				cout<<ans[ir][ic];
			}
			cout<<endl;
		}
	}
	
	return 0;
}
