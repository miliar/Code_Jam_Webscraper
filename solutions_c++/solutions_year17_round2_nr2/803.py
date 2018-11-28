
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int no_cases;
int n, r, o, y, g, b, v;
vector<char> ring;

int main(){
	cin>>no_cases;
	for (int caseID=1; caseID<=no_cases; caseID++){
		ring.clear();
		cin>>n>>r>>o>>y>>g>>b>>v;
		//small case o g v =0

		//preprocessing
		b=b-o;
		r=r-g;
		y=y-v;

		//special case
		if (b==0 && o!=0 && r==0 && y==0 && g==0 && v==0){
			cout<<"Case #"<<caseID<<": ";
			for (int i=0; i<o; i++){
				cout<<"BO";
			}
			cout<<endl;
			continue;
		}
		if (b==0 && o==0 && r==0 && y==0 && g!=0 && v==0){
			cout<<"Case #"<<caseID<<": ";
			for (int i=0; i<g; i++){
				cout<<"RG";
			}
			cout<<endl;
			continue;
		}
		if (b==0 && o==0 && r==0 && y==0 && g==0 && v!=0){
			cout<<"Case #"<<caseID<<": ";
			for (int i=0; i<v; i++){
				cout<<"YV";
			}
			cout<<endl;
			continue;
		}

		if (b<0 || r<0 || y<0){
			cout<<"Case #"<<caseID<<": IMPOSSIBLE"<<endl;
			continue;
		}

		if (b==0 && o!=0){
			cout<<"Case #"<<caseID<<": IMPOSSIBLE"<<endl;
			continue;
		}
		if (r==0 && g!=0){
			cout<<"Case #"<<caseID<<": IMPOSSIBLE"<<endl;
			continue;
		}
		if (y==0 && v!=0){
			cout<<"Case #"<<caseID<<": IMPOSSIBLE"<<endl;
			continue;
		}






		int initial=-1;
		//r=1 y=2 b=3
		if (r>=y && r>=b){
			initial=1;
			ring.push_back('R');
			r--;
		}
		else if (y>=r && r>=b){
			initial=2;
			ring.push_back('Y');
			y--;
		}
		else{
			initial=3;
			ring.push_back('B');
			b--;
		}
		bool flag=true;
		while (!(r==0 && y==0 && b==0)){
			if (ring[ring.size()-1]=='R'){
				if (y==0 && b==0){
					flag=false;
					break;
				}
				if (y==b){
					if (initial==3){
						//push_back b
						ring.push_back('B');
						b--;
					}
					else{
						ring.push_back('Y');
						y--;
					}
				}
				else{
					if (y>b){
						ring.push_back('Y');
						y--;
					}
					else{
						ring.push_back('B');
						b--;
					}
				}
			}
			else if (ring[ring.size()-1]=='Y'){
				if (r==0 && b==0){
					flag=false;
					break;
				}
				if (r==b){
					if (initial==3){
						//push_back b
						ring.push_back('B');
						b--;
					}
					else{
						ring.push_back('R');
						r--;
					}
				}
				else{
					if (r>b){
						ring.push_back('R');
						r--;
					}
					else{
						ring.push_back('B');
						b--;
					}
				}

			}
			else{
				if (y==0 && r==0){
					flag=false;
					break;
				}
				if (y==r){
					if (initial==2){
						//push_back y
						ring.push_back('Y');
						y--;
					}
					else{
						ring.push_back('R');
						r--;
					}
				}
				else{
					if (y>r){
						ring.push_back('Y');
						y--;
					}
					else{
						ring.push_back('R');
						r--;
					}
				}

			}
		}
		if (ring[0]==ring[ring.size()-1])
			flag=false;
		if (flag){
			cout<<"Case #"<<caseID<<": ";
			bool flag_o=true, flag_g=true, flag_v=true;
			for (int i=0; i<ring.size(); i++){
				cout<<ring[i];
				if (ring[i]=='B' && flag_o){
					for (int i=0; i<o; i++){
						cout<<"OB";
					}
					flag_o=false;
				}
				if (ring[i]=='R' && flag_g){
					for (int i=0; i<g; i++){
						cout<<"GR";
					}
					flag_g=false;
				}
				if (ring[i]=='Y' && flag_v){
					for (int i=0; i<v; i++){
						cout<<"VY";
					}
					flag_v=false;
				}
			}
			cout<<endl;
		}
		else{
			cout<<"Case #"<<caseID<<": IMPOSSIBLE"<<endl;
		}

	}
}