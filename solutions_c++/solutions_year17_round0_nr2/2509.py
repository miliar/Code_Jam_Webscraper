#include <iostream>
#include <fstream>
#include <deque>
#include <algorithm>
#include <functional>

using namespace std;

ofstream out("out.txt");
ifstream in("in.txt");


int main()
{
	int T;
	in >> T;
	for (int cn = 1; cn <= T; cn++)
	{
		long long int N;
		in>>N;
		deque<int> n;
		for (long long temp = N; temp != 0; temp /= 10)
		{
			n.push_front(temp % 10);
		}
		deque<int>::iterator last_tidy = adjacent_find(n.begin(), n.end(), greater<int>());
		//std::cout << *last_tidy << endl;
		if (last_tidy == n.end())
		{
			out << "Case #" << cn << ": " << N << endl;
			continue;
		}
		for (; last_tidy != n.begin(); last_tidy--)
		{
			(*last_tidy)--;
			if (*(last_tidy - 1) <= *last_tidy)break;
		}
		if (last_tidy == n.begin())
		{
			n[0]--;
		}
		last_tidy++;
		for (; last_tidy < n.end(); last_tidy++)
			*last_tidy = 9;
		N = 0;
		for (last_tidy = n.begin(); last_tidy < n.end(); last_tidy++)
		{
			N *= 10;
			N += *last_tidy;
		}
		out << "Case #" << cn << ": " << N << endl;
	}
}
