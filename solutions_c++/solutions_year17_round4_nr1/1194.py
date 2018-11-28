#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
void main2(){
	int N,P;
	cin >> N >> P;
	vector<int> G;
	array<int,5> md;
	md.fill(0);
	for(int i=0;i<N;i++){
		int x;
		cin >> x;
		md[x%P]++;
		G.push_back(x);
	}
	if(P==2){
		cout << md[0]+(md[1]+1)/2;
	} else if(P==3){
		int mn=min(md[1],md[2]);
		int lf=abs(md[1]-md[2]);
		cout << md[0]+mn+(lf+2)/3;
	} else {
		int tot = md[0];
		int o1 = md[2];
		int mn = min(md[1],md[3]);
		int lf = abs(md[1]-md[3]);
		tot+=o1/2+mn;
		o1%=2;
		if(o1==1 && lf>=2){
			tot++;
			o1=0;
			lf-=2;
		} else if(o1==1 && lf<2){
			tot++;
			lf=0;
		}

		tot+=(lf+3)/4;
		
		cout << tot;
	}

}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}