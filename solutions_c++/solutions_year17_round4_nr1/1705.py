#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		int N,P;

		vector <int> gr;

		cin>>N>>P;

		for(int i=0;i<P;++i){
			gr.push_back(0);
		}

		for(int i=0;i<N;++i){
			int tmp;
			cin>>tmp;
			gr[tmp%P]++;
		}

		if (P==2){
			cout << gr[0] + (gr[1]+1)/2 << endl;

		}

		if (P==3){
			cout << gr[0] + min(gr[1], gr[2]) + ((max(gr[1], gr[2]) - min(gr[1], gr[2]) + 2)/3)<<endl;
		}


	}
}

