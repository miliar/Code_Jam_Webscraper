#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
	int t, x = 1;
	cin >> t;
	while(t--)
	{
		ll n, k;
		cin >> n >> k;
        if(n == k)
        {
        	cout << "Case #" << x << ": 0 0" << endl;
        	x++;
        	continue;
        }
        vector<int> v;
        int i = 0, y, w, z;
        while(i < k)
        {
        	if(v.size() == 0)
        		y = n;
        	else
        	{
        		y = v[0];
        		v.erase(v.begin());
        	}
        	if(y % 2 == 0)
        	{
        		y = y / 2; w = y; z = y - 1;
        		v.push_back(y);
        		v.push_back(y - 1);
        	}
        	else
        	{
        		y = y / 2; w = y; z = y;
        		v.push_back(y);
        		v.push_back(y);
        	}
        	sort(v.begin(), v.end(), greater<int>());
        	i++;
        }
        cout << "Case #" << x << ": " << w << " " << z << endl;
        x++;
	}

    return 0;
}
