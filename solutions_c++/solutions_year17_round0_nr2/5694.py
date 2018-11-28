#include <iostream>
#include <vector>
#include <algorithm>

using namespace std; 

int main() 
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t; 
	for (int x = 1; x <= t; x++)
	{
		unsigned long long int n;
		cin >> n;

		vector<int> v;
		while (n)
		{
			v.push_back(n % 10);
			n /= 10;
		}

		reverse(v.begin(), v.end());
		
		if (v.size() == 1)
		{
			cout << "Case #" << x << ": " << v[0] << "\n";
			continue;
		}

	    for (int i = v.size() - 2; i >= 0; i--)
	    {
			if (v[i] > v[i + 1])
			{
				v[i]--;
				fill(v.begin() + i + 1, v.end(), 9);
			}
	    }

    	cout << "Case #" << x << ": ";
    	int start = 0;
    	while(!v[start])
    		start++;
    	for (int i = start; i != v.size(); i++)
      		cout << v[i];
    	cout << "\n";
	}

	return 0;
}