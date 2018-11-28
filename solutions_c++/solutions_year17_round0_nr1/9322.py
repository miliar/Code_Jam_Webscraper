#include<bits/stdc++.h>

using namespace std;

int main(){
	int t;
	int cont = 0;
	
	scanf("%d", &t);
	
	while(t--){
		cont++;
		vector<int> v(1005);
		string s;
		int k;
		
		for(int i = 0; i < v.size(); i++)
			v[i] = 0;
		
		cin >> s;
		scanf(" %d", &k);
		
		int flip = 0;
		
		for(int i = 0; i <= s.size() - k; i++){
				if((s[i] == '-' && v[i] == 0) || (s[i] == '+' && v[i] == 1)){
					flip++;
					for(int j = i; j < i + k; j++)
						v[j] = 1 - v[j];
				}
		}
		
		int poss = 1;
		
		for(int i = s.size() - k; i < s.size(); i++){
			if((s[i] == '-' && v[i] == 0) || (s[i] == '+' && v[i] == 1))
				poss = 0;
		}
		
		printf("Case #%d: ", cont);
		if(poss)
			printf("%d\n", flip);
		
		else
			printf("IMPOSSIBLE\n");
	}
	
	return 0;
}