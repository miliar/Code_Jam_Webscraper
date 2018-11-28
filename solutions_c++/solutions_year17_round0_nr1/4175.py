#include <iostream> 
#include <fstream> 
#include <cstdlib> 
#include <cstring> 
#include <algorithm> 
#include <vector> 
using namespace std;  

#define MAXN 1111 
int T,N; 
int dir[MAXN]; // (happy:0, blank:1)
int f[MAXN];
int calc(int k){
	memset(f,0,sizeof(f)); 
	int res = 0, sum = 0; 
	for (int i = 0; i+k <= N; i++){
		if ((dir[i]+sum)%2 != 0){
			res++;  
			f[i] = 1;  
		}
		sum += f[i];  
		if (i-k+1 >= 0){
			sum -= f[i-k+1];  
		}
	}
	for (int i = N-k+1; i < N; i++){
		if ((dir[i]+sum)%2 != 0){
			return -1; 
		}
		if (i-k+1 >= 0){
			sum -= f[i-k+1];   
		}
	}
	return res;  
}
int main(){
	cin >> T;
	for (int test = 1; test <= T; test++){
		memset(dir,0,sizeof(dir)); 
		string s; 
		int k;  
		cin >> s; 
		cin >> k;  
		N = s.size();  
		for (int i = 0; i < N; i++){
			if (s[i] == '+') dir[i] = 0; 
			else dir[i] = 1;    
		}
		int ans = calc(k); 
		cout << "Case #" << test << ": ";  
		if (ans == -1) cout << "IMPOSSIBLE" << endl; 
		else cout << ans << endl; 
	} 
	return 0; 
}