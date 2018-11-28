#include <bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	std::vector<string> numbers;
	for (int i = 1; i <= 17; ++i){
		for (int j = 1; j <= 9; ++j){
			string aux="";
			for (int k = 1; k <= i; ++k){
				string aux2=static_cast<std::ostringstream*>(&(std::ostringstream() << j )) ->str();
				aux=aux+aux2+"";
			}
			numbers.push_back(aux);
		}
	}
	int t;
	cin>>t;
	int pp=0;
	std::vector<long long> res;
	while(t--){
		long long n;
		cin>>n;
		int cd=1;
		long long num=0;
		string auxnum="";
		for (int i = numbers.size()-1; i >= 0; --i){
			num=atoll(numbers[i].c_str());
			//cout<<num<<endl;
			if(num<=n)
				break;
		}
		//cout<<num<<endl;
		auxnum=static_cast<std::ostringstream*>(&(std::ostringstream() << num )) ->str();
		int kd=0;
		while(kd==0){
			for (int i = cd; i < auxnum.size(); ++i){
				if(auxnum[i]=='9'){
					cd++;
					break;
				}
				auxnum[i]++;
			}
			long long auxnum1=atoll(auxnum.c_str());
			if(auxnum1<=n){
				num=auxnum1;
			}
			else{
				auxnum=static_cast<std::ostringstream*>(&(std::ostringstream() << num )) ->str();
				cd++;
			}
			//cout<<cd<<endl;
			if(cd>auxnum.size()-1)
				break;
		}
		res.push_back(num);
	}
	for (int i = 0; i < res.size(); ++i){
		
		cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
	}
	//system("pause");
	return 0;
}