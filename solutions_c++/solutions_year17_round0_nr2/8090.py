#include<conio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
void main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	string num;
	int testCaseCount = 0,i,j,k=0,count=0;
	char c;
	in >> testCaseCount;
	for (i = 1; i <= testCaseCount; i++){
		in >> num;
		for (j = 0, k = 1; j < num.length() - 1; j++, k++){
			if (num.length()==1)
			{
				break;
			}
			if (num[k] < num[j]){
				if (num[j] != '0'){
					num[j] --;
				}
				for (int l = k; l < num.length(); l++){
					num[l] = '9';
				}
				if (num[0] == '0'){
					num.erase(num.begin());
				}
				j = -1;
				k = 0;
			}
		}
		out << "Case #" << i << ": ";
		out << num;
		if (i != testCaseCount)
		{
			out << endl;
		}
	}
	
	out.close();
}