#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<string>
#include<iomanip>

#define INF 99999999
#define MAXN 1003

using namespace std;

int t;
int n, k;

long double p[MAXN];
long double u;
long double res;

long double eps = 0.000003l;

bool rowne(long double a, long double b){
	if(a < b - eps || a > b + eps)return 0;
	return 1;	
}

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> n >> k;
		
		cin >> u;
		
		for(int i = 0; i < n; i++){
			cin >> p[i];	
		}
		
		sort(p, p + n);
		
		if(n == 1){
			res = min(1.0l, p[0] + u);	
		}
		else{
			while(u > eps){
	//			cout << "u: "<<u<<endl;
	/*			cout<<"p:";
				for(int i = 0; i < n; i++){
					cout << p[i]<<",";
				}
				cout <<endl;
	*/		//	cin >> k;
				
				int dokad = 0;
				for(int i = 1; i < n; i++){
					if(!rowne(p[i], p[i-1])){
						break;
					}
					dokad = i;
				}
	//			cout << "dokad:" <<dokad<<endl;
				if(dokad == (n-1)){
					for(int i = 0; i < n; i++){
						p[i] = min(1.0l, p[i] + u/((long double)n));
					}
					u = 0.0;
				}
				else{
					long double roznica = (p[dokad + 1] - p[dokad]);
	//				cout << "roz: "<<roznica<<endl;
					for(int i = 0; i <= dokad; i++){
						p[i] += min(roznica, u/(dokad+1.0l));
					}
					if((u/(dokad+1.0l)) >= roznica - eps){
						u -= roznica*(dokad+1.0l);	
					}
					else{
						u = 0.0;	
					}
				}
				
				//sort(p, p + n);		
			}
			res = 1.0l;
			for(int i = 0; i < n; i++){
				res *= p[i];
			}
		}
		cout << "Case #"<<test<<": "<<fixed<<setprecision(8)<<res;
		cout << endl;	
	}
	
	cout << endl;
	return 0;
}
