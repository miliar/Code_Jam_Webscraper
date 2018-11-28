#include <iostream>
#include <map>

using namespace std;

int T;
long long N, K;

map<long long, long long> mymap;

void printAnswer(long long N, long long K){
	mymap.clear();	
	mymap[-N] = 1;
	
	while ( true ){
		map<long long, long long>::iterator it= mymap.begin();
		long long big = -(it->first+1); 
		long long num = it->second;
		if ( K <= num ){
			if (big%2 == 0)
				cout << big/2 << " " << big/2;
			else
				cout << big/2+1 << " " << big/2;
			return ;
		}
		K -= num;
		mymap.erase(it);

		if ( big%2 == 0 ){
			map<long long, long long>::iterator save = mymap.find(-(big/2));
			if ( save == mymap.end() )			
				mymap[-big/2] = 2*num;
			else
				save->second += 2*num;
		}
		else {
			map<long long, long long>::iterator save = mymap.find(-(big/2+1));
			if (save == mymap.end() )
				mymap[-(big/2+1)] = 1*num;
			else
				save->second += 1*num;

			save = mymap.find(big/2);
			if (save ==mymap.end() )
				mymap[-(big/2)] = 1*num;
			else
				save->second += 1*num;
		}

	}

}

int main(){
	cin >> T;
	for(int i = 1;i<=T; i++){
		cin >> N >> K;
		printf("Case #%d: ", i);
		printAnswer(N, K);
		printf("\n");
	}
	return 0;
}

