#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n;
	cin>>n;
	int r, c;
	for(int j = 0; j<n; j++){
		cin>>r>>c;
		vector<string> result;
		for(int i = 0; i<r; i++){
			string temp;
			cin>>temp;
			result.push_back(temp);
		}
		int prev_r = 0, prev_c = 0;
		bool empty = false;
		char temp;
		for(int p = 0; p<r; p++){
			if(!empty) prev_r = p;
			empty = true;
			for(int q = 0; q<c; q++){
				if(result[p][q]=='?'){
					if(!empty&&q==c-1){
						for(int t = prev_r; t<=p; t++){
							for(int d = prev_c; d<=q; d++){
								result[t][d] = temp;
							}
						}
					}
					continue;
				}
				empty = false;
				temp = result[p][q];
				for(int t = prev_r; t<=p; t++){
					for(int d = prev_c; d<=q; d++){
						result[t][d] = temp;
					}
				}
				prev_c = q+1;
			}
			if(p==r-1&&empty){
				for(int t = prev_r; t<r; t++){
					result[t] = result[prev_r-1];
				}
			}
			prev_c = 0;
		}

		cout<<"Case #"<<j+1<<":"<<endl;
		for(int i = 0; i<r; i++) cout<<result[i]<<endl;
	}
	return 0;
}