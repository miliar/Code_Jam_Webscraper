#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ofstream fout("B-small-attempt2.out");
	ifstream fin("B-small-attempt2.in");
	int T, N, count, c = 1;
	string num, ans;
	bool yup = true;
	fin >> T;
	while (T--){
		fin >> N;
		for (int i = N; i > 0; i--){
			num = to_string(i);
			count = 0;
			yup = true;
			while (count < num.length() - 1){
				//cout << num << " " <<  i <<  endl;
				if (!(num[count] <= num[count + 1]))
					yup = false;
				count++;
			}
			if (yup){
				ans = num;
				break;
			}
		}
		fout << "Case #" << c << ": " << ans << endl;
		c++;
	}
	//system("pause");
	return 0;
}