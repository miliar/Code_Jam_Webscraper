#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;
struct three_int{
	int a,b,c;
};


int main(){
	
	freopen("C-small-1-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin>>tt;

	for (int ttt=0; ttt<tt; ttt++){	
		int n,k;
		cin>>n>>k;

		int a[n+2]={0},b[n+2];
		for (int i=0; i<n+2; i++) b[i]=-1;
		a[0]=1; a[n+1]=1;
		b[0]=n+1;

		three_int abc;

		for (int i=0; i<k; i++){
			vector<three_int> x;
			int aa=0;
			//if (b[aa]-aa == 1) continue;
			while(true){
				if (b[aa]-aa==1) {aa++; continue;}
				int bb = 0.5*(b[aa]+aa);
				int final = floor(bb);
				three_int solution;
				solution.a = final;
				solution.b = final-aa;
				solution.c = b[aa]-final;
				x.push_back(solution);
				aa=b[aa];
				if (b[aa]==-1) break;
			}

			vector<three_int> y;
			int maxim = 0;
			for (int j=0; j<x.size(); j++){
				maxim = max(maxim,min(x[j].b,x[j].c)); 	
			}

			for (int j=0; j<x.size(); j++){
				if (min(x[j].b,x[j].c) == maxim) y.push_back(x[j]); 	
			}

			vector<three_int> z;
			int maxim1 = 0;
			for (int j=0; j<y.size(); j++){
				maxim1 = max(maxim1,max(y[j].b,y[j].c)); 	
			}

			for (int j=0; j<y.size(); j++){
				if (max(y[j].b,y[j].c) == maxim1) z.push_back(y[j]); 	
			}
			abc=z[0];
			a[z[0].a]=1;
			b[z[0].a]=z[0].a + z[0].c;
			b[z[0].a - z[0].b] = z[0].a;
		}

		cout<<"Case #"<<ttt+1<<": "<<max(abc.b,abc.c)-1<<" "<<min(abc.b,abc.c)-1<<endl;
	}
	return 0;
}