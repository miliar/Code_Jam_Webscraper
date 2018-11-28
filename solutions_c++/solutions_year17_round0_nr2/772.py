#include<iostream>
#include<cstdio> 
#include<cstring>
#include<string>
#include<cmath>
using namespace std;
const int INF = 1000000;

int T;
long long N;

int from_int_to_array(int a[], long long d){
	int st = -1; 
	for(int i =0; i < 20; i++ ){
		a[i] = d % 10;
		d /= 10;
		if (a[i] != 0) st = i;
	}
	return st; 
}
long long from_array_to_int(int a[]){
	long long ans = 0;
	int pos = 19;
	while(a[pos] == 0) pos --; 
	for(int i = pos; i >= 0; i--){
		ans *= 10; 
		ans += a[i];
	}
	return ans; 
}

long long solve(){
	cin >> N;
	int a[20], b[20]; 
	int end = from_int_to_array(a, N) ;
	if (end == -1)
		return 0; 
	if(end == 0)
		return a[0];
	int cur_min = a[0];
	int i = 20; 
	for( i = end - 1; i >= 0; i--){
		if(a[i] < a[i + 1])
			break;
		if(i == 0)
		    i = -1;
	}
	if (i == -1)
		return from_array_to_int(a);
	int st = i + 1;
	int j = 20; 
	for(j = end; j >= i + 1; j--){
		if(a[j] == a[st])
			break; 
	} 
//	cout << "a[j]" << a[j] << endl;
//	cout << "j" << j << endl;
	a[j] = a[j] - 1;
	for(int k = j - 1; k >= 0; k--){
		a[k] = 9;
	}

	return from_array_to_int(a); 
}

int main(){
	cin >> T; 
	long long ans; 	
	for(int i = 0; i < T; i++){
		ans = solve();
		cout << "Case #"<< (i+1) << ": " << ans << endl; 
	}	
	return 0;
}
