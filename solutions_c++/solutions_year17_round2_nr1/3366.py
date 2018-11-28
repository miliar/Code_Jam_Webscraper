#if 1
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<set>
#include <sstream>
#include<iomanip>

using namespace std;
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 


int main(){
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	int T;
	int N;
	long D;
	

	cin >> T;


	for(int ii =0; ii < T; ii++){
			cin >> D;
			cin >> N;
		double result = 0;
		vector<double> vi1;
		for(int i =0; i< N; i++){
			int si;
			long ki;
			cin >> ki;
			cin >> si;
			double t1 = (float)(D-ki) /(float) si;
			vi1.pb(t1);
		}
		double v1 = *max_element(vi1.begin(), vi1.end()); 
		if(v1 != 0)
		result = D/v1;
		else
			result = 0.0;


		cout << "Case #" << ii+1 << ": "<< fixed << setprecision(6) << result << endl;
	}

}
#endif