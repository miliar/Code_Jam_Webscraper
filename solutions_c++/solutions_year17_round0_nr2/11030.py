#include <iostream>  
#include <string> 
#include<algorithm>
#include <fstream>
// includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	//int t,k,negr=0,negl=0,posr=0,posl=0,allne=0,allpo=0;
	//string s;
	//cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	//for (int i = 1; i <= t; ++i) {
	//	cin >> s >> k ;  // read n and then m.
	//	//handle all pos and all nves
	//	for (int init = 0; init <s.length(); init++)
	//	{
	//		if (s[init] == '-')
	//			allne++;
	//	}
	//	for (int init = 0; init <s.length(); init++)
	//	{
	//		if (s[init] == '+')
	//			allpo++;
	//	}
	//	if (allne == s.length() &&k>=2)
	//		cout << "Case #" << i << ": " << s.length()/k << endl;
	//			if (allpo == s.length() && k>=2)
	//		cout << "Case #" << i << ": " << 0 << endl;

	//			allne, allpo = 0;

	//	for (int in = 0,j=s.length()-1; in < k,j>=0; ++in ,--j)
	//	{
	//		if (s[in] == '-'){
	//			negr++;
	//			if (negr == k && in==k-1)break;
	//		}
	//		if (s[j] == '-'){
	//			negl++;
	//			if (negl == k && j == 0)break;
	//		}
	//		if (s[in] == '+'){
	//			posl++;
	//			if (posl == k && in == k - 1)break;
	//		}
	//		if (s[j] == '+'){
	//			posr++;
	//			if (posr == k && j == 0)break;
	//		}

	//	}
	//	if (negr == k || negl == k)

	//	cout << "Case #" << i << ": " << k<< endl;
	//	else if((posr==k||posl==k ))
	//		cout << "Case #" << i << ": " <<0<< endl;
	//	else
	//		cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	//	negr = negl = posl = posr = 0;
	//	// cout knows that n + m and n * m are ints, and prints them accordingly.
	//	// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	//}

	
	string t;
	string num;
	//cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	ifstream myfile("B-small-attempt2.in");
	if (myfile.is_open())
	{
		getline(myfile, t);
		
	}
	int ti = stoi(t);
	for (int i = 1; i <= ti; ++i) {
		getline(myfile, num);
		//cin >> num ;  // read n and then m.
		//string s = to_string(num);
		int temp = stoi(num);
		sort(num.begin(), num.end());
		int sorted = stoi(num);
		if (temp >= 1 && temp <= 9)
			cout << "Case #" << i << ": " << num << endl;
		else{
			while (temp != sorted)
			{
				temp -= 1;
				string s = to_string(temp);
				sort(s.begin(), s.end());
				sorted = stoi(s);
			}

				cout << "Case #" << i << ": " << sorted << endl;
		}
			
		
			//cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}