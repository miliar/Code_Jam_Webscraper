#include<iostream>
#include<vector>

using namespace std;

	
int main() {
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int T;
	long long int N;

	cin >> T;
	int ii = 0;
	for(ii =0; ii < T; ii++){
		cin >> N;
		vector<int> elem;

		while(N > 0){
			int t1 = N % 10;
			elem.push_back(t1);
			N =(long long int) (N-t1)/10LL;
		}
		vector<int> elemRev;

		for(int i2 =0; i2 < elem.size(); i2++){
			elemRev.push_back(elem[elem.size()-1 -i2]);
		}

		vector<int> rv;
		bool done = false;
		int i = 0;


		while(( i < elemRev.size()-1) && (elemRev[i] <= elemRev[i+1])){
			rv.push_back(elemRev[i]);
			i++;
		}

		if(i < elemRev.size()){
			if((i+1)  == elemRev.size()){rv.push_back(elemRev[i]);
			}else{
				while((i > 0) && (elemRev[i] == elemRev[i-1])){
					i--;
					rv.pop_back();
				}
				rv.push_back(elemRev[i]-1);
				for(int l =i+1; l < elemRev.size(); l++){
					rv.push_back(9);
				}
			}
		}

		long long int result = 0;
		long long int pow = 1;
		for(int m = 0; m < rv.size(); m++ ){
			result  = result + rv[rv.size() -1 - m] * pow;
			pow = (long long int)(pow * 10LL);
		}

		cout << "Case #" << ii+1 << ": "<< result<< endl;

	}
}