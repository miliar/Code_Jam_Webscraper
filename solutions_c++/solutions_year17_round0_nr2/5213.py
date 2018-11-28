#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool good(string n_str)
{
	for(int i = 1; i < (int)n_str.length(); i++)
	{
		if(n_str[i] < n_str[i - 1])
			return false;
	}
	return true;
}

string get_tidy_num(string n_str)
{
    for(int i = n_str.length() - 1; i > 0; i--)
    {
    	n_str[i] = '9';
    	if(n_str[i - 1] > '0')
    	    n_str[i - 1]--;
        if(good(n_str))
        	break;
    }
    n_str.erase(0, n_str.find_first_not_of('0'));
    return n_str;
}

int main()
{
	int t, x = 1;
	cin >> t;
	while(t--)
	{
		ll n;
		cin >> n;
		if(good(to_string(n)))
	        cout << "Case #" << x << ": " << n << endl;
		else
		    cout << "Case #" << x << ": " << get_tidy_num(to_string(n)) << endl;
		x++;
	}
    return 0;
}
