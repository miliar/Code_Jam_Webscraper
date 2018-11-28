#include<iostream>
#include<string>
#include<fstream>
using namespace std;

string filename = "A-large.in";
int main() {

	ifstream fin(filename); // 파일 입력

	int T;
	//cin >> T;
	fin >> T;
	for (int i = 1; i <= T; i++) {

		string N;
		int size;
		int count = 0;

		fin >> N>>size;
		//cin >> N >> size;
		string result;
		int length = N.length();
		for (int j = 0; j <= length-size;j++)
		{
			
			if (N.at(j) == '-')
			{
				result = N.substr(0,j);
				for (int k = 0; k < size; k++)
				{
					if(N.at(j+k)=='-') result+= "+";
					else result += "-";					
				}
				count++;
				result += N.substr(j + size, length - 1);
				N = result;
			}
		}

		if(N.find("-")!=-1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE"<< endl;
		else 
			cout << "Case #" << i << ": " << count << endl;
		
	}
	system("pause");
}
