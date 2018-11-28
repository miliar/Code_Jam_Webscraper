#include<iostream>
#include<string>
#include<algorithm>
#include<utility>
#include<vector>
#include<queue>
using namespace std;

#define fs first
#define sd second
#define mk make_pair



int R, O , Y, G, B, V;


int solveSmall(vector<int> &aux, vector<int> &Sol){
	vector<int> Bs = aux;
	sort(Bs.begin(),Bs.end(),[](int x, int y){return x>y;});
	if(Bs[0]>Bs[1]+Bs[2])
		return -1;
	int fin;
	for(fin=0;fin<Bs[0];fin++)
		Sol[3*fin] = 1;
	for(int i=0;i<Bs[1];i++)
		Sol[3*i+1] = 2;
	for(int i=0;i<Bs[2];i++)
		Sol[3*(fin-1-i)+2] = 3;
	return 1;
}

void imprime(char c){
	if(c=='R'){
		while(G>0){
			cout << "RG";
			G--;
		}
	}
	if(c=='B'){
		while(O>0){
			cout << "BO";
			O--;
		}
	}
	if(c=='Y'){
		while(V>0){
			cout << "YV";
			V--;
		}
	}
	cout << c;
}

void print(vector<int> &Bs, vector<int> &Sol, char Max, char Med, char Min, int n){
	for(int i=0;i<3*n;i++){
		if(Sol[i]==1)
			imprime(Max);
		if(Sol[i]==2)
			imprime(Med);
		if(Sol[i]==3)
			imprime(Min);
	}
	cout << endl;
}




int solveLarge(vector<int> &Sol, int n){
	if(O>0 && O+B==n && O==B){
		for(int i=0;i<O;i++) cout << "OB";
		cout << endl;
		return 1;
	}
	if(G>0 && G+R==n && G==R){
		for(int i=0;i<G;i++) cout << "GR";
		cout << endl;
		return 1;
	}
	if(V>0 && V+Y==n && V==Y){
		for(int i=0;i<V;i++) cout << "VY";
		cout << endl;
		return 1;
	}
	if(O>=B && O>0) return -1;
	if(G>=R && G>0) return -1;
	if(V>=Y && V>0) return -1;
	vector<int> bs ={R-G,Y-V,B-O};
	if( solveSmall(bs,Sol)==-1)
		return -1;
	vector<pair<int,char>> p (3);
	p[0] = mk(R-G,'R');
	p[1] = mk(Y-V,'Y');
	p[2] = mk(B-O,'B');
	sort(p.begin(),p.end());
	print(bs,Sol,p[2].sd,p[1].sd,p[0].sd,n);
	
}


int main(){
	int T, n;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		cin >> n;
		cin >> R >> O >> Y >> G >> B >> V;
		
		vector<int> Sol(3*n,0);
		if( solveLarge(Sol,n)==-1)
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;

}
