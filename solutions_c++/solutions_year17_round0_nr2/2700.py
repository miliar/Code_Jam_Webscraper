#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

using lli = long long int;

lli tidy(lli num){
	if (num % 10 == (num/10)%10)
		return tidy(num / 10) * 10 + 9;
	else return num - 1;
}

void resolve(int ncas){
	cout << "Case #" << ncas + 1 << ": ";
	string str;
	cin >> str;

	if (str.size() == 1)
		cout << str << '\n';
	else{
		int i = 1;
		while (i < str.size() && str[i - 1] <= str[i])
			++i;
		if (i == str.size())
			cout << str << '\n';
		else {

			lli num = stoll(str.substr(0, i));
			num = tidy(num);
			while (i < str.size()){
				num = num * 10 + 9;
				++i;
			}

			cout << num << '\n';
		}
	}
}

int main(){

	ifstream in("B-large.in");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream on("B-large.txt");
	auto coutbuf = cout.rdbuf(on.rdbuf()); //save old buf and redirect std::cin to casos.txt


	int numCasos;
	cin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolve(i);

	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);

	return 0;
}