#include <iostream>
#include <unordered_map>

using namespace std;

pair<long, long> compute(long k, long n){

	long delta = 1;

	long v1 = n;
	long n1 = 1;
	long v2 = -1;
	long n2 = 0;
	// v1 > v2
	while(k > delta){
		unordered_map<long,long> tm;
		long tvv1 = -1, tvv2 = -1;
		while(n1--){
			if(v1%2){
				tvv1 = v1/2;
				if(tm.find(tvv1) == tm.end()){tm[tvv1] = 2;}
				else tm[tvv1]+=2;
			}
			else{
				tvv1 = v1/2 - 1;
				tvv2 = v1/2;
				if(tm.find(tvv1) == tm.end()){tm[tvv1] = 1;}
				else tm[tvv1]++;
				if(tm.find(tvv2) == tm.end()){tm[tvv2] = 1;}
				else tm[tvv2]++;
			}
		}

		while(n2--){
			if(v2%2){
				tvv1 = v2/2;
				if(tm.find(tvv1) == tm.end()){tm[tvv1] = 2;}
				else tm[tvv1]+=2;
			}
			else{
				tvv1 = v2/2 - 1;
				tvv2 = v2/2;
				if(tm.find(tvv1) == tm.end()){tm[tvv1] = 1;}
				else tm[tvv1]++;
				if(tm.find(tvv2) == tm.end()){tm[tvv2] = 1;}
				else tm[tvv2]++;
			}		
		}
		n1 = n1<0?0:n1;
		n2 = n2<0?0:n2;
		if(tvv1 < tvv2){
			v1 = tvv2;v2 = tvv1;n1 = tm[tvv2];n2 = tm[tvv1];
		}
		else{
			v1 = tvv1;v2 = tvv2;n1 = tm[tvv1];
			if(tvv2 >= 0) n2 = tm[tvv2];
		}

		// cout << tvv1 << " " << tvv2 <<endl;
		// cout << n1 << " " << n2 << ":" << n1+n2 << endl;
		// cout << v1 << " " << v2 << " " << endl;

		if(v2 == 0) n2 = 0;
		k -= delta;
		delta = (n1 + n2);

		// cout << "k: " << k << endl;
		// cout << "delta: " << delta << endl;
		// cout << endl;
		//if(k == 496) break;

	}

	if(k <= n1){
		if(v1%2){
			return make_pair(v1/2, v1/2);
		}
		else{
			return make_pair(v1/2, v1/2-1);
		}
	}
	else{
		if(v2%2){
			return make_pair(v2/2, v2/2);
		}
		else{
			return make_pair(v2/2, v2/2-1);
		}
	}

}


int main(){

	long T, K, N;

	cin >> T;
	for(long i = 0;i < T;i++){
		cin >> N >> K;
		pair<long, long> r = compute(K, N);
		cout << "Case #" << i+1 << ": " << r.first << " " << r.second << endl;
	}
	return 0;
}

