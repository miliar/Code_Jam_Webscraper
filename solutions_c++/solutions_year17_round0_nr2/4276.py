/*input
4
132
1000
7
111111111111111110
*/
#include <iostream>
#include <string>


int main()
{
	int T, n, flip_ct;
	T = 1;
	std::cin >> n;
	while (T <= n)
	{
		std::string s_in; // cake input
		int K; // flipper size

		std::cin >> s_in;
		int pint, cint;
		bool flag = true;
		while (flag) {
			flag = false;
			for (int i = s_in.length() - 1; i > 0; i--) {
				cint = (int)s_in[i] - 48;
				pint = (int)s_in[i-1] - 48;
				std::cout << cint << " " << pint << std::endl;
				if (cint < pint) {
					flag = true;
					cint = 9;
					pint -= 1;
					s_in[i-1] = (char)(pint + 48); // decrease leading number
					for (int j = i; j < s_in.length(); j++) {
						s_in[j] = (char)(cint + 48);
					}
				}
			}
		}
		if (s_in[0] == '0') {
			s_in.erase(0,1); // remove leading zero if exists
		}
		std::cout << "Case #" << std::to_string(T++) << ": " << s_in <<'\n';
	}
}