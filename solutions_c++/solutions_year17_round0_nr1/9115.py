#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int main(int argc, char const *argv[])
{	
	int t,
		k;

	string str;

	cin >> t;
	assert(t>=1 && t<=100);

	for (int cs = 0; cs < t; ++cs)
	{
		int swp = 0;
		cin >> str >> k;
		assert(str.length()>=2 && str.length()<=1000);
		assert(k>=1 && k<=str.length());

		size_t pos = str.find('-');
		for (auto itr = begin(str)+pos; itr <  end(str)-k+1;) {
			if(*itr == '-') {
				swp++;
				
				for (auto loop = itr; loop != itr+k; loop++) {
					if(*loop == '-') { 
						*loop = '+';
					} else {
						*loop = '-';
					}
				}

				for (auto i = itr; i != itr+k; ++i)
				{
					if(*i == '+'){
						break;
					}
					else {
						itr++;
					}
				}
			} else {
				itr++;
			}
		}

		if (str.find('-') == string::npos) {
			cout << "CASE #"<< cs+1 << ": " << swp;
		} else {
			cout << "CASE #" << cs+1 << ": " << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
