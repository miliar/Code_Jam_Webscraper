#include <bits/stdc++.h>

using namespace std;

char cambiar(char x){
	if(x=='-')
		return '+';

	return '-';
}

int main(){

	int tc;
	scanf("%d",&tc);
	int nx = 1;
	while(tc--){
		string s;
		int k;
		cin >> s >> k;
		//cout << s << " " << k << " "; 

		int sz = s.size();
		int cambios = 0;

		for(int i=0 ; i<sz-k+1; i++){

			if(s[i] == '-'){
			//	cout << "Encontre -"<<endl;
				cambios++;
				for(int j=0 ; j<k ; j++){
					s[i+j] = cambiar(s[i+j]);
				}
			}
		}
	//	cout << "RES: " << s << endl;
		bool flag = true;

		for(int i=0 ; i<sz; i++){
			if(s[i]=='-'){
				flag = false;
				break;
			}
		}

		printf("Case #%d: ", nx++);

		if(flag)
			printf("%d\n",cambios );
		else
			printf("IMPOSSIBLE\n");
	}

}