#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<string>
#include<iomanip>
#include<math.h>

#define INF 99999999
#define MAXN 100003

using namespace std;

typedef long double LD;

int t;
int n;

struct pan{
	long long r,h;	
};

long long pole_boczne(pan x){
	return x.h*x.r*2;	
}
long long pole_kola(pan x){
	return x.r*x.r;	
}

bool operator<(pan a, pan b){
	if(pole_boczne(a) < pole_boczne(b))return 0;
	return 1;	
}

pan p[MAXN];
int k;

long long res;

vector<pan> dobre;

long long max_res;

long double pi = 3.14159265359l;

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> n >> k;
		
		for(int i = 0; i < n; i++){
			cin >> p[i].r >> p[i].h;
		}
		res = 0;
		max_res = 0;
		for(int i = 0; i < n; i++){
		//	cout<<"biore: "<<i<<endl;
			//1. do sumy wybieramy i-tego:
			res = pole_kola(p[i]);
			res += pole_boczne(p[i]);
		//	cout<<"res"<<res<<endl;
			//2. wybierz (k-1) panow o najwyzszym heighcie i r <= p[i].r
			dobre.clear();
			for(int j = 0; j < n; j++){
				if(j != i){
					if(p[j].r <= p[i].r){
		//				cout<<"do dobreych dorzucam: "<<p[j].r<<" "<<p[j].h<<endl;
						dobre.push_back(p[j]);	
					}
				}
			}
			sort(dobre.begin(), dobre.end());
			
		//	if(dobre.size() > 1)cout<<"LOL:" << dobre[0].h << " "<<dobre[1].h<<endl;
			
			if(dobre.size() >= (k-1)){
				for(int j = 0; j < (k - 1); j++){
		//			cout<<"dodaje: "<<dobre[j].r<<" "<<dobre[j].h<<":"<<pole_boczne(dobre[j]);
					res += pole_boczne(dobre[j]);
				}
			}
			max_res = max(max_res, res);
		}
		
		cout << "Case #"<<test<<": "<<fixed<<setprecision(8)<<(long double)max_res*pi<<endl;
			
	}
	
	return 0;
}
