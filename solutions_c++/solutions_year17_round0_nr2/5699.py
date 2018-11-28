#include<conio.h>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;


int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	string num;
	int T = 0,i,j,k=0;

	in >> T;
	for (i = 1; i <= T; i++){
		in >> num;
		for (j = 0, k = 1; j < num.length() - 1; j++, k++){
			if (num.length()==1)
			{
				break;
			}
			if (num[k] < num[j])
            {
				if (num[j] != '0')
				{
					num[j] --;
				}
				for (int l = k; l < num.length(); l++){
					num[l] = '9';
				}
				if (num[0] == '0')
                {
					num.erase(num.begin());
				}
				j = -1;k = 0;
			}
		}
		out << "Case #" << i << ": ";
		out << num;

		if (i != T)
		{
			out << "\n";
		}
	}

	out.close();
	return 0;
}
