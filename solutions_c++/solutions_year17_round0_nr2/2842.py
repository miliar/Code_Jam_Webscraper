#include <bits/stdc++.h>
using namespace std;

/*int fb(int x){
	string cad;
	int y;
	for(int i=x; i>=0; i--){
		stringstream ss;
		ss<<i;
		ss>>cad;
		sort(cad.begin(), cad.end());
		//cout<<ss.str()<<endl;
		ss.clear();
		ss<<cad;
		ss>>y;
		//cout<<i<<" ? "<<y<<endl;
		if(i==y){
			//cout<<i<<endl;
			return i;
			break;
		} 
	}
}*/
int main(){
	/* Casosint NN=10000;
	   cout<<NN<<endl;
	   for(int i=1; i<=NN; i++) cout<<i<<endl;
	   return 0;
	*/
	int Test;
	scanf("%d\n", &Test);
	char x[20];
	for(int test=1; test<=Test; test++){
		scanf("%s\n", x);
		int n=strlen(x);
		for(int i=1; i<n; i++){
			if(x[i-1]>x[i]){
				//cout<<i<<endl;
				int k=0;
				for(int j=i-1; j>0; j--){
					if(x[j]>x[j-1]){ k=j; break; }
				}
				//cout<<k<<endl;
				x[k]--;
				for(int j=k+1; j<n; j++) x[j]='9';
				break;
			}
		}
		printf("Case #%d: ", test);
		int i=0; 
		if(x[0]=='0') i++;
		for(; i<n; i++) printf("%c", x[i]);
		printf("\n");
		//cout<<atoi(x)<<" ? "<<fb(atoi(x))<<endl;
		//if(atoi(x)!=fb(atoi(x)) ) cout<<"NO\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nONNONONO"<<endl;
		//else cout<<"NO :("<<endl;
		
	}
	
	return 0;
}
