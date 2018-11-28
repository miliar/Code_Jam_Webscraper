
using namespace std;
#include <iostream>
#include <fstream>
int main()
{
	ofstream output("output.txt");
	ifstream input("input.txt");
	int number;
	input >> number;
	for (int numbertwee = 0; numbertwee < number; numbertwee++)
	{
		int N; 
		int opslag3, tosca3, opslag2, anca2, opslag1;
		input >> N;
		if (N == 1000) {
			output << "case #" << numbertwee + 1 << ": 999" << endl;
		}else{
			do {
				opslag3 = N % 10;
				tosca3 = N / 10;
				opslag2 = tosca3 % 10;
				anca2 = tosca3 / 10;
				opslag1 = anca2 % 10;
				if ((opslag3 >= opslag2) && (opslag2 >= opslag1))
				{
					output << "case #" << numbertwee + 1 << ": " << N << endl;
				}
				N--;
			} while (opslag3 < opslag2 || opslag2 < opslag1);
		}
	}
	return 0;
}

