#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln t;
	cin >> t;
	for(lln i=0;i<t;i++){
		lln n;
		cin >> n;
		vector <lln> v;
		lln j=0;
		while(n!=0){
			v.push_back(n%10);
			n = n/10;
			j++;
		}
		lln z = v.size()-1;
		while(z!=0){
			for(lln k=v.size()-1;k>=0;k--){
				if((k-1)>=0 and v[k-1]<v[k]){
					v[k] = v[k]-1;
					for(lln u=k-1;u>=0;u--){
						v[u] = 9;
					}
				}
			}
			z--;
		}
		lln flag=0;
		cout << "Case #" << i+1 << ": ";
		for(lln k=v.size()-1;k>=0;k--){
			if(v[k]!=0)
				flag=1;
			if(flag==1)
				cout << v[k];
		}
		cout << endl;
	}
	return 0;
}