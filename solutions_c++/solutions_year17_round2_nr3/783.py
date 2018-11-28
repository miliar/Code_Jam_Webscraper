#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long int long_t;
typedef long double ld;

int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		
		int N, Q;
		cin >> N >> Q;
		
		vector<long_t> duration(N);
		vector<long_t> speed(N);
		for(int j = 0; j < N; j++)
			cin >> duration[j] >> speed[j];
			
			
		vector<vector<long_t> > distances(N);
		for(int j = 0; j < N; j++)
		{
			distances[j].resize(N);
			for(int k = 0; k < N; k++)
				cin >> distances[j][k];
		}
		
		
		vector<long_t> sources(Q);
		vector<long_t> targets(Q);
		for(int j = 0; j < Q; j++)
			cin >> sources[j] >> targets[j];
			
		// Small
		vector<ld> dists(N);
		dists[N-1] = 0;
		for(int j = N-2; j >= 0; j--){
			int td = distances[j][j+1];
			ld time = -1;
			for(int k = j+1; td <= duration[j] && k < N; td += distances[k][k+1], k++){
				ld tmp = ((ld) td) / ((ld) speed[j]) + dists[k];
				if(time == -1 || time >= tmp)
					time = tmp;
			}
			
			dists[j] = time;
		}
		
		cout << setprecision(20) << dists[0] << endl;
	}
}
