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

typedef pair<double, double> pii;


double time(double t, double s, double dist){
	return t+dist/s;
}

double solveSmall(vector<vector<double>> &M, vector<pii> &H, int n, int u, int v){
	vector<double> arr (n,-1);
	arr[0] = 0;
	for(int i=0;i<n;i++){
		if(arr[i]!=-1){
		int dist = 0;
		for(int j=i+1;j<n;j++){
			dist+=M[j-1][j];
			if(dist>H[i].fs)
				break;
			double aux = time(arr[i],H[i].sd, double(dist));
			if(arr[j]==-1 || aux<arr[j])
				arr[j] = aux;
		}
		}
	}
	return arr[n-1];
}

int main(){
	int T;
	int n, q;
	double e, s;
	cin >> T;
	for(int t=0;t<T;t++){			
		cout << "Case #" << t+1 << ": ";
		cin >> n >> q;
		vector<vector<double> > M(n,vector<double> (n));
		vector<pii> H (n);
		for(int i=0;i<n;i++){
			cin >> e >> s;
			H[i]=mk(e,s);
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin >> M[i][j];
		int u, v;
		cin >> u >> v;
		cout.precision(6);
		cout << fixed << solveSmall(M,H,n,u-1,v-1) << endl;
		
	}
	return 0;

}
