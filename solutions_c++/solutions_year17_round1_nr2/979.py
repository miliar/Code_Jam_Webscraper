#include<iostream>
#include<algorithm>
using namespace std;

int t,n,p;

long long quantity[100][100];
bool used[100][100];
long long recipe[100];

long long tab1[100];

long long tab2[100];

int res;

bool is_ok(int ind_a, int ind_b){
	for(int i = 1; i <= 1000000; i++){
		if(tab1[ind_a]*100 >= recipe[0]*i*90 && tab1[ind_a]*100 <= recipe[0]*i*110 && tab2[ind_b]*100 >= recipe[1]*i*90 && tab2[ind_b]*100 <= recipe[1]*i*110){
			return true;
		}
	}
	return false;
}
bool is_ok(int ind_a){
	for(int i = 1; i <= 1000000; i++){
		if(quantity[0][ind_a]*100 >= recipe[0]*i*90 && quantity[0][ind_a]*100 <= recipe[0]*i*110){
			return true;
		}
	}
	return false;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin >> t;
	for(int test = 0; test < t; test++){
		cin >> n >> p;
		for(int i = 0; i < n; i++){
			cin >> recipe[i];
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < p; j++){
				cin >> quantity[i][j];
				used[i][j] = 0;
			}
		}
		if(n == 2){
			
			for(int i = 0; i < p; i++){
				tab1[i] = quantity[0][i];
				tab2[i] = quantity[1][i];
			}
			sort(tab1, tab1 + p);
			sort(tab2, tab2 + p);
			
			res = 0;
			for(int i = 0; i < p; i++){
				for(int j = 0; j < p; j++){
					if(is_ok(i, j) && used[0][i] == 0 && used[1][j] == 0){
						used[0][i] = 1;
						used[1][j] = 1;
						res++;
					}
				}
			}
		}
		else{
			res = 0;
			for(int i = 0; i < p; i++){
					if(is_ok(i)){
						res++;
					}
			}
		}
		
		
		cout << "Case #"<<test+1<<": "<<res<<endl;
		
	}


return 0;
}