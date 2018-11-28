#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	
	
	
	int testNum;

	unsigned __int64 stallNum;
	unsigned __int64 tryNum;
	
	unsigned __int64 num;
	int i,k;
	unsigned __int64 temp;
	unsigned __int64 howManyTopNum;

	int testCase;

	 cin >> testNum;
	
	 for (testCase = 1; testCase <= testNum; testCase++)
	 {

		 cin >> stallNum;
		 cin >> tryNum;


		 num = 0;
		 howManyTopNum = 1;


		 temp = stallNum;
		 for (i = 0; num < tryNum; i++)
		 {
			 num += (unsigned __int64)1 << i;
		 }


		 num -= ((unsigned __int64)1 << (i - 1));



		 for (k = 0; k < i - 1; k++)
		 {

			 if (temp % 2 == 1)
			 {
				 howManyTopNum = (howManyTopNum * 2) + (((unsigned __int64)1 << (k)) - howManyTopNum);
			 }

			 temp = temp / 2;
		 }


		 if ((tryNum - num) <= howManyTopNum)
		 {
		 }
		 else {
			 temp = temp - 1;
		 }


		 cout << "Case #" << testCase << ":" << " ";
		 if (temp == 1)
		 {
			 cout << "0 0" << endl;
		 }
		 else if (temp % 2 == 0)
		 {
			 cout << temp / 2 << " " << (temp / 2) - 1 << endl;
		 }
		 else {
			 cout << temp / 2 << " " << temp / 2 << endl;
		 }
	 }
}