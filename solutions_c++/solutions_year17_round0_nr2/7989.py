#include <bits/stdc++.h>

#define fst first
#define snd second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

vector<int> num;

bool check(){
	for(int i = 1; i < num.size(); i++)
		if(num[i] < num[i-1]) return false;
	return true;
}

void convert(){
	while(!check()){
		for(int i = num.size()-2; i >= 0; i--){
			if(num[i] == 0) continue;
			if(num[i] > num[i+1]){
				num[i]--;
				for(int j = i+1; j < num.size(); j++) num[j] = 9;
			}
		}
	}
}

void print(){
	for(int i = 0; i < num.size(); i++)
		if(num[i] != 0) printf("%d",num[i]);
}

int main(){

	int tc,n;
	char c;
	cin >> tc; scanf("\n");
	for(int t = 0; t < tc; t++){
		string cad; cin >> cad;
		num.clear();
		for(int i = 0; i < cad.size(); i++)
			num.pb(cad[i]-'0');
		if(check()){
			printf("Case #%d: ",t+1);
			print(); printf("\n");
			continue;
		}
		convert();
		printf("Case #%d: ",t+1);
		print(); printf("\n");
	}

	return 0;
}