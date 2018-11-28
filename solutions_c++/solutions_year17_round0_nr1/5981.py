#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;


int main() 
{
	std::cin.sync_with_stdio(false);
	int T;
	cin >> T;
	
	for (int c = 0; c<T; ++c)
	{
		string seq;
		int K;
		cin >> seq >> K;
		set<int> p;
		if (seq[0] == '-')
			p.insert(0);
		int pos = 0;
		while (seq[pos] == seq[0])
			++pos;

		for (;pos < seq.size(); ++pos)
			if (seq[pos] != seq[pos-1])
				p.insert(pos);
		int flips = 0; 
		vector<int> to_erase;
		for (auto i:p)
		{
			if (i+K > seq.size())
				break;
			if (p.count(i+K))
				p.erase(i+K);
			else
				p.insert(i+K);
			to_erase.push_back(i);
			++flips;
		}
		for (auto i:to_erase)
			p.erase(i);
		
		if (p.size()>0 && *p.begin() < seq.size())
			flips = -1;
		
		
		cout << "Case #" << c+1 << ": ";
		if (flips >= 0)
			cout << flips;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	

}
