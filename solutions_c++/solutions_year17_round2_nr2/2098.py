#include<bits/stdc++.h>
using namespace std;

int main()
{
     freopen("input.in","r",stdin);
freopen("output_file_name.out","w",stdout);
	int t,n,man=0,r;
	int o,y,g;
	int b,v,x;
	cin>>t;
	while(t--){
	man++;
			cin>>n>>r>>o>>y>>g>>b>>v;
			cout<<"Case #"<<man<<": ";
		x=max(max(r,y),b);
		if(x==r){
			if(x>y+b){
				cout<<"IMPOSSIBLE";
			}
			else {
				while(x!=(y+b)){
					if(y>b){
						cout<<"R"<<"Y"<<"B";
					}
					else{
						cout<<"R"<<"B"<<"Y";
					}
					y--;
					b--;
					x--;
				}
				while(y!=0){
					cout<<"R"<<"Y";
					y--;
				}
				while(b!=0){
					cout<<"R"<<"B";
					b--;
				}
			}
		}
		}
		cout<<endl;

	}

}
