#include<conio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
void main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	string s;
	int testCaseCount = 0,k,count=0;
	char c;
	in >> testCaseCount;
	for (int i = 1; i <= testCaseCount; i++){
		count = 0;
		in >> s >> k;
		if (int d = s.find('-') == std::string::npos)
		{
			count=0;
		}
		else{
			for (int j = 0; j < s.length(); j++){
				if (s[j] == '-' && (j+k)<=s.length()){
					for (int jj = j; jj < (j + k); jj++){
						if (s[jj] == '-'){
							s[jj] = '+';
						}
						else{
							s[jj] = '-';
						}
					}
					j = 0;

					count++;
				}
				if (s.find('-')== std::string::npos){
					break;
				}
			}
		}
		if (s.find('-') != std::string::npos){
			for (int j = s.length()-1; j >=0; j--){
				if (s[j] == '-' && (j - k) >=0){
					for (int jj = j; jj > (j - k); jj--){
						if (s[jj] == '-'){
							s[jj] = '+';
						}
						else{
							s[jj] = '-';
						}
					}
					j = s.length() - 1;

					count++;
				}
				if (s.find('-') == std::string::npos){
					break;
				}
			}
		}
		out << "Case #" << i << ": ";
		if (s.find('-') !=std::string::npos){
			out << "IMPOSSIBLE"<<endl;
		}
		else{
			out << count<<endl;
		}
	}
	
	out.close();
	//getch();
}