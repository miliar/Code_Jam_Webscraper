#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;
int main()
{
	ofstream file("Ali.txt.txt");
	int t,l=1;
	cin >> t;
	while (t--){
		file << "Case #" << l << ": ";
		map<long long, long long>m;
		long long n,k,a,b;
		map<long long, long long>::iterator it;
		cin >> n;
		m.insert(make_pair(n, 1));
		cin >> k;
		while (k != 0)
		{
			it = m.end(); 
			it--;
			if (it->second >= k)
			{
				a = it->first;
				b = a / 2;
				if (a % 2 == 0)
				{
					a /= 2;
					a--;
				}
				else
				{
					a /= 2;
				}
				break;
			}
			else
			{
				k -= it->second;
				a = it->first;
				b = a / 2;
				if (a % 2 == 0)
				{
					a /= 2;
					a--;
				}
				else
				{
					a /= 2;
				}
				long long u = it->second;
				m.erase(it);
				it = m.find(a);
				if (it == m.end()){
					m.insert(make_pair(a, u));
				}
				else
				{
					it->second += u;
				}
				it = m.find(b);
				if (it == m.end()){
					m.insert(make_pair(b, u));
				}
				else
				{
					it->second += u;
				}
			}
		}
		file << b << " " << a << endl;
		l++;
	}
	 system("pause");
}