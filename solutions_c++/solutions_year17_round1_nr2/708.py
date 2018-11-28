#include <iostream>
#include <vector>  
#include <algorithm>  
using namespace std; 

int get_next_amount(vector<int>& index, int N, vector<vector<int> >& least){
	int result = 0;
	for (int j = 0; j < N; j++){
		result = max(result, least[j][index[j]]);
	}
	return result;
}

int solve(vector<int>& R, vector<vector<int> >& Q, vector<vector<int> >& least, vector<vector<int> >& most, int N, int P){
	vector<int> index(N, 0);
	bool done = false;
	int kits = 0;
	while (!done){
		int next_amount = get_next_amount(index, N, least);
		for (int j = 0; j < N; j++){
			while (most[j][index[j]] < next_amount){
				index[j]++;
				if (index[j] == P){
					done = true;
					break;
				}
			}
			if (done)
				break;
			if (least[j][index[j]] > next_amount){
				break;
			}
			if (j == N-1){
				kits++;
				for (int jj = 0; jj < N; jj++){
					index[jj]++;
					if (index[jj] == P){
						done = true;
						break;
					}
				}
			}			
		}
	}
	return kits;
}
 
void main()
{
	int T;
	cin >> T;
	for (int i = 1 ; i <= T; i++){
		int N, P;
		cin >> N >> P;
		vector<int> Rarray(N, 0);
		vector< vector<int> > Qarray(N, vector<int>(P, 0));
		for (int j = 0; j < N; j++){
			cin >> Rarray[j];
		}
		for (int j = 0; j < N; j++){
			for (int k = 0; k < P; k++){
				cin >> Qarray[j][k];
			}
		}
		for (int j = 0; j < N; j++){
			sort(Qarray[j].begin(), Qarray[j].end());
		}
		vector< vector<int> > least(N, vector<int>(P,0));
		vector< vector<int> > most(N, vector<int>(P,0));
		for (int j = 0; j < N; j++){
			for (int k = 0; k < P; k++){
				double ratio = (static_cast<double>(Qarray[j][k])) / Rarray[j];
				int high = floor(ratio / 0.9);
				int low = ceil(ratio / 1.1);
				if (low > high) {
					least[j][k] = -1;
					most[j][k] = -1;
				}
				else{
					least[j][k] = low;
					most[j][k] = high;
				}
				
			}
		}
		int kits = solve(Rarray, Qarray, least, most, N, P);
		cout << "Case #" << i << ": " << kits << endl;
	}


}