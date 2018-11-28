#include <iostream>
#include <string>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";
		string in;

		cin>>in;

		int flag=0;

		for (int i=0; i<in.length(); ++i) {
			if (flag){
				in[i]='9';
			}else{
				if (i==in.length()-1){
					break;
				}
				int k=i;

				while(k>=0 && in[k]>in[k+1]){
					in[k+1]='9';
					in[k]--;
					flag=1;
					--k;
				}
			}
		}

		if(in[0]=='0'){
			in=in.substr(1);
		}

		cout << in << endl;


	}
}
