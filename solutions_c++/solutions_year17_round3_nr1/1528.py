#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include<vector>
#include<algorithm>
#include <math.h>
#include<iomanip>


using namespace std;

double getArea(double R, double H)
{
	return (2 * M_PI * R * H) + (M_PI * R * R);
}

int main(){
	int i,j,k,l;
	string str;
	int N, K, T;
	cin>>T;
	for(l = 0 ; l < T ; l++){
		cin>>N>>K;
		double *R = new double[N];
		double *H = new double[N];
		for(i = 0 ; i < N ; i++)
			cin>>R[i]>>H[i];
		vector<pair<double, double> > dim;
		for(i = 0 ; i < N ; i++)
			dim.push_back(make_pair(R[i], H[i]));
		sort(dim.begin(), dim.end(), greater<pair<double, double> > ());
		double **table = new double *[N];
		for(i = 0 ; i < N ; i++)
			table[i] = new double[K + 1];
		for(i = 0 ; i < N ; i++)
			table[i][0] = 0.0;
		for(i = 1 ; i <= K ; i++)
			table[0][i] = getArea(dim[0].first, dim[0].second);
		for(i = 1 ; i < N ; i++){
			for(j = 1; j <= K ; j++){
				table[i][j] = max(table[i - 1][j], getArea(dim[i].first, dim[i].second));
				table[i][j] = max(table[i][j], table[i - 1][j - 1] + getArea(dim[i].first, dim[i].second) - (M_PI * dim[i].first * dim[i].first));
			}
		}
		/*for(i = 0 ; i < N ; i++)
		{
			for(j = 0 ; j <= K ; j++)
				cout<<table[i][j]<<"\t";
			cout<<"\n";
		}*/
		cout<<setprecision(30);
		cout<<"Case #"<<l + 1<<": "<<table[N - 1][K]<<"\n";
		for(i = 0 ; i < N ; i++)
			delete[] table[i];
		delete[] table;
		delete[] R;
		delete[] H; 
	}
	return 0;
}
