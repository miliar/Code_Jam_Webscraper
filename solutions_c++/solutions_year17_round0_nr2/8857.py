#include <cstdio>
#include <vector>
using namespace std;

vector<int> v;

bool tidy(){
	for(int i = 0; i < v.size()-1; i++){
		if(v[i] > v[i+1]){
			return false;
		}
	}
	return true; 
}

void solve() {
	for(int i = 0; i < v.size()-1; i++){
		//printf("A\n");
		if(v[i] > v[i+1]){
			v[i]--;
			for(int j = i+1; j < v.size(); j++){
				v[j] = 9;			
			}
		}
	}
}

int main() {
	int t; scanf("%d\n", &t);
	
	for(int k = 0; k < t; k++){
		char c; c = getchar();
		
		while(c != '\n'){
			v.push_back(c - '0');
			c = getchar();
		}
		
		scanf("\n");
		
		while(!tidy()){
			solve();
		}
		
		
		printf("Case #%i: ", k+1);
		bool flag = true;
		for(int i = 0; i < v.size(); i++){
			if(flag){
				while(v[i] == 0) i++;
				flag = false;			
			}
			
			printf("%d", v[i]);
		} printf("\n");
		
		v.clear();
	}
}
