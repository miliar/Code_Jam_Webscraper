#include <bits/stdc++.h>
using namespace std;

int t,n,r,o,y,g,b,v,caso,x,erro;

int main(){
	cin >> t;
	caso=1;
	while(t--){
		vector <char> s;
		erro=0;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if((r+y<b) || (r+b<y) || (b+y<r)){
			printf("Case #%d: IMPOSSIBLE\n",caso);
			caso++;
		}
		else{
			if(r>=b and b>=y){
				x=r-b;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('R');
					s.push_back('Y');
				}
				for(int i=0;i<y-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<b-y;i++){
					s.push_back('R');
					s.push_back('B');
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
			else if(r>=y and y>=b){
				x=r-y;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('R');
					s.push_back('Y');
				}
				for(int i=0;i<b-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<y-b;i++){
					s.push_back('R');
					s.push_back('Y');
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
			else if(y>=r and r>=b){
				x=y-r;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('Y');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<b-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<r-b;i++){
					s.push_back('R');
					s.push_back('Y');
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
			else if(y>=b and b>=r){
				x=y-b;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('Y');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<r-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<b-r;i++){
					s.push_back('B');
					s.push_back('Y');
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
			else if(b>=r and r>=y){
				x=b-r;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
					s.push_back('B');
				}
				for(int i=0;i<y-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
				}
				for(int i=0;i<r-y;i++){
					s.push_back('R');
					s.push_back('B');
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
			else if(b>=y and y>=r){
				x=b-y;
				for(int i=0;i<x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
					s.push_back('B');
				}
				for(int i=0;i<r-x;i++){
					s.push_back('R');
					s.push_back('B');
					s.push_back('Y');
					erro=1;
				}
				for(int i=0;i<y-r;i++){
					if(erro){
						s.push_back('B');
						s.push_back('Y');
					}
					else {
						s.push_back('Y');
						s.push_back('B');

					}
				}
				printf("Case #%d: ",caso);
				for(int i=0;i<n;i++) printf("%c",s[i]);
				printf("\n");
				caso++;
			}
		}
	}
}
