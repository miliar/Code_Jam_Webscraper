#include <iostream>
#include <string>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";
		string in;
		int K;
		cin>>in>>K;

		int ret = 0;

		for (int i=0; i<in.length(); ++i) {
			if (in[i] != '+') {
				if (i + K <= in.length()) {
					++ret;
					for (int j=i; j<i+K; ++j){
						char tmp = in[j];
						in[j]=tmp=='+'?'-':'+';
					}
				}else{
					ret = -1;
				}
			}
		}

		if (ret == -1) {
			cout <<"IMPOSSIBLE"<<endl;
		}else{
			cout<<ret<<endl;
		}


	}
}
